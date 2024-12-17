import mysql.connector
from Product import *
from Bill import *
from datetime import datetime
import locale
import os

class Service():
    orderProduct = []
    numProduct = 0
    mainFrameStatus = 0
    statisData = []
    billList = []
    
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="0912752882ha",
            database="PetShop"
        )
        locale.setlocale(locale.LC_ALL, 'vi_VN')

        self.product = Product()
        self.bill = Bill()
        self.statisData = []
        pass

    def closeService(self):
        self.bill.closeService()
        self.product.closeService()
        self.db.close()

    def clearListOrder(self):
        self.orderProduct.clear()

    def getTypeProduct(self):
        cursor = self.db.cursor()

        cursor.execute("SELECT TypeName FROM ProductType;")
        requestType = cursor.fetchall()

        cursor.close()
        return requestType

    def getProductListFromType(self, id):
        cursor = self.db.cursor()
        query = "SELECT ProductName FROM Products WHERE TypeID={ID}".format(ID=id)
        cursor.execute(query)
        requestType = cursor.fetchall()
        cursor.close()
        return requestType

    def availabelProduct(self, id):
        availabel = self.product.getAvailabelProduct(id)
        return availabel

    def getProductPrice(self, id, kind):
        cursor = self.db.cursor()
        query = ""
        if (self.mainFrameStatus == 2):
            query = "SELECT PriceSell FROM Products WHERE ID={ID}".format(ID=id)
        else:
            query = "SELECT PriceBuy FROM Products WHERE ID={ID}".format(ID=id)

        cursor.execute(query)
        request = cursor.fetchall()
        cursor.close()

        return request[0][0]

    def addToListProduct(self, id, name, quantity, kind):
        price = self.getProductPrice(id, kind)
        order = []
        order.append(id)
        order.append(name)
        order.append(quantity)
        order.append(price)

        self.orderProduct.append(order)

    def calTotalOrder(self):
        subtotal = 0
        for pr in self.orderProduct:
            subtotal += round(int(pr[2]) * float(pr[3]), 2)
        
        subtotal = round(subtotal, 2)
        tax = round(subtotal * 0.1, 2)
        total = round(subtotal * 1.1, 2)

        return subtotal, tax, total
    
    def orderRequest(self):
        date = datetime.today().strftime('%Y%m%d%H%M%S')
        dateStr = str(datetime.today().strftime('%Y/%m/%d'))
        for pr in self.orderProduct:
            if self.mainFrameStatus == 2:
                self.product.createOrders(pr[0], date, pr[2])
            else:
                self.product.importProduct(pr[0], date, pr[2])

        if self.mainFrameStatus == 2:
            self.bill.printBill(self.orderProduct, dateStr)
        pass

    def getSumOfStatisData(self):
        sumSale = 0
        sumRemain = 0
        sumProfit = 0

        for row in self.statisData: 
            sumSale = sumSale + row[2]
            sumRemain = sumRemain + row[3]
            sumProfit = sumProfit + row[4]

        return sumSale, sumRemain, sumProfit

    def sortByType(self):
        self.statisData.clear()

        cursor = self.db.cursor()
        query = """SELECT Products.ID, ProductType.TypeName, Products.ProductName,
                    PriceBuy, PriceSell
                FROM ProductType JOIN Products
                ON ProductType.ID = Products.TypeID
                ORDER BY ProductType.TypeName, Products.ProductName;"""

        cursor.execute(query)
        typeInf = cursor.fetchall()

        query = """SELECT SUM(Quantity)
                    FROM ImportGoods
                    GROUP BY ProductID
                    ORDER BY ProductID;"""
        
        cursor.execute(query)
        remain = cursor.fetchall()

        query = """SELECT SUM(Quantity)
                    FROM Orders
                    GROUP BY ProductID
                    ORDER BY ProductID;"""
        cursor.execute(query)
        sale = cursor.fetchall()

        for idx in range(len(typeInf)):
            row = []
            row.append(typeInf[idx][1])
            row.append(typeInf[idx][2])
            productID = int(typeInf[idx][0]) - 1
            row.append(sale[productID][0])
            row.append(remain[productID][0] - sale[productID][0])
            
            profit = round((typeInf[idx][4] - typeInf[idx][3]) * sale[idx][0], 2)
            row.append(profit)
            self.statisData.append(row)

        cursor.close()
    
    def sortbyName(self):
        self.statisData.clear()

        cursor = self.db.cursor()
        query = """SELECT Products.ID, ProductType.TypeName, Products.ProductName,
                    PriceBuy, PriceSell
                FROM ProductType JOIN Products
                ON ProductType.ID = Products.TypeID
                ORDER BY Products.ProductName;"""

        cursor.execute(query)
        typeInf = cursor.fetchall()

        query = """SELECT SUM(Quantity)
                    FROM ImportGoods
                    GROUP BY ProductID
                    ORDER BY ProductID;"""
        
        cursor.execute(query)
        remain = cursor.fetchall()

        query = """SELECT SUM(Quantity)
                    FROM Orders
                    GROUP BY ProductID
                    ORDER BY ProductID;"""
        cursor.execute(query)
        sale = cursor.fetchall()

        for idx in range(len(typeInf)):
            row = []
            row.append(typeInf[idx][1])
            row.append(typeInf[idx][2])
            productID = int(typeInf[idx][0]) - 1
            row.append(sale[productID][0])
            row.append(remain[productID][0] - sale[productID][0])
            
            profit = round((typeInf[idx][4] - typeInf[idx][3]) * sale[idx][0], 2)
            row.append(profit)
            self.statisData.append(row)
        cursor.close()
    
    def sortBySale(self):
        self.statisData.clear()

        cursor = self.db.cursor()
        query = """SELECT ProductType.TypeName, Products.ProductName,
                    PriceBuy, PriceSell
                FROM ProductType JOIN Products
                ON ProductType.ID = Products.TypeID
                ORDER BY Products.ID;"""

        cursor.execute(query)
        typeInf = cursor.fetchall()

        query = """SELECT SUM(Quantity)
                    FROM ImportGoods
                    GROUP BY ProductID
                    ORDER BY ProductID;"""
        
        cursor.execute(query)
        remain = cursor.fetchall()

        query = """SELECT ProductID, SUM(Quantity)
                    FROM Orders
                    GROUP BY ProductID
                    ORDER BY SUM(Quantity) DESC;"""
        cursor.execute(query)
        sale = cursor.fetchall()

        for idx in range(len(sale)):
            row = []
            productID = int(sale[idx][0]) - 1
            row.append(typeInf[productID][0])
            row.append(typeInf[productID][1])
            row.append(sale[idx][1])
            row.append(remain[productID][0] - sale[idx][1])
            
            profit = round((typeInf[idx][3] - typeInf[idx][2]) * sale[idx][1], 2)
            row.append(profit)
            self.statisData.append(row)

        cursor.close()

    def sortByRemain(self):
        self.statisData.clear()

        cursor = self.db.cursor()
        query = """SELECT ProductType.TypeName, Products.ProductName,
                    PriceBuy, PriceSell
                FROM ProductType JOIN Products
                ON ProductType.ID = Products.TypeID
                ORDER BY Products.ID;"""

        cursor.execute(query)
        typeInf = cursor.fetchall()

        query = """SELECT ProductID, SUM(Quantity)
                    FROM ImportGoods
                    GROUP BY ProductID;"""
        
        cursor.execute(query)
        remain = cursor.fetchall()

        query = """SELECT ProductID, SUM(Quantity)
                    FROM Orders
                    GROUP BY ProductID;"""
        cursor.execute(query)
        sale = cursor.fetchall()

        remainAfter = []

        for idx in range(len(remain)):
            remainAfter.append([remain[idx][0], int(remain[idx][1] - sale[idx][1])])

        remainAfter = sorted(remainAfter,key=lambda x:x[1], reverse=True)

        for idx in range(len(remainAfter)):
            row = []
            productID = int(remainAfter[idx][0]) - 1
            row.append(typeInf[productID][0])
            row.append(typeInf[productID][1])
            row.append(sale[productID][1])
            row.append(remainAfter[idx][1])
            
            profit = round((typeInf[productID][3] - typeInf[productID][2]) * sale[productID][1], 2)
            row.append(profit)
            self.statisData.append(row)

        cursor.close()

    def sortByProfit(self):
        self.statisData.clear()

        cursor = self.db.cursor()
        query = """SELECT ProductType.TypeName, Products.ProductName,
                    PriceBuy, PriceSell
                FROM ProductType JOIN Products
                ON ProductType.ID = Products.TypeID
                ORDER BY Products.ID;"""

        cursor.execute(query)
        typeInf = cursor.fetchall()

        query = """SELECT ProductID, SUM(Quantity)
                    FROM ImportGoods
                    GROUP BY ProductID;"""
        
        cursor.execute(query)
        remain = cursor.fetchall()

        query = """SELECT ProductID, SUM(Quantity)
                    FROM Orders
                    GROUP BY ProductID;"""
        cursor.execute(query)
        sale = cursor.fetchall()

        profitLst = []

        for idx in range(len(sale)):
            pr = round((typeInf[idx][3] - typeInf[idx][2]) * sale[idx][1], 2)
            profitLst.append([sale[idx][0], pr])

        profitLst = sorted(profitLst,key=lambda x:x[1], reverse=True)

        for idx in range(len(profitLst)):
            row = []
            productID = int(profitLst[idx][0]) - 1
            row.append(typeInf[productID][0])
            row.append(typeInf[productID][1])
            row.append(sale[productID][1])
            row.append(remain[idx][1])
            row.append(profitLst[idx][1])
            self.statisData.append(row)

        cursor.close()

    def getProductIDfromName(self, name):
        cursor = self.db.cursor()

        query = "SELECT * FROM Products WHERE ProductName='{na}'".format(na=name)

        cursor.execute(query)
        request = cursor.fetchall()
        cursor.close()

        return request[0][0]
    
    def getEmloyeeList(self):
        cursor = self.db.cursor()

        query = "SELECT * FROM Employees"
        cursor.execute(query)
        request = cursor.fetchall()
        cursor.close()

        return request
    
    def getCustomerList(self):
        cursor = self.db.cursor()

        query = "SELECT * FROM Customers"
        cursor.execute(query)
        request = cursor.fetchall()
        cursor.close()

        return request
    
    def addEmployee(self, ID, name, sex, phone, address):
        cursor = self.db.cursor()

        query = """INSERT INTO Employees (ID, EmName, Sex, Phone, EmAddress)
                VALUES ('{}', '{}', '{}', '{}', '{}');""".format(ID, name, sex, phone, address)
        cursor.execute(query)
        self.db.commit()

        cursor.close()

    def deleteEmployee(self, ID):
        cursor = self.db.cursor()

        query = """DELETE FROM Employees WHERE ID={};""".format(ID)
        cursor.execute(query)
        self.db.commit()

        cursor.close()

    def addCustomer(self, ID, name, sex, phone, address, petName):
        cursor = self.db.cursor()

        query = """INSERT INTO Customers (ID, EmName, Sex, Phone, EmAddress)
                VALUES ('{}', '{}', '{}', '{}', '{}, {}');""".format(ID, name, sex, phone, address, petName)
        cursor.execute(query)
        self.db.commit()

        cursor.close()

    def deleteCustomer(self, ID):
        cursor = self.db.cursor()

        query = """DELETE FROM Customers WHERE ID={};""".format(ID)
        cursor.execute(query)
        self.db.commit()

        cursor.close()

    def showBills(self):
        cwd = os.getcwd()
        cwd = cwd + "/bills/"

        for path in os.scandir(cwd):
            if path.is_file():
                if path.name.split('.')[-1] == 'txt':
                    self.billList.append(path.name)

    def getBillName(self):
        return self.bill.billName

    # def __del__( self):
    #     self.mydb.close()

    # def requestTypeProduct():
