## Hacker Rank Problems


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