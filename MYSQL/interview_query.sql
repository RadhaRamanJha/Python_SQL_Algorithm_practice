# Databases Description
show databases;
use sakila;
show tables;

# 1. Query for all actors of film which has it's title starting with A and Ending with R

# Tables to use
desc film;
desc film_actor;
desc actor;

# Prelimnary Query 
SELECT 
    f.title, a.first_name
FROM
    film f
        INNER JOIN
    film_actor fa ON f.film_id = fa.film_id
        INNER JOIN
    actor a ON fa.actor_id = a.actor_id
ORDER BY f.title;

# Modified Query - All Films and first name of all actors in them
SELECT 
    f.title,
    GROUP_CONCAT(a.first_name
        ORDER BY (a.first_name)
        SEPARATOR ', ') AS actors
FROM
    film f
        INNER JOIN
    film_actor fa ON f.film_id = fa.film_id
        INNER JOIN
    actor a ON fa.actor_id = a.actor_id
GROUP BY f.title
ORDER BY f.title;

# The Pre-Final Query -- Films with title starting with ' A ' and ending with ' R '
SELECT 
    f.title,
    GROUP_CONCAT(a.first_name
        ORDER BY (a.first_name)
        SEPARATOR ', ') AS actors
FROM
    film f
        INNER JOIN
    film_actor fa ON f.film_id = fa.film_id
        INNER JOIN
    actor a ON fa.actor_id = a.actor_id
GROUP BY f.title
having f.title regexp '^A.*R$'
ORDER BY f.title;

# Final Query with subquery 

-- Subqery to use 
SELECT 
        a.actor_id, 
            CONCAT(a.first_name,' ', a.last_name) AS actor_name
    FROM
        actor a;

# Final Query Using subquery -- using having clause to filter the film title
SELECT 
    f.title,
    GROUP_CONCAT(sub.actor_name
        ORDER BY sub.actor_name
        SEPARATOR ', ') actors
FROM
    film f
        INNER JOIN
    film_actor fa ON f.film_id = fa.film_id
        INNER JOIN
    (SELECT 
        a.actor_id,
            CONCAT(a.first_name, ' ', a.last_name) AS actor_name
    FROM
        actor a) as sub  ON fa.actor_id = sub.actor_id
# where f.title REGEXP '^A.*R$'
# where f.title like 'A%R'
GROUP BY f.title
having f.title REGEXP '^A.*R$'
ORDER BY f.title;

# 2. Query for all actors of film having more than 11 actors in it
# Final Query Using CTE 
with cte as (
SELECT 
        a.actor_id,
            CONCAT(a.first_name, ' ', a.last_name) AS actor_name
    FROM
        actor a
)
SELECT 
    f.title, count(*) total_actors,
    GROUP_CONCAT(cte.actor_name
        ORDER BY cte.actor_name
        SEPARATOR ', ') AS actors
FROM
    film f
        INNER JOIN
    film_actor fa ON f.film_id = fa.film_id
        INNER JOIN
     cte ON fa.actor_id = cte.actor_id
GROUP BY f.title
having total_actors > 11
ORDER BY total_actors desc;