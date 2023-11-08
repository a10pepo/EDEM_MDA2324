select country_id, country from country;
-- sql prueba --

-- ejercicio 1--
select title, rental_rate, replacement_cost, 
concat( round(replacement_cost / rental_rate,2), '%') as new_column
from public.film;

--ejercicio 2--
select title, ceil(replacement_cost/rental_rate) as veces_rentabilidad
from film

select title as TÍTULO
from film;

select title as DISPONIBLE
from film;

select avg(rental_rate) as precio_medio 
from film;

select max(rental_rate) as mas_cara 
from film;

select min(rental_rate) as mas_barata 
from film;

select stddev(rental_rate) as variabilidad 
from film;

SELECT MIN(replacement_cost) AS menor_costo_reemplazo 
FROM film;

SELECT max(replacement_cost) AS menor_costo_reemplazo 
FROM film;

-- ejercicio 3 --
select 
first_name as NOMBRE_ACTOR, 
last_name as APELLIDOS_ACTOR
from actor

select
rental_rate as mas_10€
from film
where rental_rate >= 10

select 
rental_rate as entre_5y10
from film
where rental_rate < 10 and rental_rate > 5

select 
film_id as posicion_pelicula,
title as titulo,
rental_rate as entre_5y10
from film
where rental_rate < 5 and length < 100



