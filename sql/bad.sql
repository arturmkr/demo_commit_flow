SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
INNER JOIN Customers O Orders.CustomerID = Customers.CustomerID;