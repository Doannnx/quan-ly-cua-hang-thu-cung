SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

DROP TABLE IF EXISTS PetShop.ImportGoods;
DROP TABLE IF EXISTS PetShop.Orders;
DROP TABLE IF EXISTS PetShop.Products;
DROP TABLE IF EXISTS PetShop.ProductType;
DROP TABLE IF EXISTS PetShop.Employees;
DROP TABLE IF EXISTS PetShop.Customers;

SET NAMES utf8mb4 COLLATE utf8mb4_unicode_ci;

DROP DATABASE IF EXISTS PetShop;

CREATE DATABASE IF NOT EXISTS PetShop DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER DATABASE PetShop CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS PetShop.ImportGoods
(
	ID 		        INT NOT NULL AUTO_INCREMENT,
    ProductID       INT,
	DateImport     	DATE,
	Quantity        INT,
	PRIMARY KEY (ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO PetShop.ImportGoods (ProductID, DateImport, Quantity) VALUES ('1', '2024-07-04', '99');
INSERT INTO PetShop.ImportGoods (ProductID, DateImport, Quantity) VALUES ('2', '2024-07-04', '86');
INSERT INTO PetShop.ImportGoods (ProductID, DateImport, Quantity) VALUES ('3', '2024-07-04', '55');
INSERT INTO PetShop.ImportGoods (ProductID, DateImport, Quantity) VALUES ('4', '2024-07-04', '51');
INSERT INTO PetShop.ImportGoods (ProductID, DateImport, Quantity) VALUES ('5', '2024-07-04', '88');
INSERT INTO PetShop.ImportGoods (ProductID, DateImport, Quantity) VALUES ('6', '2024-07-04', '50');
INSERT INTO PetShop.ImportGoods (ProductID, DateImport, Quantity) VALUES ('7', '2024-07-04', '57');
INSERT INTO PetShop.ImportGoods (ProductID, DateImport, Quantity) VALUES ('8', '2024-07-04', '96');
INSERT INTO PetShop.ImportGoods (ProductID, DateImport, Quantity) VALUES ('9', '2024-07-04', '92');
INSERT INTO PetShop.ImportGoods (ProductID, DateImport, Quantity) VALUES ('10', '2024-07-04', '100');
INSERT INTO PetShop.ImportGoods (ProductID, DateImport, Quantity) VALUES ('11', '2024-07-04', '58');
INSERT INTO PetShop.ImportGoods (ProductID, DateImport, Quantity) VALUES ('12', '2024-07-04', '61');
INSERT INTO PetShop.ImportGoods (ProductID, DateImport, Quantity) VALUES ('13', '2024-07-04', '85');
INSERT INTO PetShop.ImportGoods (ProductID, DateImport, Quantity) VALUES ('14', '2024-07-04', '73');
INSERT INTO PetShop.ImportGoods (ProductID, DateImport, Quantity) VALUES ('15', '2024-07-04', '70');
INSERT INTO PetShop.ImportGoods (ProductID, DateImport, Quantity) VALUES ('16', '2024-07-04', '62');
INSERT INTO PetShop.ImportGoods (ProductID, DateImport, Quantity) VALUES ('17', '2024-07-04', '57');
INSERT INTO PetShop.ImportGoods (ProductID, DateImport, Quantity) VALUES ('18', '2024-07-04', '74');
INSERT INTO PetShop.ImportGoods (ProductID, DateImport, Quantity) VALUES ('19', '2024-07-04', '0');
INSERT INTO PetShop.ImportGoods (ProductID, DateImport, Quantity) VALUES ('20', '2024-07-04', '0');

CREATE TABLE IF NOT EXISTS PetShop.Orders
(
	ID 		        INT NOT NULL AUTO_INCREMENT,
    ProductID       INT,
	DateSale     	DATE,
	Quantity        INT,
	PRIMARY KEY (ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO PetShop.Orders (ProductID, DateSale, Quantity) VALUES ('1', '2024-07-06', '16');
INSERT INTO PetShop.Orders (ProductID, DateSale, Quantity) VALUES ('2', '2024-07-06', '32');
INSERT INTO PetShop.Orders (ProductID, DateSale, Quantity) VALUES ('3', '2024-07-06', '30');
INSERT INTO PetShop.Orders (ProductID, DateSale, Quantity) VALUES ('4', '2024-07-06', '18');
INSERT INTO PetShop.Orders (ProductID, DateSale, Quantity) VALUES ('5', '2024-07-06', '20');
INSERT INTO PetShop.Orders (ProductID, DateSale, Quantity) VALUES ('6', '2024-07-06', '39');
INSERT INTO PetShop.Orders (ProductID, DateSale, Quantity) VALUES ('7', '2024-07-06', '30');
INSERT INTO PetShop.Orders (ProductID, DateSale, Quantity) VALUES ('8', '2024-07-06', '40');
INSERT INTO PetShop.Orders (ProductID, DateSale, Quantity) VALUES ('9', '2024-07-06', '29');
INSERT INTO PetShop.Orders (ProductID, DateSale, Quantity) VALUES ('10', '2024-07-06', '18');
INSERT INTO PetShop.Orders (ProductID, DateSale, Quantity) VALUES ('11', '2024-07-06', '33');
INSERT INTO PetShop.Orders (ProductID, DateSale, Quantity) VALUES ('12', '2024-07-06', '34');
INSERT INTO PetShop.Orders (ProductID, DateSale, Quantity) VALUES ('13', '2024-07-06', '11');
INSERT INTO PetShop.Orders (ProductID, DateSale, Quantity) VALUES ('14', '2024-07-06', '14');
INSERT INTO PetShop.Orders (ProductID, DateSale, Quantity) VALUES ('15', '2024-07-06', '20');
INSERT INTO PetShop.Orders (ProductID, DateSale, Quantity) VALUES ('16', '2024-07-06', '42');
INSERT INTO PetShop.Orders (ProductID, DateSale, Quantity) VALUES ('17', '2024-07-06', '44');
INSERT INTO PetShop.Orders (ProductID, DateSale, Quantity) VALUES ('18', '2024-07-06', '35');
INSERT INTO PetShop.Orders (ProductID, DateSale, Quantity) VALUES ('19', '2024-07-06', '0');
INSERT INTO PetShop.Orders (ProductID, DateSale, Quantity) VALUES ('20', '2024-07-06', '0');

CREATE TABLE IF NOT EXISTS PetShop.Products
(
    ID 		        INT NOT NULL AUTO_INCREMENT,
	ProductName 	VARCHAR(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
	TypeID			INT NOT NULL,
	PriceBuy		DECIMAL(6, 2),
	PriceSell		DECIMAL(6, 2),
	PRIMARY KEY (ID)
) ENGINE=InnoDB CHARACTER SET utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ALTER TABLE PetShop.Products CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- ALTER TABLE PetShop.Products MODIFY ProductName VARCHAR(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

INSERT INTO PetShop.Products (ProductName, TypeID, PriceBuy, PriceSell) VALUES (N'Hat', '1', '6.83', '9.34');
INSERT INTO PetShop.Products (ProductName, TypeID, PriceBuy, PriceSell) VALUES (N'Pate', '1', '4.98', '10.91');
INSERT INTO PetShop.Products (ProductName, TypeID, PriceBuy, PriceSell) VALUES (N'Sup thuong', '1', '3.86', '6.76');
INSERT INTO PetShop.Products (ProductName, TypeID, PriceBuy, PriceSell) VALUES (N'Sua', '1', '9.56', '18.76');
INSERT INTO PetShop.Products (ProductName, TypeID, PriceBuy, PriceSell) VALUES (N'Banh thuong', '1', '9.68', '23.3');
INSERT INTO PetShop.Products (ProductName, TypeID, PriceBuy, PriceSell) VALUES (N'Co meo', '1', '3.37', '6.87');
INSERT INTO PetShop.Products (ProductName, TypeID, PriceBuy, PriceSell) VALUES (N'Binh nuoc', '2', '8.44', '14.46');
INSERT INTO PetShop.Products (ProductName, TypeID, PriceBuy, PriceSell) VALUES ('Bat an', '2', '2.51', '5.36');
INSERT INTO PetShop.Products (ProductName, TypeID, PriceBuy, PriceSell) VALUES ('Luoc chai', '2', '5.8', '8.51');
INSERT INTO PetShop.Products (ProductName, TypeID, PriceBuy, PriceSell) VALUES ('Do choi', '2', '9.18', '22.13');
INSERT INTO PetShop.Products (ProductName, TypeID, PriceBuy, PriceSell) VALUES ('Vong co', '2', '3.21', '4.3');
INSERT INTO PetShop.Products (ProductName, TypeID, PriceBuy, PriceSell) VALUES ('Day dat', '2', '9.75', '19.37');
INSERT INTO PetShop.Products (ProductName, TypeID, PriceBuy, PriceSell) VALUES ('Balo', '2', '9.33', '13.96');
INSERT INTO PetShop.Products (ProductName, TypeID, PriceBuy, PriceSell) VALUES ('Cat ve sinh', '3', '4.21', '8.85');
INSERT INTO PetShop.Products (ProductName, TypeID, PriceBuy, PriceSell) VALUES ('Sua tam', '3', '6.6', '12.17');
INSERT INTO PetShop.Products (ProductName, TypeID, PriceBuy, PriceSell) VALUES ('Khay ve sinh', '3', '6.39', '12.59');
INSERT INTO PetShop.Products (ProductName, TypeID, PriceBuy, PriceSell) VALUES ('Thuoc thu y', '4', '3.9', '8.23');
INSERT INTO PetShop.Products (ProductName, TypeID, PriceBuy, PriceSell) VALUES ('Thuc pham chuc nang', '4', '5.54', '10.58');
INSERT INTO PetShop.Products (ProductName, TypeID, PriceBuy, PriceSell) VALUES ('Ve sinh', '5', '5', '7.58');
INSERT INTO PetShop.Products (ProductName, TypeID, PriceBuy, PriceSell) VALUES ('Cat tia long', '5', '10.5', '11.58');

CREATE TABLE IF NOT EXISTS PetShop.ProductType
(
    ID 		        INT NOT NULL AUTO_INCREMENT,
	TypeName 		VARCHAR(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
	PRIMARY KEY (ID)
) ENGINE=InnoDB CHARACTER SET utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO PetShop.ProductType (TypeName) VALUES ('Thuc an');
INSERT INTO PetShop.ProductType (TypeName) VALUES ('Do dung');
INSERT INTO PetShop.ProductType (TypeName) VALUES ('Cham soc');
INSERT INTO PetShop.ProductType (TypeName) VALUES ('Thuoc');
INSERT INTO PetShop.ProductType (TypeName) VALUES ('Dich vu');

CREATE TABLE IF NOT EXISTS PetShop.Employees
(
    ID 		        VARCHAR(3) NOT NULL,
	EmName	 		VARCHAR(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
	Sex		 		VARCHAR(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
	Phone	 		VARCHAR(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
	EmAddress	 	VARCHAR(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
	PRIMARY KEY (ID)
) ENGINE=InnoDB CHARACTER SET utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO PetShop.Employees (ID, EmName, Sex, Phone, EmAddress) VALUES ('001', 'Nga Ngo', 'Female', '0338473343', '2 Pham Van Dong');
INSERT INTO PetShop.Employees (ID, EmName, Sex, Phone, EmAddress) VALUES ('002', 'Tuan', 'Male', '0338438541', '10 Cau Giay');
INSERT INTO PetShop.Employees (ID, EmName, Sex, Phone, EmAddress) VALUES ('003', 'Dong', 'Male', '0338883344', '99A Hang Buom');
INSERT INTO PetShop.Employees (ID, EmName, Sex, Phone, EmAddress) VALUES ('004', 'Linh', 'Female', '0338009943', '1 Giai Phong');

CREATE TABLE IF NOT EXISTS PetShop.Customers
(
    ID 		        VARCHAR(3) NOT NULL,
	EmName	 		VARCHAR(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
	Sex		 		VARCHAR(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
	Phone	 		VARCHAR(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
	EmAddress	 	VARCHAR(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
	petName			VARCHAR(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
	PRIMARY KEY (ID)
) ENGINE=InnoDB CHARACTER SET utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO PetShop.Customers (ID, EmName, Sex, Phone, EmAddress, petName) VALUES ('001', 'Nau', 'Female', '0338473343', '67 Nguyen Thien Thuat', 'Alex');
INSERT INTO PetShop.Customers (ID, EmName, Sex, Phone, EmAddress, petName) VALUES ('002', 'My Dieu', 'Female', '0338438541', '47 Hai Ba Trung', 'Elizabeth');
INSERT INTO PetShop.Customers (ID, EmName, Sex, Phone, EmAddress, petName) VALUES ('003', 'Dau', 'Male', '0338883344', '99 Trieu Viet Vuong', 'Tom');
INSERT INTO PetShop.Customers (ID, EmName, Sex, Phone, EmAddress, petName) VALUES ('004', 'My Lem', 'Female', '0338009943', '1 Thai Ha', 'Jerry');

