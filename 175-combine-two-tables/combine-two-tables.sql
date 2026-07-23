# Write your MySQL query statement below
select firstname, lastname,city, state
from Person p
LEFT JOIN ADDRESS a
on p.personid = a.personid;