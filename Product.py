import mysql.connector

class Product():
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="0912752882ha",
            database="PetShop"
        )
        pass

    # def __del__( self):
    #     self.db.close()

    def importProduct(self, id, date, quantity):
        insert_query = """INSERT INTO ImportGoods (ProductID, DateImport, Quantity) 
            VALUES ('{ProductID}', '{DateImport}', '{Quantity}') ;
            """.format(ProductID=id, DateImport=date, Quantity=quantity)

        cursor = self.db.cursor()
        cursor.execute(insert_query)

        self.db.commit()

        cursor.execute("SELECT LAST_INSERT_ID() FROM ImportGoods;")
        importID = cursor.fetchall()

        cursor.close()
        return importID[0][0]

    def getAvailabelProduct(self, id):
        query_import = """SELECT ProductID, SUM(Quantity) FROM ImportGoods 
                    WHERE ProductID='{ProductID}'
                    GROUP BY ProductID""".format(ProductID=id)

        cursor = self.db.cursor()
        cursor.execute(query_import)

        result_import = cursor.fetchall()
        importProduct = int(result_import[0][1])

        query_export = """SELECT ProductID, SUM(Quantity) FROM Orders 
                WHERE ProductID='{ProductID}'
                GROUP BY ProductID""".format(ProductID=id)

        cursor.execute(query_export)

        result_export = cursor.fetchall()
        exportProduct = int(result_export[0][1])

        cursor.close()
        return (importProduct - exportProduct)

    def checkInventory(self, id, quantity):
        query_import = """SELECT ProductID, SUM(Quantity) FROM ImportGoods 
                    WHERE ProductID='{ProductID}'
                    GROUP BY ProductID""".format(ProductID=id)

        cursor = self.db.cursor()
        cursor.execute(query_import)

        result_import = cursor.fetchall()
        importProduct = result_import[0][1]

        query_export = """SELECT ProductID, SUM(Quantity) FROM Orders 
                WHERE ProductID='{ProductID}'
                GROUP BY ProductID""".format(ProductID=id)
        
        cursor.execute(query_export)

        result_export = cursor.fetchall()
        exportProduct = result_export[0][1]

        returnVal = True
        if ((importProduct - exportProduct) < quantity):
            returnVal = False

        cursor.close()
        return returnVal

    def createOrders(self, id, date, quantity):
        insert_query = """INSERT INTO Orders (ProductID, DateSale, Quantity) 
            VALUES ('{ProductID}', '{DateImport}', '{Quantity}') ;
            """.format(ProductID=id, DateImport=date, Quantity=quantity)

        cursor = self.db.cursor()
        cursor.execute(insert_query)

        self.db.commit()

        cursor.execute("SELECT LAST_INSERT_ID() FROM ImportGoods;")
        orderID = cursor.fetchall()

        cursor.close()
        return orderID[0][0]

    def closeService(self):
        self.db.close()