--SESION 1
SELECT TITLE,
RENTAL_RATE,
REPLACEMENT_COST,
ROUND((rental_rate/replacement_cost * 100), 2) AS PORCENTAJE
FROM film f
ORDER BY PORCENTAJE DESC
;

SELECT TITLE,
RENTAL_RATE,
REPLACEMENT_COST,
CEIL(replacement_cost/rental_rate) AS NUM_DISCOS
FROM film f;

SELECT 
COUNT(TITLE) AS PELICULAS_DISPONIBLES,
AVG(rental_rate) AS PRECIO_MEDIO_ALQUILER
FROM film f 
;

SELECT 
TITLE AS PELICULAS_MAS_CARAS, rental_rate AS PRECIO
FROM film
WHERE RENTAL_RATE = (SELECT MAX(rental_rate) FROM film) 
;

SELECT 
TITLE AS PELICULAS_MAS_BARATAS, rental_rate AS PRECIO
FROM film
WHERE RENTAL_RATE = (SELECT min(rental_rate) FROM film) 
;

SELECT DISTINCT rental_rate AS PRECIOS, COUNT(*) AS UNIDADES
FROM film
GROUP BY rental_rate ;

SELECT MIN(replacement_cost) AS COSTE_MINIMO_REEMPLAZO,
MAX(replacement_cost) AS COSTE_MAXIMO_REEMPLAZO
FROM FILM;

SELECT first_name AS nombres_por_a,
last_name AS apellido
FROM actor
WHERE first_name LIKE 'A%';

SELECT title, rental_rate
FROM film
WHERE rental_rate > 10;

SELECT count(*)
FROM film
WHERE rental_rate BETWEEN 5 AND 10;

SELECT count(*)
FROM film
WHERE rental_rate < 5 AND length < 100;

SELECT TITLE, RENTAL_RATE
FROM film f 
WHERE TITLE IN ('Giant Troopers', 'Gilbert Pelican', 'Gilmore Boiled');

SELECT * FROM FILM;

SELECT title, rating, length AS duracion
FROM FILM
WHERE title = 'Ali Forever';

SELECT count(*)
FROM film f 
WHERE rental_rate IS NULL;

SELECT TITLE,
length
FROM film f
ORDER BY length ASC
;

SELECT TITLE AS PELICULAS_MAS_CORTAS
FROM film f
ORDER BY length ASC
LIMIT 5
;


--SESION 2
SELECT * FROM FILM;
SELECT AVG(RENTAL_RATE)
FROM film f WHERE rating = 'PG';

SELECT RATING, COUNT(*) FROM FILM
GROUP BY rating 
HAVING COUNT(*) > 200;

SELECT RATING, AVG(rental_rate)
FROM FILM
GROUP BY RATING
HAVING AVG(RENTAL_RATE) > 3;

SELECT RATING, AVG(LENGTH)
FROM film f 
GROUP BY RATING
HAVING AVG(LENGTH) > 115;


SELECT * FROM FILM;
SELECT * FROM ACTOR;
SELECT * FROM film_actor fa ;
SELECT * FROM STORE;

SELECT f.title, count(first_name)
FROM FILM F
INNER JOIN film_actor fa 
ON F.film_id = FA.film_id
INNER JOIN actor a 
ON FA.actor_id = A.ACTOR_ID
GROUP BY f.title
;

SELECT A.address_id, A.address 
FROM address a 
INNER JOIN CUSTOMER c
ON A.address_id = C.address_id
ORDER BY A.address_id ASC ;

SELECT c.first_name , A.address, city.city_id 
FROM address a 
INNER JOIN CUSTOMER c
ON A.address_id = C.address_id
INNER JOIN CITY
ON A.city_id = city.city_id 
ORDER BY A.address_id ASC;

SELECT c.first_name , A.address, city.city_id , c2.country 
FROM address a 
INNER JOIN CUSTOMER c
ON A.address_id = C.address_id
INNER JOIN CITY
ON A.city_id = city.city_id 
INNER JOIN country c2 
ON city.country_id = c2.country_id 
ORDER BY A.address_id ASC;


SELECT COUNT(*) FROM (
SELECT F.title
FROM film f
INNER JOIN film_actor fa 
ON F.film_id = FA.film_id 
INNER JOIN ACTOR a
ON FA.actor_id = A.actor_id 
WHERE A.last_name LIKE 'C%'
GROUP BY F.title 
) AS PELICULAS
;

SELECT F.title, COUNT(FA.actor_id) 
FROM FILM F
INNER JOIN film_actor fa 
ON F.film_id = FA.film_id
INNER JOIN actor a 
ON FA.actor_id = A.ACTOR_ID
GROUP BY f.title
ORDER BY COUNT(FA.actor_id) DESC
;

SELECT F.title, COUNT(*) AS NUM_ACTORES
FROM FILM F
INNER JOIN film_actor fa 
ON F.film_id = FA.film_id
INNER JOIN actor a 
ON FA.actor_id = A.ACTOR_ID
GROUP BY f.title
HAVING COUNT(*) > 1
ORDER BY COUNT(*) DESC
LIMIT 1
;

CREATE TABLE IF NOT EXISTS public.reviews_acb (
film_id int2 NOT NULL,
customer_id int2 NOT NULL,
review_date date NOT NULL,
review_description varchar,
CONSTRAINT reviews__acb_pkey PRIMARY KEY (film_id, customer_id)
);

SELECT * FROM public.reviews_acb;

insert INTO public.reviews_acn
(film_id,customer_id,review_date,review_description)
VALUES (10, 15, '10-11-2023', 'La película es TOP');