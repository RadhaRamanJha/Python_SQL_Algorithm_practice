/*
1. SQL Joins
Performance Improvement
Raw Problem
You are given a table having the marks of one student in every test (Tests are held every day).
 You have to output the tests in which the student has improved his performance. For a student to improve his performance he has to score more than the previous test. 
 Given that TestIDs are in increasing order, forming a continuous sequence without any missing numbers.
Table: Tests
NOTE: The output should contain one column by the name ‘TestId’.
*/
SELECT 
    t1.testid
FROM
    Tests t1
        INNER JOIN
    Tests t2
WHERE
    (t1.testid = t2.testid + 1)
        AND (t1.marks > t2.marks);
/*
2. SQL Subqueries :- 
Study Selection

Given a table STUDY, query for all the attributes, which have marks greater than 80.
*/
SELECT 
    sub.ID, sub.Name, sub.Age, sub.Marks
FROM
    (SELECT 
        *
    FROM
        STUDY
    WHERE
        marks > 80) AS sub;
/*
2. SQL Subqueries :- 
Study Update
Given a table STUDY, update the marks of all the students to 50, whose marks lie in the range 25 - 50 (excluding 25 , including 50 i.e. (25,50] ). 
Then print the new table.
*/
SELECT 
    sub.id, sub.name, sub.age, sub.marks
FROM
    (SELECT 
        id,
            name,
            age,
            CASE
                WHEN (marks > 25 AND marks < 51) THEN 50
                ELSE marks
            END marks
    FROM
        STUDY) AS sub;
/*
3. Basic Select
Town Queries
Given a table Towns, query for all the Towns which have a Population greater than 1000.
*/
SELECT 
    *
FROM
    Towns
WHERE
    Population > 1000;
/*
3. Basic Select
Student Query
Given a table STUDENT, query for all the Names with Class 1 and SubjectCount greater than 3.
*/
SELECT 
    name
FROM
    STUDENT
WHERE
    class = 1 AND SubjectCount > 3;
/*
4. Aggregation
5'th Highest Marks
Given the ‘STUDENTS’ table. Write an SQL query to find the 5’th highest marks in the students table.
*/
SELECT 
    marks
FROM
    STUDENTS
ORDER BY marks DESC
LIMIT 1 OFFSET 4;
/*
5. Advanced Select
Role Player
Given a table GAMERS, query for a list sorted by alphabetical order of all the Players in the table, 
followed by the First letter of the Role each player plays in the game enclosed in braces (). Example: Ram(H)
*/
SELECT 
    CONCAT(player, '(', LEFT(Role, 1), ')') AS 'N'
FROM
    GAMERS
ORDER BY Player;
/*
5. Basic Join
Engineers Joined
Given 2 tables ENGINEER and DATA, query the sum of Count of all the engineers whose Type is FrontEnd.

Note: The column ID is the same in both the tables.
*/
SELECT 
    A
FROM
    (SELECT 
        d.type, SUM(e.Count) AS A
    FROM
        ENGINEER e
    INNER JOIN DATA d ON e.ID = d.ID
    GROUP BY d.type
    HAVING d.type = 'FrontEnd') AS sbuq;
 -- 27/06/2024   
/*
Given 2 tables ENGINEER and DATA, query for the total count of each Type in the ENGINEER table. 
Print the result in alphabetical order of the Type.

Note: The ID columns in both tables are identical.
*/

SELECT 
    sub.Count AS A
FROM
    (SELECT 
        d.type, SUM(e.Count) AS Count
    FROM
        DATA d
    INNER JOIN ENGINEER e ON d.id = e.id
    GROUP BY d.type
    ORDER BY d.type) AS sub;

/*
SELECT avgerage of people saved by FIREFIGHTERS where countrycode = 'PM';
*/

SELECT 
    AVG(PeopleSaved)
FROM
    FIREFIGHTERS
WHERE
    countrycode = 'PM';
/*
Write a SQL Query to find the name of all reviewers who have rated their ratings with a NULL value.
*/
SELECT 
    rev.reviewer_name
FROM
    reviewers rev
        INNER JOIN
    ratings rat ON rev.reviewer_id = rat.reviewer_id
WHERE
    rat.reviewer_stars IS NULL;
