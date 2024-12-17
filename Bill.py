import mysql.connector
from time import gmtime, strftime
import random
import os

class Bill():
    billName = ""

    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="0912752882ha",
            database="PetShop"
        )
        pass

        self.total = 0

    def calculateBill(self, ID, billType):
        tableLabel = ""
        priceLabel = ""
        if (billType == "IMPORT"):
            tableLabel = "ImportGoods"
            priceLabel = "PriceBuy"
        elif (billType == "ORDER"):
            tableLabel = "Orders"
            priceLabel = "PriceSell"

        query = """SELECT Products.ProductID, ProductName, Quantity, {price}
                FROM {bill} JOIN Products ON {bill}.ProductID=Products.ProductID
                WHERE ID={id}
                """.format(price=priceLabel, bill=tableLabel, id=ID)
        cursor = self.db.cursor()
        cursor.execute(query)

        result = cursor.fetchall()

        self.printBill(result[0][1], result[0][2], result[0][3])

        self.total += result[0][2] * result[0][3]
        return 

    def printBill(self, lstProduct, date):
        filename = random.randint(100001, 999999)
        cwd = os.getcwd()
        cwd = cwd + "/bills/"
        self.billName = "{fi}.txt".format(fi=filename)
        f = open(cwd + "{fi}.txt".format(fi=filename), "w")
        f.write("		Cua hang thu cung\n")
        f.write("	 Lien he so. 01122334455 , AMM-2003\n")
        f.write("===============================================\n")
        f.write("Ten khach hang: Nga ngo\n")
        f.write("Hoa don so: ")
        f.write("{}".format(filename).ljust(10))
        f.write("       Ngay: ")
        f.write("{}".format(date).ljust(10))
        f.write("\n")
        f.write("===============================================\n")
        f.write("Ten san pham".ljust(25) + "So luong".ljust(14) + "Gia".ljust(10))
        f.write("\n===============================================\n\n")
        subtotalPrice = 0
        for pr in lstProduct:
            spname = pr[1]
            spquan = pr[2]
            price = round(float(pr[2]) * float(pr[3]), 2)
            f.write("{}".format(spname).ljust(25))
            f.write("{}".format(spquan).ljust(14))
            f.write("{}".format(price).ljust(10))
            f.write("\n")
            subtotalPrice = subtotalPrice + price

        subtotalPrice = round(float(subtotalPrice), 2)
        tax = round(float(subtotalPrice) * 0.1, 2)
        total = round(float(subtotalPrice) * 1.1, 2)

        f.write("\n===============================================\n")
        f.write("Tien thanh toan".ljust(39))
        f.write("{}".format(subtotalPrice).ljust(10))
        f.write("\n")
        f.write("Thue".ljust(39))
        f.write("{}".format(tax).ljust(10))
        f.write("\n")
        f.write("Tong can thanh toan".ljust(39))
        f.write("{}".format(total).ljust(10))
        f.write("\n===============================================\n")
        f.close()

    def closeService(self):
        self.db.close()