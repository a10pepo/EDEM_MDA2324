
-- ¿Cuantas ciudades tiene cada pais?

select c2.country ,count(c.city_id) as nº
from city c ,country c2 
where c.country_id = c2.country_id 
group by (c2.country_id);


-- ¿Que porcentaje supone el coste de alquiler sobre el coste de reemplazo?

select f.title,
f.rental_rate,
f.replacement_cost,
round((f.rental_rate/f.replacement_cost*100),2) as rentas_replacement
from film f;


-- ¿Cuantas veces tienen que alquilar una peli para recuperar la inversion?

select f.title,
ceiling((f.replacement_cost/f.rental_rate)) as veces_para_recuperar
from film f; 


-- ¿Cuantas peliculas hay?

select count(distinct f.film_id) as pelis_disponibles
from film f;


-- precio mas cara, precio mas barato, percio medio, variabilidad

select max(f.rental_rate) as precio_max,
min(f.rental_rate) as precio_min,
avg(f.rental_rate) as precio_medio,
stddev(f.rental_rate) as variabilidad_precios
from film f;


-- coste menor de remplazo y el mas grande

select max(f.replacement_cost) as rep_precio_max,
min(f.replacement_cost) as rep_precio_min
from film f;


-- Nombres de los actores que empiecen por A

select a.first_name as name,
a.last_name as surname 
from actor a
where a.first_name like 'A%';



-- pelis que se alquilan por mas de 10€ 

select f.title as titulo
from film f 
where f.rental_rate > 10;


-- que pelis se alquilan entre 5 y 10€

select count(f.film_id) as nº
from film f 
where f.rental_rate between 5 and 10;


-- pelis de menos de 5€ y menor de 100 mins de duracion

select count(f.film_id) as nº
from film f 
where f.rental_rate < 5 and f.length < 100;


-- precio alquiler las pelis 'Giant Troopers'...

select f.title as titulo,
f.rental_rate as percio_alquiler
from film f 
where f.title in ('Giant Troopers', 'Gilbert Pelican', 'Gilmore Boiled');


-- rating ali forever y la duracion

select f.title as titulo,
f.rating,
f.length 
from film f 
where f.title = 'Ali Forever';


-- hay algun nulo en precio alquiler

select count(f.film_id) as nº
from film f 
where f.rental_rate is null;


-- listado de pelis por orden de duracion

select f.title 
from film f
order by f.length asc;


-- 5 titulos de las pelis mas cortas

select f.title as titulo
from film f
order by f.length asc
limit 5;


-- seleciona datos diferentes por categoria de rating

select f.rating,
count(f.film_id)as nº,
round(avg(f.rental_rate),2) as mean_pr,
min(f.rental_rate) as min_pr,
max(f.rental_rate) as max_pr,
round(avg(f.length),2) as mean_dur,
min(extract(year from f.last_update)) as old_year,
max(extract(year from f.last_update)) as new_year
from film f 
group by rating;


-- el num de pelis por rating dnd el conteo sea mayor a 200

select f.rating ,
count(*)
from film f 
group by f.rating 
having count(*) > 200;


-- precio medio de alqiler por rating sup a 3

select f.rating,
round(avg(f.rental_rate),2)
from film f 
group by f.rating 
having avg(f.rental_rate) > 3;


-- duracion superior a 115

select f.rating,
round(avg(f.length),2)
from film f 
group by f.rating 
having avg(f.length) > 115;


-- direcciones de clientes que son de nuetro video club
-- SQLformat.org para hacer las queries bonitas
SELECT c.first_name AS name,
       c.last_name AS surname,
       c2.city AS city,
       c3.country AS country
FROM customer c
LEFT JOIN address a ON c.address_id = a.address_id
LEFT JOIN city c2 ON a.city_id = c2.city_id
LEFT JOIN country c3 ON c2.country_id = c3.country_id;


-- peliculas que tenga 1 actor q su apellido emoiece por c

SELECT distinct(f.title) AS title
FROM film f
LEFT JOIN film_actor fa ON f.film_id = fa.film_id
LEFT JOIN actor a ON a.actor_id = fa.actor_id
WHERE a.last_name like 'C%'
order by f.title;


-- cuantos actores por peli, 

select f.title as title,
count(a.actor_id) as nº_actores
from film f 
LEFT JOIN film_actor fa ON f.film_id = fa.film_id
LEFT JOIN actor a ON a.actor_id = fa.actor_id
group by f.film_id;


-- que pelis tienen mas de dos actores, 

select f.title as title,
count(a.actor_id) as nº_actores
from film f 
LEFT JOIN film_actor fa ON f.film_id = fa.film_id
LEFT JOIN actor a ON a.actor_id = fa.actor_id
group by f.film_id 
having count(a.actor_id) > 2;


-- que peli tiene más actores

SELECT f.title AS title,
       count(a.actor_id) AS nº_actores
FROM film f
LEFT JOIN film_actor fa ON f.film_id = fa.film_id
LEFT JOIN actor a ON a.actor_id = fa.actor_id
GROUP BY f.film_id
ORDER BY count(a.actor_id) DESC
LIMIT 1;


-- crear una tabla de rewiews_javdh

create table if not exists reviews_javdh(
	film_id serial4 not null,
	customer_id serial4 not null,
	review_date TIMESTAMP not null default NOW(),
	review_description VARCHAR(100) not null,
	constraint film_rev_javdh primary key(film_id, customer_id)
);


-- insertar cosas

insert into reviews_javdh (film_id, customer_id, review_date ,review_description)
values(8,5,'10-11-2023','peli malisima la verdad, recomiendo quemar cualquier cine donde se proyecte');


select c.customer_id 
from customer c  
order by c.customer_id; 

select *
from blockbuster;

update reviews_javdh  
set review_description = 'grita pez en voz alta'
where film_id = 8;

delete 
from reviews_javdh 
where film_id = 8;

alter table if exists reviews_cf
rename column review
to manolo;

alter table if exists review_jj
drop column review_date;

alter table if exists review_pepe
alter column customer_id type varchar;

--drop table reviews_edem; 


-- VISTAS

create view	my_view_of_the_world as
SELECT c.first_name AS name,
       c.last_name AS surname,
       c2.city AS city,
       c3.country AS country
FROM customer c
LEFT JOIN address a ON c.address_id = a.address_id
LEFT JOIN city c2 ON a.city_id = c2.city_id
LEFT JOIN country c3 ON c2.country_id = c3.country_id;

select *
from my_view_of_the_world 

SELECT actor_id, first_name, last_name, last_update 
FROM public.actor 
where first_name in 
	(select first_name 
	from public.actor 
	where last_name ilike 'C%' 
		or last_name ilike 'c%')

		
select f.title 
from film f 
where f.language_id in 
	(select l.language_id 
	from language l
	where l.name = 'English')
	

select c.first_name, c.last_name 
from customer c 
where c.address_id in 
	(select a.address_id 
	from address a
	where a.district  ilike 'A%')

	
select c.first_name, c.last_name 
from customer c 
where c.customer_id  in 
	(select p.customer_id  
	from payment p 
	group by p.customer_id 
	having sum(p.amount) > 200)
	
