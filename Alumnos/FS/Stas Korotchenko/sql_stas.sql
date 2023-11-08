-- ejercicio 1
SELECT title, rental_rate, replacement_cost, round(rental_rate/replacement_cost*100, 2) as porcentaje
FROM public.film

-- ejercicio 2/1
SELECT title, rental_rate, replacement_cost, floor(replacement_cost/rental_rate) as veces
FROM public.film

-- ejercicio 2/2
/*
 ** Включите псевдоним таблицы во все запросы и переименуйте столбец.
«название» за «названием»
Сколько фильмов доступно?
Какой фильм самый дорогой в прокате? И самый дешевый? Какова средняя стоимость аренды? Какой у нас разброс цен?
Какая минимальная стоимость замены? Какой из них самый большой?
*/
SELECT count(distinct film_id), MAX(replacement_cost) as mas_caro, MIN(replacement_cost) as mas_barato, 
AVG(replacement_cost) as precio_medio
FROM public.film

-- ejercicio 3
-- ¿Cómo se llaman los actores que empiezan por la letra A?
select first_name 
from public.actor a
where first_name like 'A%'

-- ¿Cuales son las películas que podemos alquilar por más de 10€?
select title 
from public.film f 
where rental_rate > 10

-- ¿Cuantas películas podemos alquilar entre 5 y 10 euros?
select count(title) 
from public.film f 
where rental_rate between 2 and 3

-- ¿Cuantas películas podemos alquilar por menos de 5€ y con una duración menor a 100 minutos?
select count(title)
from film f 
where rental_rate < 5 and length  < 100;


-- ejercicio 4

-- ¿Qué precio de alquiler tienen las siguientes películas? Giant Troopers Gilbert Pelican Gilmore Boiled
select title, rental_rate as "hy hy"
from film f
where title in ('Giant Troopers', 'Gilbert Pelican', 'Gilmore Boiled');

-- ¿Qué rating tiene la película Ali Forever? ¿Cuánta es su duración?
select rating, length
from public.film f 
where title = 'Ali Forever';

-- ¿Nos falta por informar algún precio de alquiler en nuestra base de datos?
select title
from film f
where rental_rate is null

-- ejercicio 5

-- Desea obtener un listado de las películas por orden de duración (de menos duración a más duración)
select title
from public.film f 
order by length asc

-- Quiere conocer los títulos de las 5 películas más cortas del videoclub
select title
from public.film f 
order by length asc
limit 5

-- ejercicio 6

-- Obten por ‘rating’:  El número de películas El precio medio de alquiler El mínimo precio de alquiler El máximo precio de alquiler La duración media de las películas
select rating, count(title), avg(rental_rate), min(rental_rate), max(rental_rate), avg(length)  
from film f
group by rating 

-- ejercicio 7
-- Tiene una primera hipótesis. ¿Los precios de alquiler de las películas son mayores cuanto mayor es la duración?
select rental_rate, AVG(length) as length 
from film f
group by rental_rate 
order by rental_rate 

-- Tiene una segunda hipótesis. ¿Los precios de alquiler de las películas son mayores cuanto mayor es el coste de reemplazo?

select rental_rate, avg(replacement_cost) as replacement_cost 
from film f
group by rental_rate
order by rental_rate

-- ejercicio 8

-- El número de películas y quédate únicamente con aquellos rating que tengan más de 200 películas
select rating, count(title)
from film f 
group by rating
having count(title) > 200

-- El precio medio de alquiler y quédate únicamente con aquellos rating que tenga un precio medio superior a 3
select rating, avg(rental_rate) as avd_rating 
from film f 
group by rating
having avg(rental_rate) > 3

-- La duración media de las películas y quédate con aquellos rating que tengan una duración media mayor a 115 minutos
select rating, avg(length) as avg_length
from film f 
group by rating
having avg(length) > 115











