# Write your MySQL query statement below
select p.firstname, p.lastname,a.city, a.state
from Person p
LEFT JOIN ADDRESS a
on p.personid = a.personid;