USE northwind;
-- Question 1
SELECT ProductID, ProductName, UnitPrice
FROM products
ORDER BY UnitPrice ASC;

-- Question 2
SELECT ProductName, UnitInStock, UnitPrice
FROM Products 
WHERE UnitInStock >= 100
ORDER BY UnitPrice DESC;

-- Question 3
SELECT ProductName, UnitsInStock, UnitPrice 
FROM Products
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC, ProductName ASC;

-- Question 4
SELECT COUNT(DISTINCT CustomerID) AS CustomerCount
FROM Orders;

-- Question 5
SELECT ShipCountry, COUNT(DISTINCT CustomerID) AS CustomerCount
FROM Orders
GROUP BY ShipCountry
ORDER BY CustomerCount DESC;

-- Question 6
SELECT ProductName, UnitsInStock, UnitsOnOrder
FROM Products
WHERE UnitsInStock < 25 AND UnitsOnOrder >= 1
ORDER BY UnitsOnOrder DESC, ProductName ASC;

-- Question 7
SELECT Title, COUNT(*) AS EmployeeCount
FROM Employees
GROUP BY Title;

-- Question 8
SELECT FirstName, LastName, Title, Salary
FROM Employees
WHERE Salary BETWEEN 2000 AND 2500
ORDER BY Title; 

