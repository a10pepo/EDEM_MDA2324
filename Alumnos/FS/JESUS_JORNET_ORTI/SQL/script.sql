--ejercicio 1

/* Qué porcentaje supone el coste de alquiler sobre el coste de reemplazar?
 Ofrece un resultado redondeado a 2 decimales y renombra la columna. 
 */

select title,
rental_rate,
replacement_cost,
round (replacement_cost/rental_rate,2) as Porcentaje 
from public.film;

--ejercicio 2
/* Cuántas veces hay que alquilar una película para que sea rentable
*/

select title,
rental_rate,
replacement_cost,
ceiling (replacement_cost/rental_rate) as Rentable
from public.film;

--ejercicio 3
/* ¿Cómo se llaman los actores que empiezan por la letra A?
¿Cuáles son las películas que podemos alquilar por más de 10€?
¿Cuántas películas podemos alquilar entre 5 y 10€?
¿Cuántas películas podemos alquilar por menos de 5€ y con una duración menor a 100 minutos?
*/

select *
from public.actor
where first_name like 'A%'

select *
from public.film
where rental_rate > 10

select *
from public.film
where rental_rate between 5 and 10


select
count (film_id)
from public.film
where rental_rate < 5 and length <100

--ejercicio 4
/* ¿Qué precio de alquiler tienen las siguientes películas? Giant Troopers - Gilbert Pelican - Gilmore Boiled
 * ¿Qué rating tiene lapelícula Ali Forever? ¿Cuánta es su duración?
 * Nos falta por ingormar algún precio de alquiler en nuestra base de datos?
 */ 

select
title,
rental_rate
from public.film
where title in ('Giant Troopers' , 'Gilbert Pelican' , 'Gilmore Boiled')

select
title,
rating,
length 
from public.film
where title = 'Ali Forever'

select
title
from public.film 
where rental_rate is null 


--ejercicio 5
/* El responsable de tienda está interesado en conocer mejor las películas que tienen en tienda.
 * - desea obtener un listado de las películas por orden de duración (de menos duración a más duración)
 * - Quiere conocer los título de las 5 pelícu.as más cortas del videoclub
 */


select rating, 
	count(*)as number,
	avg(rental_rate) as media,
	min(rental_rate) as mínimo,
	max(rental_rate) as máximo,
	avg(length) as duración_media,
	min(extract(year from last_update)) as antigua,
	max(extract(year from last_update)) as nueva	
from film
group by rating
	having count(*) > 200;
	

select rating, 
	count(*)as number,
	avg(rental_rate) as media,
	min(rental_rate) as mínimo,
	max(rental_rate) as máximo,
	avg(length) as duración_media,
	min(extract(year from last_update)) as antigua,
	max(extract(year from last_update)) as nueva	
from film
group by rating
	having avg(rental_rate) > 3;
	

select rating, 
	count(*)as number,
	avg(rental_rate) as media,
	min(rental_rate) as mínimo,
	max(rental_rate) as máximo,
	avg(length) as duración_media,
	min(extract(year from last_update)) as antigua,
	max(extract(year from last_update)) as nueva	
from film
group by rating
	having avg(length) > 115;
	
-- Vistas -- 


create view GDPR_NOT_COMPLIANT as
select a.first_name, a.last_name , b.address, c.city, d.country
from customer a
left join address b on a.address_id = b.address_id
left join city c on b.city_id = c.city_id
left join country d on c.country_id = d.country_id 
order by country asc 

select *
from gdpr_not_compliant 


select a.title , c.first_name, c.last_name
from film a
right join film_actor b on a.film_id = b.film_id
right join actor c on b.actor_id = c.actor_id
where c.last_name like 'C%'

select a.title , c.first_name, c.last_name
from film a
left join film_actor b on a.film_id = b.film_id
left join actor c on b.actor_id = c.actor_id
where c.last_name in (
					select last_name
					from public.actor
					where last_name like 'C%')


--¿Cuántos actores tiene cada película?
--¿Cuáles son las películas que tienen más de 2 actores?
--¿Cual es la película que tiene más actores?

select a.title,
count(actor_id)as number
from film a
left join film_actor b on a.film_id = b.film_id
group by a.title 
having count(actor_id) > 2
order by count(actor_id) desc
limit 1;

--reviews en una tabla con mi nombre

create table if not exists reviews_jj (
film_id int2 not null,
customer_id int2 not null,
review_date date not null,
review_description varchar,
primary key (film_id)
);

insert into reviews_jj (film_id,customer_id,review_date,review_description)
values (4, 7, '2023-11-11', 'La película es peor que Piratas del Caribe');

select film_id,customer_id,review_date,review_description
from reviews_jj

select *
from reviews_fc;

update reviews_fc
set review_description = 'órale putooooo'
where review_description = 'locura de peli'

alter table reviews_fc 
rename column review_description
to opiniones_de_mierda;

alter table reviews_fc
alter column mi_columnita type varchar;

drop table reviews_led;


--Obtén haciendo una subconsulta en la cláusula WHERE, todas aquellas oelículas que están en inglés

select title
from film a
left join language b on a.language_id = b.language_id
where name in (
			select name
			from language
			where name like 'Eng%')
			
select *
from film f
where language_id in (
				select language_id
				from "language" l
				where name = 'English')
				
-- Obtén haciendo subconsulta WHERE todos los clientes que viven en una dirección que empiece por A
				
select *
from customer
where address_id in (
			select address_id
			from address
			where address like 'A%')
				
-- Aquellos clientes que han gastado más de 190€

select a.customer_id, b.first_name, b.last_name, a.amount
from payment a 
right join customer b on a.customer_id = b.customer_id
where amount < 190
			