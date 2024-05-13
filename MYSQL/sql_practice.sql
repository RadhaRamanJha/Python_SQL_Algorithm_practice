-- Aggregation
/*
Q1. Table: Cinema

+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| id             | int      |
| movie          | varchar  |
| description    | varchar  |
| rating         | float    |
+----------------+----------+
id is the primary key (column with unique values) for this table.
Each row contains information about the name of a movie, its genre, and its rating.
rating is a 2 decimal places float in the range [0, 10]
 

Write a solution to report the movies with an odd-numbered ID and a description that is not "boring".

Return the result table ordered by rating in descending order.
*/
SELECT 
    *
FROM
    cinema
WHERE
    (id % 2 != 0)
        AND (description != 'boring')
ORDER BY rating DESC;
/* Basic joins
Table: Activity

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| machine_id     | int     |
| process_id     | int     |
| activity_type  | enum    |
| timestamp      | float   |
+----------------+---------+
The table shows the user activities for a factory website.
(machine_id, process_id, activity_type) is the primary key (combination of columns with unique values) of this table.
machine_id is the ID of a machine.
process_id is the ID of a process running on the machine with ID machine_id.
activity_type is an ENUM (category) of type ('start', 'end').
timestamp is a float representing the current time in seconds.
'start' means the machine starts the process at the given timestamp and 'end' means the machine ends the process at the given timestamp.
The 'start' timestamp will always be before the 'end' timestamp for every (machine_id, process_id) pair.
 

There is a factory website that has several machines each running the same number of processes. Write a solution to find the average time each machine takes to complete a process.

The time to complete a process is the 'end' timestamp minus the 'start' timestamp. The average time is calculated by the total time to complete every process on the machine divided by the number of processes that were run.

The resulting table should have the machine_id along with the average time as processing_time, which should be rounded to 3 decimal places.

Return the result table in any order.*/
SELECT 
    a1.machine_id AS machine_id,
    ROUND(AVG(a2.timestamp - a1.timestamp), 3) AS processing_time
FROM
    Activity a1
        INNER JOIN
    Activity a2 ON (a1.machine_id = a2.machine_id)
        AND (a1.process_id = a2.process_id)
WHERE
    a1.activity_type = 'start'
        AND a2.activity_type = 'end'
GROUP BY a1.machine_id;
/*
Table: Sales

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
(sale_id, year) is the primary key (combination of columns with unique values) of this table.
product_id is a foreign key (reference column) to Product table.
Each row of this table shows a sale on the product product_id in a certain year.
Note that the price is per unit.
 

Table: Product

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
product_id is the primary key (column with unique values) of this table.
Each row of this table indicates the product name of each product.
 

Write a solution to select the product id, year, quantity, and price for the first year of every product sold.

Return the resulting table in any order.*/
SELECT 
    product_id,
    MIN(year) AS first_year,
    CASE
        WHEN year = MIN(year) THEN quantity
    END quantity,
    CASE
        WHEN year = MIN(year) THEN price
    END price
FROM
    Sales
GROUP BY product_id;
SELECT 
    product_id, year AS first_year, quantity, price
FROM
    Sales
WHERE
    (product_id , year) IN (SELECT 
            product_id, MIN(year)
        FROM
            Sales
        GROUP BY product_id);
/* Basic join 
Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| empId       | int     |
| name        | varchar |
| supervisor  | int     |
| salary      | int     |
+-------------+---------+
empId is the column with unique values for this table.
Each row of this table indicates the name and the ID of an employee in addition to their salary and the id of their manager.
 

Table: Bonus

+-------------+------+
| Column Name | Type |
+-------------+------+
| empId       | int  |
| bonus       | int  |
+-------------+------+
empId is the column of unique values for this table.
empId is a foreign key (reference column) to empId from the Employee table.
Each row of this table contains the id of an employee and their respective bonus.
 

Write a solution to report the name and bonus amount of each employee with a bonus less than 1000.

Return the result table in any order.
*/
SELECT 
    e.name, b.bonus
FROM
    employee e
        LEFT JOIN
    bonus b ON e.empId = b.empId
WHERE
    b.bonus < 1000 OR b.bonus IS NULL;
/*
Table: Teacher

+-------------+------+
| Column Name | Type |
+-------------+------+
| teacher_id  | int  |
| subject_id  | int  |
| dept_id     | int  |
+-------------+------+
(subject_id, dept_id) is the primary key (combinations of columns with unique values) of this table.
Each row in this table indicates that the teacher with teacher_id teaches the subject subject_id in the department dept_id.
 

Write a solution to calculate the number of unique subjects each teacher teaches in the university.

Return the result table in any order.
*/
SELECT 
    teacher_id, COUNT(DISTINCT subject_id) AS cnt
FROM
    teacher
GROUP BY teacher_id;

-- Aggregation with CTE to include all cases

/*
Table: Prices

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| start_date    | date    |
| end_date      | date    |
| price         | int     |
+---------------+---------+
(product_id, start_date, end_date) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the price of the product_id in the period from start_date to end_date.
For each product_id there will be no two overlapping periods. That means there will be no two intersecting periods for the same product_id.
 

Table: UnitsSold

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| purchase_date | date    |
| units         | int     |
+---------------+---------+
This table may contain duplicate rows.
Each row of this table indicates the date, units, and product_id of each product sold. 
 

Write a solution to find the average selling price for each product. average_price should be rounded to 2 decimal places.

Return the result table in any order.
*/

with pur as (
select a.product_id, round(sum(b.units*a.price)/sum(b.units),2) as average_price
from Prices a
inner join  UnitsSold b on
a.product_id = b.product_id
where b.purchase_date between a.start_date and a.end_date
group by a.product_id
)
select * from pur
union all
select a.product_id,0 as average_price
from Prices a
left join  UnitsSold b on
a.product_id = b.product_id
where a.product_id not in (select product_id from UnitsSold);
/* ################### Aggregate functions ##########################
1075. Project Employees I
Table: Project

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| project_id  | int     |
| employee_id | int     |
+-------------+---------+
(project_id, employee_id) is the primary key of this table.
employee_id is a foreign key to Employee table.
Each row of this table indicates that the employee with employee_id is working on the project with project_id.
 

Table: Employee

+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| employee_id      | int     |
| name             | varchar |
| experience_years | int     |
+------------------+---------+
employee_id is the primary key of this table. It's guaranteed that experience_years is not NULL.
Each row of this table contains information about one employee.
 

Write an SQL query that reports the average experience years of all the employees for each project, rounded to 2 digits.

Return the result table in any order.
*/
SELECT 
    p.project_id,
    ROUND(AVG(e.experience_years), 2) average_years
FROM
    project p
        INNER JOIN
    employee e ON p.employee_id = e.employee_id
GROUP BY p.project_id;

/* ############### Sorting and Grouping ############
1141. User Activity for the Past 30 Days I
Table: Activity

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| session_id    | int     |
| activity_date | date    |
| activity_type | enum    |
+---------------+---------+
This table may have duplicate rows.
The activity_type column is an ENUM (category) of type ('open_session', 'end_session', 'scroll_down', 'send_message').
The table shows the user activities for a social media website. 
Note that each session belongs to exactly one user.
 

Write a solution to find the daily active user count for a period of 30 days ending 2019-07-27 inclusively. A user was active on someday if they made at least one activity on that day.

Return the result table in any order.
*/
SELECT 
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM
    Activity
WHERE
    activity_date BETWEEN '2019-06-28' AND '2019-07-28'
GROUP BY activity_date;
/* ################ Basic Joins ###################################
Table: Weather

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the column with unique values for this table.
There are no different rows with the same recordDate.
This table contains information about the temperature on a certain day.
 

Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order.
*/
SELECT 
    w1.id AS id
FROM
    weather w1
        INNER JOIN
    weather w2 ON (DATEDIFF(w1.recordDate, w2.recordDate) = 1)
WHERE
    w1.temperature > w2.temperature;
    
/* Aggregate Functions :- 
Table: Transactions

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| country       | varchar |
| state         | enum    |
| amount        | int     |
| trans_date    | date    |
+---------------+---------+
id is the primary key of this table.
The table has information about incoming transactions.
The state column is an enum of type ["approved", "declined"].
 

Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

Return the result table in any order.
*/
SELECT 
    DATE_FORMAT(trans_date, '%Y-%m') AS month,
    country,
    COUNT(*) AS trans_count,
    SUM(IF(state = 'approved', 1, 0)) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(IF(state = 'approved', amount, 0)) AS approved_total_amount
FROM
    transactions
GROUP BY month , country;
    
/* 
Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.
 

Write a solution to find managers with at least five direct reports.

Return the result table in any order. */
SELECT 
    e1.name
FROM
    employee e1
        JOIN
    employee e2 ON e1.id = e2.managerId
GROUP BY e1.id
HAVING COUNT(e2.managerId) >= 5;

-- Advanced Select
/* Problem 1 :- Generate folowing result sets :- 
1. Query an alphabetically order list of names in occupation immediatlty followed by first letter of profession in parenticals
   e.g. An_Actor_Name (A), A_Doctor_Name (D)
2. Query the number of occurances of each occupation in Occupations. Sort the occurances in ascending order, output them in following format
   "There are a total of [occupation_count] [occupation]s" */
SELECT 
    CONCAT(name,
            '(',
            UPPER(LEFT(occupation, 1)),
            ')')
FROM
    occupations
ORDER BY name;
SELECT 
    CONCAT('There are a total of ',
            COUNT(occupation),
            ' ',
            LOWER(occupation),
            's.')
FROM
    occupations
GROUP BY occupation
ORDER BY COUNT(occupation) , occupation;
/* Problem 2 :- 
Consider P1 (a, c) and P2 (b, d) to be two points on a 2D plane where (a, b) are the respective minimum and maximum values 
of Northern Latitude (LAT_N) and (c, d) are the respective minimum and maximum values of Western Longitude (LONG_W) in STATION.
Query the Euclidean Distance between points P1 and P2 and format your answer to display 4 decimal digits.
The STATION table has following columns:
-----
STATION 
----
Field Туре
ID    NUMBER 
CITY  VARCHAR2(21)
STATE VARCHAR2(2)
LAT_N NUMBER
LONG_W NUMBER
*/
SELECT 
    FORMAT(SQRT(POW(MAX(LAT_N) - MIN(LAT_N), 2) + POW(MAX(LONG_W) - MIN(LONG_W), 2)),4)
FROM
    station;
/* Advannced Select
Table: Employees

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| employee_id | int      |
| name        | varchar  |
| reports_to  | int      |
| age         | int      |
+-------------+----------+
employee_id is the column with unique values for this table.
This table contains information about the employees and the id of the manager they report to. Some employees do not report to anyone (reports_to is null). 
 

For this problem, we will consider a manager an employee who has at least 1 other employee reporting to them.

Write a solution to report the ids and the names of all managers, the number of employees who report directly to them, and the average age of the reports rounded to the nearest integer.

Return the result table ordered by employee_id. */
SELECT 
    e1.employee_id,
    e1.name,
    COUNT(*) reports_count,
    ROUND(AVG(e2.age)) average_age
FROM
    Employees e1
        INNER JOIN
    Employees e2 ON e1.employee_id = e2.reports_to
GROUP BY e1.employee_id , e1.name
ORDER BY e1.employee_id;
/* Joins
Table: Signups

+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| user_id        | int      |
| time_stamp     | datetime |
+----------------+----------+
user_id is the column of unique values for this table.
Each row contains information about the signup time for the user with ID user_id.
 

Table: Confirmations

+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| user_id        | int      |
| time_stamp     | datetime |
| action         | ENUM     |
+----------------+----------+
(user_id, time_stamp) is the primary key (combination of columns with unique values) for this table.
user_id is a foreign key (reference column) to the Signups table.
action is an ENUM (category) of the type ('confirmed', 'timeout')
Each row of this table indicates that the user with ID user_id requested a confirmation message at time_stamp and that confirmation message was either confirmed ('confirmed') or expired without confirming ('timeout').
 

The confirmation rate of a user is the number of 'confirmed' messages divided by the total number of requested confirmation messages. The confirmation rate of a user that did not request any confirmation messages is 0. Round the confirmation rate to two decimal places.

Write a solution to find the confirmation rate of each user.

Return the result table in any order.
*/
SELECT 
    s.user_id,
    ROUND(SUM(CASE
                WHEN c.action = 'confirmed' THEN 1
                ELSE 0
            END) / COUNT(*),
            2) AS confirmation_rate
FROM
    Signups s
        LEFT JOIN
    Confirmations c ON s.user_id = c.user_id
GROUP BY s.user_id; 