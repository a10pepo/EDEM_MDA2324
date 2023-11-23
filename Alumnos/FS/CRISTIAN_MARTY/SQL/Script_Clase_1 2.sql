--Pruebas
SELECT  actor.actor_id,
actor.first_name,
actor.last_name,
actor.last_update
FROM public.actor;

SELECT title,
rental_rate,
replacement_cost,
CONCAT(ROUND((rental_rate/replacement_cost)*100,2),'%')AS percentage
FROM public.film
ORDER BY percentage DESC;

SELECT title,
rental_rate,
replacement_cost,
CEIL((replacement_cost /rental_rate)) AS RATIO
FROM public.film
ORDER BY RATIO DESC ;


SELECT count(DISTINCT film_id) AS id_distintos,
max(rental_rate),
min(rental_rate),
avg(rental_rate),
stddev(rental_rate),
min(replacement_cost) AS min_costo_reemplazo
FROM film;

--Ejercicios
---Como se llaman los actores que comienzan con la letra 'A'?
SELECT first_name, last_name 
FROM actor  
WHERE first_name LIKE 'A%';


--● ¿Cuales son las películas que podemos alquilar por más de 10€? 
SELECT title, rental_rate  
FROM film  
WHERE rental_rate > 5 AND rental_duration < 10 ;


--¿Cuantas películas podemos alquilar por menos de 5€ y con una duración menor a 100 minutos?
SELECT count(film_id)  
FROM film  
WHERE rental_rate < 5 AND length  < 100 ;


--¿Qué precio de alquiler tienen las siguientes películas?
SELECT film_id, title, rental_rate
FROM film
WHERE title in ('Giant Troopers', 'Gilbert Pelican'); 

--¿Qué rating tiene la película Ali Forever? ¿Cuánta es su duración?
SELECT title,length,rating 
FROM film
WHERE title ='Ali Forever' ;


SELECT *
FROM inventory i 
--WHERE amount  = NULL 
