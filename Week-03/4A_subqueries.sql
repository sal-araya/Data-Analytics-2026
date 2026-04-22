USE northwind;
SELECT ProductName
FROM Products
WHERE UnitPrice = (
     SELECT MAX(UnitPrice) FROM Products
);

SELECT p.ProductName, c.CategoryName
FROM Products p
JOIN Categories c ON p. CategoryID = c. CategoryID
WHERE p. UnitPrice = (
    SELECT MIN(UnitPrice) FROM Products
);

SELECT OrderID, ShipName, ShipAddress
FROM Orders
WHERE ShipVia = (
    SELECT ShipperID
    FROM Shippers
    WHERE CompanyName = 'Federal Shipping' 
);

SELECT OrderID
FROM `Order Details`
WHERE ProductID = (
     SELECT ProductID
     FROM Products 
     WHERE ProductsName = 'Sasquatch Ale'
);

SELECT FirstName, LastName
FROM Employees
WHERE EmployeeID = (
     SELECT EmployeeID
     FROM Orders
     WHERE OrderID = 10266
);

SELECT CompanyName
FROM Customers
WHERE CustomerID = (
     SELECT CustomerID 
     FROM Orders 
     WHERE OrderID = 10266
);     