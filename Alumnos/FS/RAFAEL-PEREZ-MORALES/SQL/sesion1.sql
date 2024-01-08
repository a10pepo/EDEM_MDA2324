-- Ejercicio 1 --
SELECT title,
       rental_rate,
       replacement_cost,
       ROUND((replacement_cost / rental_rate), 2) AS new_column
FROM public.film;

-- Ejercicio 2 --

SELECT title,
       rental_rate,
       replacement_cost,
       ROUND(rental_rate / replacement_cost, 0) AS new_operation
FROM public.film;

-- Ejercicio 3 --

SELECT actor_id, first_name, last_name
FROM public.actor
WHERE last_name LIKE 'A%';

SELECT film_id, title
FROM public.film
WHERE rental_rate > 10;

SELECT COUNT(*) AS num_peliculas
FROM public.film
WHERE rental_rate BETWEEN 5 AND 10;

SELECT COUNT(*) AS num_peliculas
FROM public.film
WHERE rental_rate < 5 AND length < 100;

-- Ejercicio 4 --
SELECT title, rental_rate
FROM public.film
WHERE title IN ('Giant Troopers', 'Gilbert Pelican', 'Gilmore Boiled');

SELECT title, rating, length
FROM public.film
WHERE title = 'Ali Forever';

SELECT title
FROM public.film
WHERE rental_rate IS NULL;

-- Ejercicio 5 --
SELECT title, length
FROM public.film
ORDER BY length ASC;

SELECT title, length
FROM public.film
ORDER BY length ASC
LIMIT 5;

-- Ejercicio 6 --
SELECT
    rating,
    COUNT(*) AS numero_peliculas,
    AVG(rental_rate) AS precio_medio_alquiler,
    MIN(rental_rate) AS precio_minimo_alquiler,
    MAX(rental_rate) AS precio_maximo_alquiler,
    AVG(length) AS duracion_media
FROM
    public.film
GROUP BY
    rating;

-- Ejercicio 7 --
SELECT length, AVG(rental_rate) AS precio_medio_alquiler
FROM public.film
GROUP BY length
ORDER BY length;

SELECT replacement_cost, AVG(rental_rate) AS precio_medio_alquiler
FROM public.film
GROUP BY replacement_cost
ORDER BY replacement_cost;

SELECT rating, COUNT(*) AS numero_de_peliculas
FROM public.film
GROUP BY rating
HAVING COUNT(*) > 200;

SELECT rating, AVG(rental_rate) AS precio_medio_alquiler
FROM public.film
GROUP BY rating
HAVING AVG(rental_rate) > 3;

SELECT rating, AVG(length) AS duracion_media
FROM public.film
GROUP BY rating
HAVING AVG(length) > 115;