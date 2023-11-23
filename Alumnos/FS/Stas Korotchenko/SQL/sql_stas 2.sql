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

-- 10.11.2023 session 2 y 3

-- Ejercicio 8 Cláusula JOIN


select first_name, last_name, c.address_id, c2.city, c3.country 
from customer c
inner join address a on
	c.address_id = a.address_id
inner join city c2
	on a.city_id = c2.city_id
inner join country c3
	on c2.country_id = c3.country_id 

-- Ejercicio 9/1	Cláusula JOIN
-- Obtén solamente las películas que tienen un actor que tenga un apellido que empiece por la letra “C”
select f.title
from film f
inner join film_actor fa on f.film_id = fa.film_id
inner join actor a on fa.actor_id = a.actor_id
where a.last_name like 'C%'

 
-- Ejercicio 9/2 Cláusula JOIN

/*
- ¿Cuántos actores tiene
cada película?
- ¿Cuáles son las películas
que tienen más de 2
actores?
- ¿Cual es la película que
tiene más actores?*/

select title, count(first_name) 
from film f
inner join film_actor fa on f.film_id = fa.film_id
inner join actor a on fa.actor_id = a.actor_id
group by 1
having count(last_name) > 2
order by 2 desc

-- Ejercicio 10

create table if not exists public.reviews_sk (
	film_id int2 not null,
	customer_id int2 not null,
	review_date date not null,
	review_description varchar,
	CONSTRAINT reviews_pkey PRIMARY KEY (film_id, customer_id)
	);

-- Ejercicio 11

insert into reviews_sk (film_id, customer_id,review_date, review_description)
values ('4','7',' 10-11-2023','a película es un
poco aburrida')

-- Ejercicio 12

update reviews_sk
set review_description = 'La película es bastante divertida y para todo los
públicos'
where customer_id = '7' and film_id = '4' 

-- Ejercicio 13

alter table reviews_sk
	--add column review_stars int2
	--rename column review_description to review_opinion
	--alter column review_stars type varchar
	--drop column review_stars

delete
from reviews_sk
where customer_id = '7'

drop table public.reviews_sk 

-- Views
-- Ejercicio 14

create view stas_korotchenko as
select title, rating 
from film f 

-- Subconsultas en WHERE
-- Ejercicio 14
-- Obtén haciendo una subconsulta en la cláusula WHERE, todas aquellas películas que están en el idioma de inglés

SELECT *
FROM public.film
where title in (
	select f.title
	from film f 
	inner join "language" l on f.language_id = l.language_id
	where l.name = 'English'
	)
	
-- Ejercicio 15
-- Obtén haciendo una subconsulta en la cláusula WHERE, todos aquellos clientes que viven en una dirección que empieza por A

SELECT first_name
FROM public.customer c 
where address_id in (
	select address_id 
	from address a 
	where district  like 'A%'
	)	
	
-- Obtén haciendo una subconsulta en la cláusula WHERE, aquellos clientes que han se han gastado más de 190€
	
SELECT first_name
FROM public.customer c 
where customer_id in (
	select customer_id 
	from payment p 
	group by customer_id 
	having sum(amount) > 190
	);
	
-- WITH
-- La suma de los amount que de los clientes que han pagado más de 190€
	
with sub_query as (
select customer_id, sum(amount) as sum_cust
from payment p 
group by customer_id 
having sum(amount) > 190
)
select sum(sum_cust)
from sub_query

-- El número de clientes que han pagado más de 190€
with sub_query as (
select customer_id
from payment p 
group by customer_id 
having sum(amount) > 190
)
select count(customer_id)
from sub_query

-- El número de veces que un cliente ha alquilado una película.
-- El número de veces que un cliente ha alquilado una película en el año 2005 y en el 2006
-- por ejemplo sin with
select c.customer_id,c.first_name, c.last_name, f.title, count(f.title)
from customer c 
inner join rental r on c.customer_id = r.customer_id 
inner join inventory i on r.inventory_id  = i.inventory_id 
inner join film f on i.film_id = f.film_id
where extract (year from r.rental_date) in ('2005','2006')
group by c.customer_id, f.title
order by c.customer_id



 


	
	
 










