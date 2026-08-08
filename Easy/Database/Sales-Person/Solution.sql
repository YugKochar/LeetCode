# Write your MySQL query statement below
select name from Salesperson where sales_id not in 
(select Orders.sales_id from Orders 
join Company on Orders.com_id = Company.com_id where Company.name = 'Red');