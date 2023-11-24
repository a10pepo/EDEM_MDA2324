---------------------------------------TRABAJO CLASE --------------------------------

select * from actor;

select * from address;

select count (*) as mismoNombre from actor
group by actor_id
order by mismoNombre desc;


select * from category;

select * from payment where rental_id  in (
select rental_id from rental);

select * from rental;


------------------------------------------------------------------------------------


select * 
from payment 
inner join rental 
on payment.rental_id = rental.rental_id;


select * 
from payment 
inner join rental 
on payment.rental_id = rental.rental_id;


-------------------------------------------

--ejercicio 1
select title, rental_rate, replacement_cost, round((replacement_cost/rental_rate),2) as porcentaje , ceil(replacement_cost/rental_rate) as duplicar
from film;

--ejercicio 2

select rental_rate,replacement_cost, ceil(replacement_cost/rental_rate) as superar_dias  from film;


-- ejercicio 3

select * from film;

select count(*) from film;
select count(distinct title ) from film;


select max(rental_rate) from film;
select min(rental_rate) from film;
select avg(rental_rate) from film;
 
select min(replacement_cost) as coste_min_replazo , max(replacement_cost) as coste_max_replazo from film;


--ejercicio 4

select  * from actor 
where first_name like 'A%';

select * from film;

select * from film
where rental_rate > 10;

select * from film
where rental_rate between 5 and 10;

select count(*) from film
where rental_rate < 5 and length <100 ;


-- ejercicio 4


select * from film
where title in ('Giant Troopers', 'Gilbert Pelican', 'Gilmore Boiled');

select rating from film
where title = 'Ali Forever';



select * from film
where rental_rate is null;

select * from film
where rental_rate = null;




-- ejercicio 5

select title, length  from film 
order by length desc
limit 5;


-- ejercicio 6

/*
● Obten por ‘rating’:
○	El número de películas
○ 	El precio medio de alquiler
○ 	El mínimo precio de alquiler
○ 	El máximo precio de alquiler
○ 	La duración media de las películas
○ 	El año de la película más antigua
○ 	El año de la película más nueva
year(date)
*/


select count(*), rating from film 
group by rating ;

select avg(rental_rate),rating  from film
group by rating;

select min(rental_rate),rating from film 
group by rating ;

select max(rental_rate),rating from film 
group by rating ;

select extract (year from last_update),last_update from film;

select min(release_year) from film;

select max(extract (year from last_update)), last_update from film
group by last_update;

select max(extract (month from last_update)), last_update from film
group by last_update;

select max(extract (day from last_update)), last_update from film
group by last_update;

select min(extract (year from last_update)), last_update from film
group by last_update;

--EJERCICIOS 6

-- HAVING
/*
● Obten por ‘rating’:
○ 	El número de películas y quédate únicamente con aquellos
		rating que tengan más de 200 películas
○ 	El precio medio de alquiler y quédate únicamente con aquellos
		rating que tenga un precio medio superior a 3
○ 	La duración media de las películas y quédate con aquellos
		rating que tengan una duración media mayor a 115 minutos
*/

select rating, count(film_id) as numero_peliculas_rating
from film
group by rating
having  count(film_id) > 200 ;


select rating, avg(rental_rate),count(film_id) as precio_medio
from film
group by rating
having  avg(rental_rate) > 3  and count(film_id) >200;


select rating, avg(length) from film
group by rating
having avg(length) > 115;




-- EJERCICIO 7

SELECT  a.film_id,a.title,b.actor_id , c.first_name, c.last_name 
FROM film_actor b
LEFT JOIN film a on a.film_id = b.film_id
left join actor c on b.actor_id = c.actor_id ;

/* 
 * 
 Responde a las siguientes preguntas:
		- ¿Cuántos actores tiene cada película?
		- ¿Cuáles son las películas que tienen más de 2 actores?
		- ¿Cual es la película que tiene más actores?
 
 */


SELECT a.title, count(actor_id) actor_por_pelicula
FROM film_actor b
inner JOIN film a on a.film_id = b.film_id
group by a.title
having count(actor_id) >2
order  by Count(actor_id) DESC
limit 1;

--
--Obtén las direcciones de aquellos clientes de nuestro videoclub


select a.address_id , b.address
from customer a
left join address B ON A.address_id  = b.address_id  ;



select a.address_id , b.address, c.city
from customer a
left join address b ON A.address_id  = b.address_id 
left join city c on c.city_id = b.city_id;


select a.address_id , b.address, c.city,c2.country
from customer a
left join address b ON A.address_id  = b.address_id 
left join city c on c.city_id = b.city_id
left join country c2 on c2.country_id  = c.country_id ;


SELECT FIRS_NAME, LAST_NAME, ADDRESS, CITY, COUNTRY
FROM customer c
INNER JOIN address a ON
c.address_id = a.address_id INNER JOIN city ct ON
ct.city_id = a.city_id INNER JOIN country co ON
     ct.country_id = co.country_id;
    
    



--Obtén solamente las películas que tienen un actor que tenga un apellido que empiece por la letra “C”
    
   
 
SELECT distinct a.title, c.last_name 
FROM film a
LEFT JOIN film_actor b ON a.film_id = b.film_id
LEFT JOIN actor c ON b.actor_id = c.actor_id
where c.last_name like 'C%';
 

/*
 
- ¿Cuántos actores tiene cada película?
- ¿Cuáles son las películas que tienen más de 2 actores?
- ¿Cual es la película que tiene más actores?
 */
 
 
SELECT distinct a.title, COUNT(*) as N_ACTORES
FROM film a
LEFT JOIN film_actor b ON a.film_id = b.film_id
group by a.title 
having COUNT(*) > 2
order by N_ACTORES DESC;

 
SELECT distinct a.title, COUNT(b.actor_id) as N_ACTORES
FROM film a
LEFT JOIN film_actor b ON a.film_id = b.film_id
group by a.title 
order by N_ACTORES DESC;

 
SELECT distinct a.title, COUNT(*) as N_ACTORES
FROM film a
LEFT JOIN film_actor b ON a.film_id = b.film_id
group by a.title 
order by N_ACTORES desc
limit 1;


CREATE TABLE IF NOT EXISTS public.reviews_mpv ( film_id int2 NOT NULL,
customer_id int2 NOT NULL,
review_date date NOT NULL,
review_description varchar);



insert INTO public.reviews_mpv (film_id,customer_id,review_date,review_description)
VALUES (3, 4, '09-11-2023', ':)');


select * from reviews_acn ;
   
select * from reviews_mpv;

UPDATE public.reviews_mpv
SET review_description = 'La película es bastante divertida y para todo los públicos' 
WHERE review_description = 'hola';



-- 48322294

alter table reviews_mpv add column Hola_Mar varchar;





---------------------------------------------------------------------------------

-------------------------------- VISTAS -----------------------------------------




CREATE VIEW my_view_of_actor_ACN AS
SELECT actor_id, first_name, last_name, last_update FROM public.actor
where first_name like '%C';

SELECT actor_id, first_name, last_name, last_update FROM public.actor
where first_name like '%';

select * from my_view_of_actor_ACN;



select COUNT(*) from (SELECT distinct a.title, c.last_name 
FROM film a
LEFT JOIN film_actor b ON a.film_id = b.film_id
LEFT JOIN actor c ON b.actor_id = c.actor_id
where c.last_name like '%C%') as ALIAS ;
 

select COUNT(*) from (SELECT distinct a.title, c.last_name 
FROM film a
LEFT JOIN film_actor b ON a.film_id = b.film_id
LEFT JOIN actor c ON b.actor_id = c.actor_id
where c.last_name Ilike '%C%') as ALIAS ;
 

SELECT actor_id, first_name, last_name, last_update FROM public.actor
where first_name in (select first_name from public.actor where last_name ilike 'C%')

--select first_name,last_name from public.actor where last_name ilike 'C%';


-- Obtén haciendo una subconsulta en la cláusula WHERE, todas aquellas películas que están en el idioma de inglés


SELECT *  FROM film ff where language_id in (
select language_id from "language" where name = 'English');




----

/*
 
 Subconsultas
- Obtén haciendo una subconsulta en la cláusula WHERE, todos aquellos clientes que viven en una dirección que empieza por A
- Obtén haciendo una subconsulta en la cláusula WHERE, aquellos clientes que han se han gastado más de 190€

 * */

 
select * from customer where address_id in (
select address_id from address where address ilike '%A%'
);

select address_id, address from address ;


select substring(address from 3 for 5) from address;


