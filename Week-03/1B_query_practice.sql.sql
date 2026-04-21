USE northwind;
SELECT * FROM products;
SELECT ProductID, ProductName, UnitPrice
FROM products;

SELECT *
FROM products
WHERE UnitPrice <= 7.50;

SELECT *
FROM products
WHERE UnitsInStock = 0
AND UnitsOnOrder > 0;

SELECT * FROM categories;

SELECT p.ProductName, c.CategoryName 
FROM products p
JOIN categories c
ON p.CategoryID = c.CategoryID
WHERE c.CategoryName = 'Seafood';

SELECT *
FROM suppliers
WHERE CompanyName = 'Tokyo Traders';

SELECT *
FROM products
WHERE SupplierID = 4;

SELECT COUNT(*) AS TotalEmployees
FROM employees;
SELECT *
FROM employees
WHERE Title LIKE '%Manager%';