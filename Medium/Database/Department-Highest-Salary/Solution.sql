# Write your MySQL query statement below
select Department.name as Department, Employee.name as Employee, Employee.salary as Salary from Employee
inner join Department on Employee.departmentID = Department.id where Employee.salary = (select max(salary) from Employee where Department.Id = Employee.departmentId);