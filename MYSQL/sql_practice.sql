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
