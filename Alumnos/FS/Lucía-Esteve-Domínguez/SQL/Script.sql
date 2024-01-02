- Prueba SQL 
SELECT actor_id, 
first_name, 
last_name,
last_update
FROM public.actor;


--Ejercicio1: RENOMBRAR --> ENTRE PARENTESIS LAS COLUMNAS MAS AS  REDONDEAR ROUND (LAS COLUNAS A REDONDEAR),los decimales que quieres y  para finalizar fragmento siempre ; 
SELECT title, 
rental_rate,
replacement_cost,
ROUND (rental_rate/replacement_cost , 2) AS PORCENTAJE
FROM public.film;

--Ejercicio1:añadir el porcentaje concatenamos --> concat (string1 los string los alinea a la izq, string2) 
CREATE VIEW my_view_led AS
SELECT title, 
rental_rate,
replacement_cost,
CONCAT (ROUND ((rental_rate/replacement_cost) * 100,2),'%') AS PORCENTAJE
FROM public.film


--Ejercicio2: redondear a la alta --> CEILING
SELECT title, 
rental_rate,
replacement_cost,
CEILING  (replacement_cost / rental_rate) AS NUMVECES
FROM public.film;

--Ejercicio3 --> ¿cuántas películas hay disponibles?
SELECT count (DISTINCT (title))  
FROM public.film;

-- Ejercicio 4 --> ¿cuál es la pelicula más cara? ¿y la más barata? con un alias --> AS 
SELECT max (rental_rate) AS precio_minimo, 
 min (rental_rate) AS precio_máximo
FROM public.film f;

-- Ejercicio 5 --> ¿cuál es el precio medio de alquiler? 
SELECT avg(rental_rate)AS precio_medio
FROM public.film f;
--Ejercicio 6  --> ¿Qué variabilidad de precios tenemos? 
SELECT stddev(rental_rate)
FROM public.film f;
--Ejercicio 7 --> Coste más pequeño de remplazo


--Ejercicio 8 --> Coste más grande de remplazo

--> EJERCICIOS CON WHERE 

-- Ejercicio 1: 

--CLASE SQL 2 
-- GROUP BY : 
--número de películas Ejercicio 6: 
SELECT rating, count(film_id) AS conteo_peliculas,
avg(rental_rate) AS precio_medio_alq,
min(rental_rate) AS precio_minimo_alq,
max(rental_rate) precio_max_alq, 
avg(length) AS duración_media,
MIN (EXTRACT (YEAR FROM last_update )),
MAX (EXTRACT (YEAR FROM last_update ))
FROM film
GROUP BY rating

--HAVING para filtrar dentro de la agrupación --> ES UN FILTRO DE LA TABLA
--Ejercicio 7 
SELECT rating, count(film_id) AS conteo_peliculas,
avg(rental_rate) AS precio_medio_alq,
avg(length) AS duración_media
FROM film
GROUP BY rating
HAVING count(film_id)>200 AND avg(film.rental_rate)>3 AND avg(length) >115

-- Práctica de joins 
-- Obten las direcciones de aquellos clientes de nuestro videoclub 

SELECT c.address_id, a.address
FROM customer c 
inner JOIN address a ON
	c.address_id = a.address_id
inner JOIN city b ON
	a.city_id  = b.city_id 
inner JOIN country d a ON
	b.country_id = d.country_id 

	-- EJERCICIO 9 
	--Obtener las películas que tengan un actor que empiece por la letra c 
	
	SELECT f.title, a.actor_id 
	FROM film f 
	INNER JOIN film_actor fa ON
		fa.film_id = f.film_id 
	INNER JOIN actor a ON
		fa.actor_id = a.actor_id 
	WHERE a.last_name LIKE 'C%'
	
	-- EJERCICIO 9 
	--¿cuántos actores tiene cada película?
	--¿cuáles son las películas que tienen más de 2 actores?
	--¿cuál es la película que tiene más actores? 
	
	SELECT film actor id, 
	
	-- CREAR TABLA 
	CREATE TABLE reviews_led(
		film_id int2,
	customer_id int2,
	review_date date,
	review_description varchar);
		
    INSERT INTO reviews_led (film_id,customer_id,review_date,review_description)
	VALUES('4','7','10/11/2023','La película es un poco aburrida')
	
	SELECT * 
	FROM reviews_fc
	
	ALTER TABLE reviews_fc 
	DROP COLUMN review_date
	
	ALTER TABLE reviews_fc 
	RENAME COLUMN customer_id
	TO clientes_de_mierda

ALTER TABLE reviews_fc 
ALTER COLUMN clientes_de_mierda TYPE VARCHAR;

DROP TABLE reviews_fc 

CREATE VIEW my_view_

SELECT *
FROM my_view_led 

-- SUBCONSULTAS

SELECT actor_id, first_name, last_name, last_update 
FROM public.actor 
WHERE first_name IN (SELECT first_name FROM public.actor WHERE last_name ILIKE 'c%')

--Ejercicio obtén una subconsulta con la clausula Where todas las peliculas en idioma inglés

SELECT TITLE  
FROM film  
WHERE language_id  IN (SELECT language_id  FROM "language"  WHERE name  = 'English')

--WITH creas una 'variable' de una subconsulta, le pones nombre a la subconsulta y luego puedes hacer cualquier operación con la subconsulta



