--Ejercicio 0

/*select first_name as Nombre, last_name as Apellido
from public.actor*/

--Ejercicio 1
/*select title, rental_rate,replacement_cost,round(replacement_cost/rental_rate,2) as PuntoEquilibrio
from public.film*/

--Ejercicio 2
/*SELECT title, 
rental_rate, 
replacement_cost, 
ceil (rental_rate / replacement_cost) as new_operation
FROM public.film*/

--Ejercicio 3
--Como se llaman los actores que empiezan por la letra A
/*select first_name, last_name
from public.actor
where first_name like 'A%'*/

--Cuales son las películas que podemos alquilar por más de 10€? Ninguna
/*select title, rental_rate
from public.film
where rental_rate>10*/

--Cuantas películas podemos alquilar entre 5 y 10 euros? Ninguna
/*select title, rental_rate
from public.film
where rental_rate<10 and rental_rate>5*/

--¿Cuantas películas podemos alquilar por menos de 5€ y con una duración menor a 100 minutos?
/*select title, rental_rate, length
from public.film
where length<100 and rental_rate<5*/

--Ejercicio 4
--¿Qué precio de alquiler tienen las siguientes películas? Giant Troopers, Gilbert Pelican, Gilmore Boiled,

/*select title, rental_rate
from public.film
where title like 'Gilbert Pelican' or title like 'Gilmore Boiled' or title like  'Giant Troopers'*/

--¿Qué rating tiene la película Ali Forever? ¿Cuánta es su duración?
/*select title, rating,length
from public.film
Where title like 'Ali Forever'*/

--¿Nos falta por informar algún precio de alquiler en nuestra base de datos?
/*select title, rental_rate
from public.film
where rental_rate is null*/

--Ejercicio 5
-- El responsable de tienda está interesado en conocer mejor las películas que tienen en tienda.
--Desea obtener un listado de las películas por orden de duración (de menos duración a más duración)
/*select title, length
from public.film
order by length asc*/

--Quiere conocer los títulos de las 5 películas más cortas del videoclub
/*select title, length
from public.film
order by length asc
limit 5*/

--Ejercicio 6
--Obten por ‘rating’:
--○ El número de películas
/*select count(film)
from public.film*/
--○ El precio medio de alquiler
/*select ceil(avg(rental_rate))
from public.film*/
--○ El mínimo precio de alquiler
/*select min(rental_rate)
from public.film*/
--○ El máximo precio de alquiler
/*select max(rental_rate)
from public.film*/
--○ La duración media de las películas
/*select ceil(avg(length))
from public.film*/

--Ejercicio 7: Obten por ‘rating’: Este ejercicio no lo tengo muy claro
-- El número de películas y quédate únicamente con aquellos rating que tengan más de 200 películas
/*SELECT rating, COUNT(*)
FROM public.film
GROUP BY rating
HAVING COUNT(*) > 200;*/

--El precio medio de alquiler y quédate únicamente con aquellos rating que tenga un precio medio superior a 3
/*SELECT rating, AVG(rental_rate)
FROM public.film
GROUP BY rating
HAVING AVG(rental_rate) > 3;*/

-- La duración media de las películas y quédate con aquellos rating que tengan una duración media mayor a 115 minutos
/*SELECT rating, AVG(length)
FROM public.film
GROUP BY rating
HAVING AVG(length) > 115;*/


--Ejercicio 8
--Obtén las direcciones de aquellos clientes de nuestro videoclub
/*select customer_id, first_name,last_name,customer.address_id,address.address_id,address.address
from public.customer
left join public.address
on customer.address_id=address.address_id*/

--Ahora, añade las ciudades de las que son nuestros clientes
/*select customer.customer_id, customer.first_name,customer.last_name,customer.address_id,address.address,city.city
from public.customer
left join public.address
on customer.address_id=address.address_id
left join public.city
on address.city_id=city.city_id*/

--Ejercicio 9
--Obtén solamente las películas que tienen un actor que tenga un apellido que empiece por la letra “C”
/*SELECT film.title, film.title, actor.last_name
FROM public.film
INNER JOIN public.film_actor
ON film.film_id = film_actor.film_id
INNER JOIN public.actor
ON film_actor.actor_id = actor.actor_id
WHERE actor.last_name like 'C%'*/

--¿Cuántos actores tiene cada película?
/*SELECT film.title, count(film_actor.actor_id)
from public.film
inner join public.film_actor
on film.film_id=film_actor.film_id
inner join public.actor
on film_actor.actor_id=actor.actor_id
group by film.title*/

-- ¿Cuáles son las películas que tienen más de 2 actores? 
/*SELECT film.title, count(film_actor.actor_id)
from public.film
inner join public.film_actor
on film.film_id=film_actor.film_id
inner join public.actor
on film_actor.actor_id=actor.actor_id
group by film.title
having count(actor.actor_id)>2*/

-- ¿Cual es la película que tiene más actores? 
/*SELECT film.title, count(film_actor.actor_id)
from public.film
inner join public.film_actor
on film.film_id=film_actor.film_id
inner join public.actor
on film_actor.actor_id=actor.actor_id
group by film.title
order by count(actor.actor_id) desc*/

--Ejercicio 10


/*CREATE TABLE IF NOT EXISTS public.reviews_josan(
	film_id int2 NOT NULL,
	customer_id int2 NOT NULL,
	review_date date NOT NULL,
	review_description varchar,
	CONSTRAINT reviews_pkey PRIMARY KEY (film_id, customer_id));*/
	 
--Ejercicio 11

/*insert into reviews_josan(film_id, customer_id, review_description, review_date)
values (4, 7,' ha dicho que “La película es un poco aburrida','2023-11-10')*/

/*select *
from public.reviews_josan*/

--Ejercicio 12

/*UPDATE public.reviews_josan
SET review_description = 'La película es 
bastante divertida y para todo los públicos'
WHERE customer_id = 7 and film_id = 4;

select *
from public.reviews_josan*/

--Ejercicio 13
/*alter table public.reviews_josan
ALTER COLUMN  review_description type VARCHAR(200)*/

/*ALTER TABLE public.reviews_josan
ADD COLUMN review_satars Varchar(200);*/

/*update public.reviews_josan
set review_satars = 'Geniales'
WHERE customer_id = 7 and film_id = 4*/

/*alter table public.reviews_josan
drop review_satars*/

/*select *
from public.reviews_josan*/

/*drop table reviews_josan*/

--Ejercicio 14

/*CREATE VIEW my_view_josan2 as
Select actor.actor_id, actor.first_name, actor.last_name, actor.last_update
FROM public.actor
WHERE first_name LIKE 'J%';*/

