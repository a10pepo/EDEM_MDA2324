select actor_id,
first_name,
last_name
last_update
from public.actor;

select title,
rental_rate,
replacement_cost,
round(replacement_cost /rental_rate,2) as nueva_columna
from film;


select title,
rental_rate,
replacement_cost,
ceil (replacement_cost /rental_rate) as nueva_columna2
from film;


select count(film_id) as nº_peliculas,
max(rental_rate) as pelicula_cara,
min(rental_rate) as pelicula_barata,
avg(rental_rate) as media_peliculas,
count(distinct(rental_rate)) as variablidad_precios,
min(replacement_cost) as remplazo_minimo,
max(replacement_cost) as remplazo_maximo
from film;


select title
from film
where rental_rate < 5;



-- ejercicio 
select first_name 
from actor 
where first_name like 'A%';

select title
from film 
where rental_rate > 10;

select title
from film
where rental_rate between 5 and 10;

select title
from film 
where rental_rate < 5 and length < 100

select title, rental_rate 
from film 
where title in ('Giant Troopers', 'Gilbert Pelican', 'Gilmore Boiled');

select title, rating, length
from film 
where title = 'Ali Forever'

select rental_rate, title from film
where rental_rate = null;

select title, length
from film 
order by length asc ;

select title, length
from film 
order by length asc 
limit 5;

select distinct rating, count(rating) as nº_peliculas,
round(avg(rental_rate),2) as precio_medio,
min(rental_rate) as precio_mínimo,
max(rental_rate) as precio_máximo,
round(avg(length)) as duracion_media,
min(extract(year from last_update)) as año_minimo,
max(extract(year from last_update)) as año_maximo
from film 
group by rating
having count(*)>200;

select distinct rating, 
count(rating) as nº_peliculas from film
group by rating
having count(rating)>200;

select distinct rating,
avg(rental_rate) as media_precio
from film
group by rating
having avg (rental_rate)>3;

select distinct count(title) as nºpelis ,rating,
avg(length) as duracion_media
from film
group by rating
having avg (length)>115;

select distinct rating from film;

SELECT c.first_name AS Nombre_Cliente,
       a.address AS Dirrección,
       c2.city AS Ciudades,
       c3.country AS Pais
FROM customer c
LEFT JOIN address a ON c.address_id = a.address_id
LEFT JOIN city c2 ON a.city_id = c2.city_id
LEFT JOIN country c3 ON c2.country_id = c3.country_id;

SELECT DISTINCT (f.title) AS Titulo
FROM film f
LEFT JOIN film_actor fa ON f.film_id = fa.film_id
LEFT JOIN actor a ON fa.actor_id = a.actor_id
WHERE a.last_name like 'C%';


select f.title as nombre_peli, count(a.actor_id) as numero_actores 
FROM film f
LEFT JOIN film_actor fa ON f.film_id = fa.film_id
LEFT JOIN actor a ON fa.actor_id = a.actor_id
group by f.film_id


select f.title as nombre_peli, count(a.actor_id) as numero_actores 
FROM film f
LEFT JOIN film_actor fa ON f.film_id = fa.film_id
LEFT JOIN actor a ON fa.actor_id = a.actor_id
group by f.film_id
having count(a.actor_id) > 2 

SELECT f.title AS nombre_peli,
       count(a.actor_id) AS numero_actores
FROM film f
LEFT JOIN film_actor fa ON f.film_id = fa.film_id
LEFT JOIN actor a ON fa.actor_id = a.actor_id
GROUP BY f.film_id
ORDER BY count(a.actor_id) DESC
LIMIT 1;


create table if not exists public.reviews_cf(
	film_id int2 not null,
	customer_id int2 not null,
	review_date date not null,
	review_description varchar(100),
	constraint cf_reviews_pkey primary key (film_id, customer_id)
);

insert into reviews_manolo (film_id, customer_id, review_date, manolo)
Values('1','10','09-11-2023','una locura')

select *
from reviews_manolo rm  ;

update reviews_fc 
set review_description  = 'locura de peli'
where review_description = 'TROYANO INCOMING';

alter table reviews_manolo  
rename to reviews_carlos

drop table public.reviews_carlos

CREATE VIEW my_view_carlos_ferrer AS
SELECT DISTINCT rating,
                count(rating) AS nº_peliculas,
                round(avg(rental_rate), 2) AS precio_medio,
                min(rental_rate) AS precio_mínimo,
                max(rental_rate) AS precio_máximo,
                round(avg(LENGTH)) AS duracion_media,
                min(extract(YEAR
                            FROM last_update)) AS año_minimo,
                max(extract(YEAR
                            FROM last_update)) AS año_maximo
FROM film
GROUP BY rating
HAVING count(*)>200;


select *
from my_view_carlos_ferrer;


SELECT a.actor_id,
       a.first_name,
       a.last_name,
       a.last_update
FROM public.actor a
WHERE a.first_name in
    (SELECT a2.first_name
     FROM public.actor a2
     WHERE a2.last_name ilike 'C%');
    
    
select *
from customer c 
where c.address_id  in 
					(select a.address_id 
					from address a 
					where a.address like '%A%');
				
select *
from customer c 
where c.customer_id  in 
					(select p.customer_id 
					from payment p  
					where p.amount  > '190');

