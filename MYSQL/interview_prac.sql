# Databases Description
show databases;
use sakila;
show tables;

# 1. Query for all actors of film which has it's title starting with A and Ending with R

# Tables to use
desc film;
desc film_actor;
desc actor;

# Prelimnary Query - All Films and first name of all actors in them
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
        actor a) sub ON fa.actor_id = sub.actor_id
GROUP BY f.title
having
    f.title REGEXP '^A.*R$'
ORDER BY f.title;

# Final Query Using CTE -- using where clause to filter the film title
with sub as (
SELECT 
        a.actor_id,
            CONCAT(a.first_name, ' ', a.last_name) AS actor_name
    FROM
        actor a

)
SELECT 
    f.title,
    GROUP_CONCAT(sub.actor_name
        ORDER BY sub.actor_name
        SEPARATOR ', ') AS actors
FROM
    film f
        INNER JOIN
    film_actor fa ON f.film_id = fa.film_id
        INNER JOIN
     sub ON fa.actor_id = sub.actor_id
WHERE
    title REGEXP '^A.*R$'
GROUP BY f.title
ORDER BY f.title;

# 2. Query to know the tile of all films which has earnings more than 200 units

# Tables to use
desc film;
desc payment;
desc rental;
desc inventory;

# Final Query 
SELECT 
    f.title, SUM(p.amount) earnings
FROM
    film f
        INNER JOIN
    inventory i ON f.film_id = i.film_id
        INNER JOIN
    rental r ON i.inventory_id = r.inventory_id
        INNER JOIN
    payment p ON r.rental_id = p.rental_id
GROUP BY f.title
HAVING SUM(p.amount) > 200
ORDER BY SUM(p.amount) DESC;