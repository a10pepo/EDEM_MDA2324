-- EJERCICIO_01
-- ¿qué porcentaje supone el coste de alquiler sobre el coste de reemplazar? 
-- Ofrece un resultado redondeado a 2 decimales y renombra la columna
select title,
	rental_rate,
	replacement_cost,
	round ((rental_rate / replacement_cost) * 100, 2) as Nombre1
from public.film;
-- EJERCICIO_02
-- ¿Cuántas veces tienen que alquilar cada película para igualar o superar el coste de reemplazar la película?
-- Da un resultado entero y renombra la nueva columna.
select title,
	rental_rate,
	replacement_cost,
	ceiling (replacement_cost / rental_rate) as Rentable
from public.film;
-- ejercicio 03
-- Incluye en todas tus queries un alias a la tabla y renombre la columna "title" por "título"
-- ¿Cuántas películas disponibles hay?
-- ¿Cuál es la elícula a alquilar más cara? ¿Y la más barata? ¿Cuál es el precio medio de alquiler? ¿Qué variabilidad de precios tenemos?
-- ¿Cuál es el coste más pequeño de reemplazo? ¿Cual es el más grande?
select
	count(title) as título,
	max(rental_rate) as precio_más_alto,
	min(rental_rate) as precio_más_bajo,
	avg(rental_rate) as precio_medio,
	stddev(rental_rate) as variabilidad_precios,
	min(replacement_cost) as reempalzo_más_bajo,
	max(replacement_cost) as reemplazo_más_alto
from public.film;
-- ejercicio 04
-- ¿Cómo se llaman los actores que empiezan por la letra A?
-- ¿Cuales son las películas que podemos alquilar por más de 10€?
-- ¿Cuántas películas podemos alquilar entre 5 y 10 euros?
-- ¿Cuántas películas podemos alquilar por menos de 5€ y con una duración menor a 100 minutos?
-- Lista todas las duraciones (lo hemos hecho para saber si está en minutos)
select
	first_name
from public.actor
where first_name like 'A%';
select
	title
	from public.film
where rental_rate > 10;
select count (title)
from public.film
where rental_rate > 5 and rental_rate < 10;
select count (title)
from public.film
where rental_rate < 5 and length < 100;
select
	length
from public.film;
-- ¿Qué precio de alquiler tienen las siguientes películas? "Giant Troopers" "Gilbert Pelican" "Gilmore Boiled"
-- ¿Qué rating tiene la película Ali Forever? ¿Cuánta es su duración?
-- ¿Nos falta por informar algún precio de alquiler en nuestra base de datos?
select
	title,
	rental_rate 
from public.film
where title in ('Giant Troopers', 'Gilbert Pelican', 'Gilmore Boiled');
select
	rating
from public.film
where title in ('Ali Forever');
select
	title
from public.film
where rental_rate is null;
-- El responsable de tienda está interesado en conocer mejor las películas que tienen en tienda.
-- Desea obtener un listado de las películas por orden de duración (de menos duración a más duración)
-- Quiere conocer los títulos de las 5 películas más cortas del videoclub
select
	title,
	length
from public.film
order by length asc
limit 5;
-- EJERCIO_06
-- Obten por ‘rating’:
-- El número de películas
-- El precio medio de alquiler
-- El mínimo precio de alquiler
-- El máximo precio de alquiler
-- La duración media de las películas
-- El año de la película más antigua
-- El año de la película más nueva
select
	rating,
count(*) as number,
avg(rental_rate) as precio_medio,
min(rental_rate) as precio_minimo,
max(rental_rate) as precio_maximo,
avg(length) as duración,
min(extract(year from last_update)) as año_viejo,
max(extract(year from last_update)) as año_nuevo
from public.film
group by rating;
-- voy a comprobar tooodas las columnas
select *  
	from public.film;
-- EJERCICIO_07
-- Obten por ‘rating’:
-- El número de películas y quédate únicamente con aquellos rating que tengan más de 200 películas

select
	rating,
	count(*) as number
from public.film
group by rating
having count(rating) > 200;

-- El precio medio de alquiler y quédate únicamente con aquellos rating que tenga un precio medio superior a 3
select
	rating,
	avg(rental_rate)
from public.film
group by rating 
having avg(rental_rate) > 3;
-- La duración media de las películas y quédate con aquellos rating que tengan una duración media mayor a 115 minutos
select
	rating,
	avg(length)
from public.film
group by rating 
having avg(length) > 115;

-- Obtén las direcciones de aquellos clientes de nuestro videoclub
SELECT a.customer_id,
       b.address,
       c.city,
       d.country
FROM customer a
LEFT JOIN address b ON a.address_id = b.address_id
LEFT JOIN city c ON b.city_id = c.city_id
LEFT JOIN country d ON c.country_id = d.country_id;

-- Para poner el formato bonito, vamos a sqlformat.org y lo copiamos, y volvemos y lo pegamos que mola más.

-- Obtén solamente las películas que tienen un actor que tenga un apellido que empiece por la letra "C"
SELECT a.title,
       c.first_name
FROM film a
LEFT JOIN film_actor b ON a.film_id = b.film_id
LEFT JOIN actor c ON b.actor_id = c.actor_id
WHERE c.first_name like 'C%';

-- ¿Cuántos actores tiene cada película?
select
	a.title,
count(actor_id) as number
from film a
left join film_actor b on a.film_id = b.film_id
group by a.title;
-- ¿Cuáles son las películas que tienen más de 2 actores?
select
	a.title,
count(actor_id) as number
from film a
left join film_actor b on a.film_id = b.film_id
group by a.title
having count(actor_id) > 2;
-- ¿Cual es la película que tiene más actores?
select
	a.title,
count(actor_id) as number
from film a
left join film_actor b on a.film_id = b.film_id
group by a.title
order by count(actor_id) desc
limit 1;

-- crear una tabla - Desde el videoclub estamos empezando a guardar las opiniones de los clientes referentes a una película.
-- Esta información queremos guardarla en base de datos para que podamos analizarla:
-- film_id
-- customer_id
-- review_date
-- review_description
--Llama a esta tabla “reviews” seguido de la inicial de tu nombre y tu apellido. Por
--ejemlpo, reviews_ng sería el nombre que le daría.(natalia garcia)
CREATE TABLE if not exists reviews_fc (
film_id int2 NOT NULL,
customer_id int2 NOT NULL,
review_date date NOT NULL,
review_description varchar,
primary key (film_id)
);

-- Inserta la opinión del cliente en la tabla nueva que hemos creado
-- Película con ID = 4, el cliente con ID = 7 ha dicho que “La película es un poco aburrida” y lo ha dicho hoy, 10-11-2023

insert into reviews_fc (film_id, customer_id, review_date, review_description)
values (4, 7, '10-11-2023', 'La película es una caca de vaca');

select film_id, customer_id,review_date,review_description
from reviews_fc

-- Hacerle un UPDATE a Blockbuster
update reviews_jj 
set review_description = 'La película es peor que Piratas del Caribe, pero Piratas del Caribe no está mal'
where review_description = 'te lo cambio jaja pringui'

-- ver tabla de jesus
select film_id, customer_id,review_date,review_description
from reviews_jj

-- borrar la tabla
delete from reviews_jj
where customer_id = 6;

-- ver tabla de jesus
select *
from reviews_fc;

--- renombrar una columna
ALTER TABLE reviews_fc
RENAME COLUMN new_column_name
TO mi_columnita;

-- cambiar tipo de columna
ALTER TABLE reviews_fc
ALTER COLUMN clientes_de_mierda TYPE VARCHAR;

-- borrar tabla
drop table reviews_jj;

-- crear una vista
CREATE VIEW vista_01 AS
SELECT *
FROM film;

-- ver la vista
select *
from vista_01;

-- subconsulta de todos los nombres que tengan apellido que empiece por C
SELECT actor_id, first_name, last_name, last_update
FROM public.actor
where first_name in (select first_name from
public.actor where last_name like 'C%');

-- probar la subconsulta suelta para saber qué nos da
select first_name from
public.actor where last_name like 'C%';

-- subconsulta de una condición de idioma y que sea en inglés
select title, language_id
from public.film
where title in (select title from public.film where language_id = 1)

-- vemos la tabla para saber a que ID le pertenece el inglés
select *
from public.language

-- solución de Natalia
select * from film f
where language_id in (select language_id from
"language" l where l."name" = 'English')


-- obtener con subconsulta todos aquellos clientes que viven en una dirección que empieza por A
select first_name, last_name
from public.customer
where customer_id in (select address_id from address where address like '%A%')

-- obtener con subconsulta todos aquellos clientes que han gastado más de 190€

