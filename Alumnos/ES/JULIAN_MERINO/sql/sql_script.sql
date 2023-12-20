/* Ejercicio 1 */
select first_name as nombre, last_name as apellido
from actor a

/* Ejercicio 2*/
select title, rental_rate, replacement_cost, rental_rate  + replacement_cost as operacion,
concat(round(100 * rental_rate / replacement_cost, 2),'%') as rental_replacement /* The same as casting the numeric bit with ::varchar*/
from public.film


/*Ejercicio 3*/
select title, rental_rate, replacement_cost, ceil(replacement_cost / rental_rate)
from film f 

/*Ejercicio 4*/
select count(title) as Título 
from film f 

/*Ejercicio 5*/

/*Ejercicio 6*/

/*Ejercicio 7 - Todos los datos de la peli Academy Dinosaur*/
select * from film f 
where title = 'Academy Dinosaur'

/*Ejercicio 8 - Muestra todas las pelis que cuesten menos de 5€ de alquiler*/
select title, rental_rate from public.film 
where rental_rate <5

/*Ejercicio 9 - Actores que empiezan por la letra a*/
select first_name from actor a 
where first_name LIKE 'A%'

/*Ejercicio 10 - Pelis en alquiler por >4€*/
select title from film f 
where rental_rate > 4;

/* Ejercicio 11 - Pelis en alquiler entre 2€ y 4€*/
select title, rental_rate from film 
where rental_rate between 2 and 4

/*Ejercicio 12 - Cuántas pelis en alquiler por menos de 10€ y que duren menos de 100 min*/
select title, rental_rate, length from film 
where rental_rate < 5 and length < 100;

/*Ejercicio 13 - Precio de Giant Troopers, Gilbert Pelican y Gilmore Boiled*/
select title, rental_rate from film where title like 'Gi%';

/*Ejercicio 14 - rating y duración de Ali Forever*/
select title, rating, length from film where title like 'Ali Forever';

/*Ejercicio 15 - Pelis sin precio de alquiler*/
select count(title)  from film where rental_rate is null 

/*Ejercicio 16 - Responsable quiere conocer mejor sus pelis: listar pelis por oden de duración (- a +)
y conocer las 5 pelis más cortas*/
select title, length from film f 
order by length desc limit 5

/*Ejercicio 17 - Encuentra la peli más cara por minuto*/
select title, rental_rate, (rental_rate / length) as precio_minuto
from film order by precio_minuto desc limit 10

/*Ejercicio 18 - 10 pelis m´s antiguas cuyo precio de alquiler < 3€*/
select title, release_year, rental_rate
from film f 
where rental_rate < 3
order by release_year asc limit 10

/*Ejercicio 19 - Group by: selecciona pelis por rating: número de pelis*/
select rating, count(rating) as no_pelis, round(avg(rental_rate),2) as alquiler_medio, min(rental_rate) as alquiler_min,
max(rental_rate) as alquiler_max, round(avg(length), 2) as duración_media, 
min(release_year) as más_antigua, max(release_year) as más_reciente
from film f 
group by rating

/*Ejercicio 20 - HAVING - agrupar pelis por rating cuando haya más de X pelis en ese grupo*/
select rating, count(rating) as no_pelis, round(avg(rental_rate),2) as alquiler_medio, min(rental_rate) as alquiler_min,
max(rental_rate) as alquiler_max, round(avg(length), 2) as duración_media, 
min(release_year) as más_antigua, max(release_year) as más_reciente
from film f 
group by rating having count(rating) > 200

/*Ejercicio 21 - Obtén por rating el no. de pelis y quédate con los rating con más de 200 pelis*/
select count(title), rating from film f group by rating having count(rating) > 200

/*Ejercicio 22 - Obtén por rating el precio medio del alquiler y quédate con aquellos rating con un precio medio entre 1 y 3*/
select avg(rental_rate), rating from film f 
group by rating 
having 1 <= avg(rental_rate) and 3 >= avg(rental_rate)

/*Ejercicio 24 - Obtén por rating duración media de las pelis y qiédate con aquellos rating con una duración media
 * mayor a 115 pero menor a 200 min*/
select avg(length), rating from film f 
group by rating 
having avg(length) > 115 and 200 > avg(length)

/*Ejercicio 25 - Obtén por rating que empiecen por P*/
select title, rating from film f 
where rating::text like 'P%'

/*Ejercicio 26 - Obtén direcciones de aquellos clientes de nuestro videoclub*/
select c.first_name, c.last_name, a.address, ct.city, co.country
from customer c 
join address a 
on a.address_id = c.address_id
join city ct 
on a.city_id = ct.city_id
join country co 
on co.country_id = ct.country_id
order by c.first_name asc

/*Ejercicio 27 - Obtén no. de clientes agrupados por países*/
select co.country, count(co.country)
from customer c 
join address a 
on a.address_id = c.address_id
join city ct 
on a.city_id = ct.city_id
join country co 
on co.country_id = ct.country_id
group by co.country
order by co.country asc

/*Ejercicio 28 - Obtén pelis con un actor con un apellido que empiece por C*/
select f.title, a.first_name, a.last_name
from film f
join film_actor fa 
on f.film_id = fa.film_id
join actor a 
on fa.actor_id = a.actor_id
where a.last_name like 'C%'

/*Ejercicio 29 - Cuántos actores tiene cada peli*/
select f.title, count(a.actor_id)
from actor a 
join film_actor fa 
on a.actor_id = fa.actor_id
join film f 
on fa.film_id = f.film_id
group by f.title
order by f.title asc

/*Ejercicio 30 - Pelis con más de dos actores*/
select f.title as "Título", count(a.actor_id) as "Recuento"
from actor a 
join film_actor fa 
on a.actor_id = fa.actor_id
join film f 
on fa.film_id = f.film_id
group by f.title /*Se puede poner group by 1 (primera columna en select) para ahorrar tiempo de computación*/
having count(a.actor_id) > 2
order by count(a.actor_id) desc

/*Ejercicio 31 - Peli con más actores*/
select f.title as "Título", count(a.actor_id) as "Recuento"
from actor a 
join film_actor fa 
on a.actor_id = fa.actor_id
join film f 
on fa.film_id = f.film_id
group by f.title /*Se puede poner group by 1 (primera columna en select) para ahorrar tiempo de computación*/
having count(a.actor_id) > 2
order by count(a.actor_id) desc
limit 1

/*Ejercicio 32 - Generar una tabla nueva con film_id, customer_id, review_date y review_description*/
create table public.review_jmp(
film_id int2,
customer_id int2,
review_date timestamp,
review_description varchar(50),
constraint review_jmp_pkey primary key (film_id, customer_id)
/*constraint review_jmp_filmid_fkey foreign key (film_id) references public.film(film_id), quitamos las foreign keys, no tenemos permisos*/
/*constraint review_jmp_customerid_fkey foreign key (customer_id) references public.customer(customer_id)*/
)

/*Ejercicio 33 - Insertar datos (filas) en tablas de compañeros*/
insert into reviews_jorgeredbull (film_id, customer_id, review_date, review_description)
values (4, 4, '11-29-2023', 'Mr Robot es mucho mejor que Mi Pequeño Pony')

/*Ejercicio 34 - Actualizar la tabla de arriba con update*/
update reviews_jorgeredbull
set review_description = 'Fucking panza lambo burpees mileurista foak'
where customer_id = 4 and film_id = 4;

/*Ejercicio 35 - Cambiar tipo de dato de una columna, añadir/borrar entradas, etc.*/
insert into reviews_reyes (film_id, customer_id, review_date, mi_fakin_opinion)
values (13, 14, '11-30-2023', 'GO HOME, NO QR SORRY')

/*Ejercicio 36 - Renombrar una columna*/
alter table review_jmp
rename column review_description to descripcion_reseña;

/*Ejercicio 37 - Cambiar nombre de otra columna*/
alter table review_jarupu
rename column llados to matias_el_humilde;

/*Ejercicio 38 - Cambiar tipo de datos a varchar*/
alter table review_jarupu
alter column matias_el_humilde type varchar

/*Ejercicio 39 - delete: borrar registros de una tabla, bajo condición*/
delete review_jarupu 
where jorje_es_toni_cuquerella = '16474' and jose_mota_es_mi_padre = '2'

/*Ejercicio 40 - Eliminar tabla*/
drop table review_jmp

/*Ejercicio 41 - Crear una vista*/
create view my_view_of_actor_jmp as
select actor_id, first_name, last_name, last_update
from public.actor

/*Ejercicio 42 - Ejecutar una vista*/
select * from my_view_of_actor_jmp

/*Ejercicio 43 - Eliminar una vista*/
drop view my_view_of_actor_jmp

/*Ejercicio 44 - Subquery en where*/
select actor_id, first_name, last_name, last_update
from public.actor
where actor_id in (select actor_id from public.actor
where last_name ilike 'C%')

/*Ejercicio 45 - Todas las pelis que estén en inglés haciendo subquery en where*/
select title, language_id
from film
where language_id in (select language_id from language where language_id = '1')

/*Ejercicio 46 - Todos aquellos clientes que viven en una dirección que empieza por A*/
select customer_id, first_name, last_name, address_id
from customer
where address_id in (select address_id from address where address ilike '122%')

/*Ejercicio 47 - Obtén haciendo una subconsulta en where aquellos clientes que se han gastado más de 190€*/
select customer_id, first_name, last_name
from customer
where customer_id in (select customer_id from payment group by customer_id having sum(amount) > 190)

/*Ejercicio 48 - Obtén haciendo una subconsulta en where la suma de aquellos 4 clientes que se han gastado más de 190€*/
select sum(amount) as suma_4
from payment
where customer_id in (
select customer_id
from payment
group by customer_id
having sum(amount) > 190)

/*Ejercicio 49 - Obtén haciendo una subconsulta aquellos clientes que se han gastado más de 190€ con WITH*/
with my_subquery as (
select customer_id from payment
group by customer_id
having sum(amount) > 190)
select sum(p.amount) from my_subquery
join payment p
on my_subquery.customer_id = p.customer_id


/*Ejercicio 49 - Obtén haciendo una subconsulta los amounts de aquellos clientes que se han gastado más de 190€ con WITH*/
with my_subquery as (
select customer_id from payment
group by customer_id 
having sum(amount) > 190)
select count(customer_id) from my_subquery

/*Ejercicio 50 - Obtén el número de veces que un cliente ha alquilado una peli con WITH*/
with subq_inventory as (
	select film_id, inventory_id
	from inventory
),
/* No necesito un WITH por cada definición de with, puedo separarlas por comas*/
subq_rental as (
	select customer_id, rental_id, inventory_id
	from rental
),
subq_film as (
	select film_id, title
	from film
)
select subqf.title, c.customer_id, c.first_name, c.last_name, count(subqr.rental_id) as rental_count
from customer c
join subq_rental subqr /*Los alias en join no se pasan con AS sino simplemente con un espacio*/
	on c.customer_id = subqr.customer_id
join subq_inventory subqi
	on subqr.inventory_id = subqi.inventory_id
join subq_film subqf
on subqi.film_id = subqf.film_id
group by subqf.title, c.customer_id
order by rental_count desc;

/*Ejercicio 51 - Obtén el número de veces que un cliente ha alquilado una peli en 2005 y 2006 con WITH*/
with subq_inventory as (
	select film_id, inventory_id
	from inventory
),
subq_rental as (
	select customer_id, rental_id, inventory_id, rental_date
	from rental
),
subq_film as (
	select film_id, title
	from film
)
select subqf.title, c.customer_id, c.first_name, c.last_name, count(subqr.rental_id) as rental_count, extract(year from subqr.rental_date) as rental_year
from customer c
join subq_rental subqr
	on c.customer_id = subqr.customer_id
join subq_inventory subqi
	on subqr.inventory_id = subqi.inventory_id
join subq_film subqf
on subqi.film_id = subqf.film_id
group by subqf.title, c.customer_id, extract(year from subqr.rental_date) /*No sé por qué en el group by y having no me deja usar el alias rental_year*/
having extract(year from subqr.rental_date) in (2005, 2006)
order by rental_count desc;
