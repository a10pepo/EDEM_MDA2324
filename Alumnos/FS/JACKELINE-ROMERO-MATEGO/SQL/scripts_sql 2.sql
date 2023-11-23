/* EJERCICIO DE PRUEBA

select actor_id,
first_name,
last_name,
last_update
from public.actor;*/

-- Ejercicio 1: ¿Qué porcentaje supone el coste de alquiler sobre el coste de reemplazar?
-- Ofrece un resultado redondeado a 2 decimales y renombra la columna. 

/*select 
	title,
	rental_rate,
	replacement_cost,
	concat( ROUND (replacement_cost / rental_rate ,2), '%') as percentage_rent_cost
from public.film*/

-- EJERCICIO 2: ¿Cuántas veces tienen que alquilar cada película para igualar o superar el coste de reemplazar la película?
-- Da un resultado entero y renombra la nueva columna.

select 
	title,
	rental_rate,
	replacement_cost,
	ceiling(replacement_cost / rental_rate) as rent_time
from public.film;

-- Incluye en todas tus queries un alias a la tabla y renombra la columna 'title' por 'título'
-- ¿Cuántas películas disponibles? 
-- ¿Cuál es la película a alquilar más cara? ¿Y la más barata? ¿Cuál es el precio medio de alquiler?
-- ¿Qué variabilidad de precios tenemos?
-- ¿Cuál es el coste más pequeño de reemplazo? ¿Cuál es el más grande?

select 
count(title) as total_peliculas, 
max(f.rental_rate) as expensive_film, 
min(f.rental_rate) as cheap_film, 
avg(f.rental_rate) as average_rent, 
stddev(rental_rate) as variabilidad, 
min(replacement_cost) as min_replacement_cost,
max(replacement_cost) as max_replacement_cost  
from public.film f;

-- ¿Cómo se llaman los actores que empiezan por la letra A?
-- ¿Cuáles son las películas que podemos alquilar por más de 10€?
-- ¿Cuántas películas podemos alquilar entre 5 y 10 euros?
-- ¿Cuántas películas podemos alquilar por menos de 5€ y con una duración menor a 100 minutos?

select 
	first_name
from public.actor
where first_name like 'A%';

select 
	title
from public.film
where rental_rate > 10;

select
	count (title)
from public.film
where rental_rate between 5 and 10;

select
	count (title)
from public.film
where rental_rate < 5 and length < 100;

-- ¿Qué precio de alquiler tienen las siguientes películas? Gliant Troopers, Gilbert Pelican, Gilmore Boiled
-- ¿Qué rating tiene la película "Ali Forever"? ¿Cuánta es su duración?
-- ¿Nos falta por informar algún precio de alquiler en nuestra base de datos?

select
	title,
	rental_rate 
from public.film
where title in ('Giant Troopers', 'Gilbert Pelican', 'Gilmore Boiled');

select
	title,
	rating,
	length
from public.film
where title in ('Ali Forever');

select
	count(title)
from public.film
where rental_rate is null;

-- El responsable de tienda está interesado en conocer mejor las películas que tienen en la tienda. 
-- Desea obtener un listado de las películas por orden de duración (de menos duración a más duración)
-- Quiere conocer los títulos de las 5 películas más cortas del videoclub.

select 
	title,
	length 
from public.film
order by length asc 
limit 5;


/*Obten por 'rating':
 * nº de películas
 * precio medio de alquiler
 * mínimo precio de alquiler
 * máximo precio de alquiler
 * la duración media de las películas
 * el año de la película más antigua
 * el año de la película más nueva
 */

select
	rating,
	count(title)
from public.film
group by rating;

select
	rating,
	round(avg(rental_rate),2) as average_rentalrate
from public.film
group by rating;

select
	rating,
	min(rental_rate) as min_rentalrate
from public.film
group by rating;

select
	rating,
	max(rental_rate) as max_rentalrate
from public.film
group by rating;

select
	rating,
	round(avg(rental_duration),2) as average_rentalduration
from public.film
group by rating;

-- prueba

/*select
	title, release_year 
from public.film
order by release_year;*/

select 
	rating, 
	min(release_year)
from public.film
group by rating;

select 
	rating,
	max(release_year)
from public.film
group by rating;


/*Obten por 'rating':
 * - El número de películas y quédate únicamente con aquellos rating que tengan más de 200 películas.
 * - El precio medio de alquiler y quédate únicamente con aquellos rating que tenga un precio medio superior a 3.
 * - La duración media de las películas y quédate con aquellos rating que tengan una duración media mayor a 115 minutos.
 */

select 
	rating,
	count(title)
from film
group by rating
having count(title) > 200;

select
	rating,
	round(avg(rental_rate),2) as avg_rentalratemas3
from film
group by rating 
having avg(rental_rate) > 3;

select 
	rating,
	avg(rental_duration)
from film f 
group by rating
having avg(rental_duration) > 115;

-- Obtén las direcciones de aquellos clientes de nuestro videoclub: ¿De dónde son mis clientes?
-- Añade las ciudades de las que son nuestros clientes
-- Añade el país también

select c.first_name , a.address , c2.city , c3.country 
from customer c
left join address a on c.address_id = a.address_id 
left join city c2 on a.city_id = c2.city_id 
left join country c3 on c2.country_id = c3.country_id; 

-- Obtén solamente las películas que tienen un actor que tenga un apellido que empiece por la letra "C"

select f.title , a.last_name 
from film f 
left join film_actor fa on f.film_id = fa.film_id 
left join actor a on fa.actor_id = a.actor_id
where last_name like 'C%'

-- ¿Cuántos actores tiene cada película?
-- ¿Cuáles son las películas que tienen más de 2 actores?
-- ¿Cuál es la película que tiene más actores?

select 
	f.film_id, 
	count(fa.actor_id) 
from film f 
inner join film_actor fa on f.film_id = fa.film_id 
group by 1;

create table if not exists public.reviews_jr (
film_id int2 not null,
customer_id int2 not null,
review_date date not null,
review_description varchar)

insert into public.reviews_jr (film_id, customer_id, review_description, review_date)
values (4, 7, 'La pelicula es un poco aburrida', '10-11-2023');

insert into public.reviews_jc (film_id, customer_id, review_description, review_date)
values (2, 4, 'Espabila piolin', '10-11-2023');

update public.reviews_emg 
set review_description = 'Amo los viernes'
where review_description = 'La pelicula es aburrida';

delete 
from public.reviews_jc 
where review_description = 'Espabila piolin';

-- SESIÓN SÁBADO 11 NOVIEMBRE

alter table public.reviews_fc
rename column film_id
to identificador_pelicula;

alter table public.reviews_fc
alter column identificador_pelicula type varchar;

drop table public.reviews_pm;

-- CREAR VISTAS

create view my_view_of_actor_jr as
select actor_id , first_name, last_name , last_update
from public.actor
where first_name like 'F%';

select * from my_view_of_actor_jr;

SELECT actor_id, first_name, last_name, last_update
FROM public.actor
where first_name in (select first_name from
public.actor where last_name ilike 'C%')

/*Obtén haciendo una subconsulta en la cláusula WHERE, todas aquellas
películas que están en el idioma de inglés*/

select *
from public.film
where language_id  in (select language_id  from public.language where name = 'English');

/*Obtén haciendo una subconsulta en la cláusula WHERE, todos
aquellos clientes que viven en una dirección que empieza por A*/

select *
from public.customer
where address_id in (select address_id from public.address where address ilike '%A%');

/*Obtén haciendo una subconsulta en la cláusula WHERE, aquellos
clientes que han se han gastado más de 190€*/











	


