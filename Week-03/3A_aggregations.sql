USE northwind;
Select MIN(UnitPrice) AS CheapestPrice
FROM Products;

SELECT ProductName 
FROM Products
WHERE UnitPrice = (
	SELECT  MIN(UnitPrice) FROM Products
);

SELECT AVG(UnitPrice) AS AveragePrice
FROM Products;
SELECT ROUND(AVG(UnitPrice), 2) AS AveragePrice
FROM Products;

SELECT MAX(UnitPrice) AS MaxPrice
FROM Products;

SELECT p.ProductName, s.CompanyName AS SupplierName
FROM Products p
JOIN Suppliers s ON p.SupplierID = s.SupplierID
WHERE p.UnitPrice = (
    SELECT MAX(UnitPrice) FROM Products
);

SELECT SUM(Salary) AS TotalPayroll
FROM Employees;

SELECT 
    MAX(Salary) AS HighestSalary,
    MIN(Salary) AS LowestSalary
FROM Employees;

SELECT s.SupplierID, s.CompanyName, COUNT(p.ProductID) AS NumberOfProducts
FROM Suppliers s
JOIN Products p ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID, s.CompanyName;

SELECT c.CategoryName, AVG(p.UnitPrice) AS AvgPrice
FROM Categories c
JOIN Products p ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryName;

SELECT s.CompanyName, COUNT(p.ProductID) AS NumberOfItems
FROM Suppliers s
JOIN Products p ON s.SupplierID = p.SupplierID
GROUP BY s.CompanyName
HAVING COUNT(p.ProductID) >= 5;

SELECT 
    ProductID,
    ProductName,
    UnitPrice * UnitsInStock AS InventoryValue
FROM Products
WHERE UnitsInStock > 0
ORDER BY InventoryValue DESC, ProductName;