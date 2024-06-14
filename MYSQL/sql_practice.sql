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

/* Students and Examinations
Table: Students

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| student_name  | varchar |
+---------------+---------+
student_id is the primary key (column with unique values) for this table.
Each row of this table contains the ID and the name of one student in the school.
 

Table: Subjects

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| subject_name | varchar |
+--------------+---------+
subject_name is the primary key (column with unique values) for this table.
Each row of this table contains the name of one subject in the school.
 

Table: Examinations

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| student_id   | int     |
| subject_name | varchar |
+--------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates.
Each student from the Students table takes every course from the Subjects table.
Each row of this table indicates that a student with ID student_id attended the exam of subject_name.
 

Write a solution to find the number of times each student attended each exam.

Return the result table ordered by student_id and subject_name
*/

SELECT 
    st.student_id,
    st.student_name,
    sub.subject_name,
    COUNT(e.subject_name) attended_exams
FROM
    (Students AS st
    CROSS JOIN Subjects AS sub)
        LEFT JOIN
    Examinations AS e ON (st.student_id = e.student_id)
        AND (sub.subject_name = e.subject_name)
GROUP BY st.student_id , st.student_name , sub.subject_name
ORDER BY st.student_id , st.student_name , sub.subject_name;
/*
Table: Users

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| user_name   | varchar |
+-------------+---------+
user_id is the primary key (column with unique values) for this table.
Each row of this table contains the name and the id of a user.
 

Table: Register

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| contest_id  | int     |
| user_id     | int     |
+-------------+---------+
(contest_id, user_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the id of a user and the contest they registered into.
 

Write a solution to find the percentage of the users registered in each contest rounded to two decimals.

Return the result table ordered by percentage in descending order. In case of a tie, order it by contest_id in ascending order.*/
with total_user as (
    select count(*) as users_no 
    from users
)
select contest_id,round((count(user_id)*100/users_no),2) as percentage
from Register,total_user
group by contest_id
order by percentage desc,contest_id;

/*
Table: Queries

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| query_name  | varchar |
| result      | varchar |
| position    | int     |
| rating      | int     |
+-------------+---------+
This table may have duplicate rows.
This table contains information collected from some queries on a database.
The position column has a value from 1 to 500.
The rating column has a value from 1 to 5. Query with rating less than 3 is a poor query.
 

We define query quality as:

The average of the ratio between query rating and its position.

We also define poor query percentage as:

The percentage of all queries with rating less than 3.

Write a solution to find each query_name, the quality and poor_query_percentage.

Both quality and poor_query_percentage should be rounded to 2 decimal places.

Return the result table in any order. */
SELECT 
    query_name,
    ROUND(AVG(rating / position), 2) AS quality,
    ROUND(SUM(CASE
                WHEN rating < 3 THEN 1
                ELSE 0
            END) * 100 / COUNT(*),
            2) AS poor_query_percentage
FROM
    queries
WHERE
    query_name IS NOT NULL
GROUP BY query_name;
## Final prep SQl 
show databases;
use newdb;
show tables;

/*
Table: Courses

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student     | varchar |
| class       | varchar |
+-------------+---------+
(student, class) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the name of a student and the class in which they are enrolled.
 

Write a solution to find all the classes that have at least five students.

Return the result table in any order.*/
SELECT 
    class
FROM
    courses
GROUP BY class
HAVING COUNT(student) >= 5;

/*
Table: Followers

+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| follower_id | int  |
+-------------+------+
(user_id, follower_id) is the primary key (combination of columns with unique values) for this table.
This table contains the IDs of a user and a follower in a social media app where the follower follows the user.
 

Write a solution that will, for each user, return the number of followers.

Return the result table ordered by user_id in ascending order. */
SELECT 
    user_id, COUNT(follower_id) AS followers_count
FROM
    followers
GROUP BY user_id
ORDER BY user_id;

/*
Table: MyNumbers

+-------------+------+
| Column Name | Type |
+-------------+------+
| num         | int  |
+-------------+------+
This table may contain duplicates (In other words, there is no primary key for this table in SQL).
Each row of this table contains an integer.
 

A single number is a number that appeared only once in the MyNumbers table.

Find the largest single number. If there is no single number, report null. */
select max(num) as num
from (
    select num
    from MyNumbers
    group by num
    having count(num) = 1
) count_num;
/*
Table: Delivery

+-----------------------------+---------+
| Column Name                 | Type    |
+-----------------------------+---------+
| delivery_id                 | int     |
| customer_id                 | int     |
| order_date                  | date    |
| customer_pref_delivery_date | date    |
+-----------------------------+---------+
delivery_id is the column of unique values of this table.
The table holds information about food delivery to customers that make orders at some date and specify a preferred delivery date (on the same order date or after it).
 

If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.

The first order of a customer is the order with the earliest order date that the customer made. It is guaranteed that a customer has precisely one first order.

Write a solution to find the percentage of immediate orders in the first orders of all customers, rounded to 2 decimal places.*/
SELECT 
    (ROUND(SUM(CASE
                WHEN order_date = customer_pref_delivery_date THEN 1
                ELSE 0
            END) / COUNT(*),
            4) * 100) AS immediate_percentage
FROM
    delivery
WHERE
    (customer_id , order_date) IN (SELECT 
            customer_id, MIN(order_date)
        FROM
            delivery
        GROUP BY customer_id);
/*
Amber's conglomerate corporation acquired new companies, each with a specific hierarchy.
You need to write a query to print the company_code, founder name, total number of lead managers, senior managers, managers, and employees, ordered by company_code. 
The company_code should be sorted lexicographically.
*/
SELECT 
    company.company_code,
    company.founder,
    COUNT(DISTINCT lead_manager.lead_manager_code),
    COUNT(DISTINCT senior_manager.senior_manager_code),
    COUNT(DISTINCT manager.manager_code),
    COUNT(DISTINCT employee.employee_code)
FROM
    company
        INNER JOIN
    lead_manager ON company.company_code = lead_manager.company_code
        INNER JOIN
    senior_manager ON lead_manager.company_code = senior_manager.company_code
        INNER JOIN
    manager ON senior_manager.company_code = manager.company_code
        INNER JOIN
    employee ON manager.company_code = employee.company_code
GROUP BY company.company_code , company.founder
ORDER BY company.company_code;
/*
Consider P1(a,b) and P2(c,d) to be two points on a 2D plane.
 a happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
 b happens to equal the minimum value in Western Longitude (LONG_W in STATION).
 c happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
 d happens to equal the maximum value in Western Longitude (LONG_W in STATION).
Query the Manhattan Distance between points  and  and round it to a scale of  decimal places.*/
SELECT 
    ABS(FORMAT(MAX(lat_n) - MIN(lat_n), 4)) + ABS(FORMAT(MAX(long_w) - MIN(long_w), 4))
FROM
    station;
/*
 given three tables: Students, Friends and Packages. Students contains two columns: ID and Name. 
 Friends contains two columns: ID and Friend_ID (ID of the ONLY best friend). 
 Packages contains two columns: ID and Salary (offered salary in $ thousands per month).
 Write a query to output the names of those students whose best friends got offered a higher salary than them. 
 Names must be ordered by the salary amount offered to the best friends. It is guaranteed that no two students got same salary offer.
*/
SELECT 
    s.name
FROM
    students s
        INNER JOIN
    friends f ON s.id = f.id
        INNER JOIN
    packages p1 ON f.friend_id = p1.id
        INNER JOIN
    packages p2 ON s.id = p2.id
WHERE
    p1.salary > p2.salary
ORDER BY p1.salary;
/*
Table: Employee

+---------------+---------+
| Column Name   |  Type   |
+---------------+---------+
| employee_id   | int     |
| department_id | int     |
| primary_flag  | varchar |
+---------------+---------+
(employee_id, department_id) is the primary key (combination of columns with unique values) for this table.
employee_id is the id of the employee.
department_id is the id of the department to which the employee belongs.
primary_flag is an ENUM (category) of type ('Y', 'N'). If the flag is 'Y', the department is the primary department for the employee. If the flag is 'N', the department is not the primary.
 

Employees can belong to multiple departments. When the employee joins other departments, they need to decide which department is their primary department. Note that when an employee belongs to only one department, their primary column is 'N'.

Write a solution to report all the employees with their primary department. For employees who belong to one department, report their only department.

Return the result table in any order.
*/

SELECT 
    employee_id, department_id
FROM
    employee
GROUP BY 1
HAVING COUNT(DISTINCT department_id) = 1 
UNION SELECT 
    employee_id, department_id
FROM
    employee
WHERE
    primary_flag = 'Y';

/*
Table: Employees

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| employee_id | int      |
| name        | varchar  |
| manager_id  | int      |
| salary      | int      |
+-------------+----------+
In SQL, employee_id is the primary key for this table.
This table contains information about the employees, their salary, and the ID of their manager. Some employees do not have a manager (manager_id is null). 
 

Find the IDs of the employees whose salary is strictly less than $30000 and whose manager left the company. When a manager leaves the company, their information is deleted from the Employees table, but the reports still have their manager_id set to the manager that left.

Return the result table ordered by employee_id.
*/
SELECT 
    employee_id
FROM
    employees
WHERE
    salary < 30000
        AND manager_id NOT IN (SELECT 
            employee_id
        FROM
            employees)
ORDER BY employee_id;
/*
Table: Triangle

+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
| y           | int  |
| z           | int  |
+-------------+------+
In SQL, (x, y, z) is the primary key column for this table.
Each row of this table contains the lengths of three line segments.
 

Report for every three line segments whether they can form a triangle.

Return the result table in any order.
*/
SELECT 
    x,
    y,
    z,
    CASE
        WHEN (x + y < z) OR (x + y = z) THEN 'No'
        WHEN (x + z < y) OR (x + z = y) THEN 'No'
        WHEN (y + z < x) OR (y + z = x) THEN 'No'
        ELSE 'Yes'
    END triangle
FROM
    Triangle;