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

/*
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