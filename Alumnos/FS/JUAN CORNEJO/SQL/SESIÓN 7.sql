-- POSGRES

-- 1º EJERCICIO - Columna calculada y renombrada
select title,rental_rate,replacement_cost, CONCAT(ROUND((rental_rate / replacement_cost) * 100, 2), '%') as Margen
from public.film;
-- OJO, el hecho de hacer un CONCAT convierte el número a string, por lo que no se podría hacer una media.
-- Cada ; marca el final de la sentencia y solo se ejecutará el script previo a ese ;

-- 2º EJERCICIO - ¿Cuantas veces hay que alquilarlas para hacerla rentable?
select title,rental_rate,replacement_cost,CEIL((replacement_cost / rental_rate)) as Veces_para_rentabilizar
from public.film;
--CEIL - Redonde hacia arriba

-- ¿Cuantas peliculas hay disponibles?
select count(distinct (title))
from public.film;

-- ¿Pelicula más cara y más barata en alquiler?
select max(rental_rate), min (rental_rate)
from public.film;

-- ¿Remplazo más caro y más barato?
select max (replacement_cost), min (replacement_cost)
from public.film;

-- Media alquiler
select round(avg(rental_rate),2)
from public.film;

-- Variabilidad
select round(stddev(rental_rate),2)
from public.film;

-- Coste más pequeño de remplazo
select min (replacement_cost)
from public.film;

-- Clausula WHERE especifica condicionales y siempre va después de FROM
-- WHERE columName BETWEEN numero_1 and numero_2
-- Las varibles o alias no se guardan ni almacenan. Han de ser definidos o escritos en cada script o query.
-- LIKE que empiece por. El %, si va a los dos lados, es que tenga esa palabra. El % indica a partir de donde iría el resto de cadena de texto.
-- WHERE columnName in/not in ("Titanic","Casablanca")
-- WHERE siempre va antes que GROUP BY


-- ¿Cómo se llaman los acotres que empiezan por la letra A?
select first_name 
from actor
where first_name like 'A%';

-- ¿Peliculas que podemos alquilar por más de 10€?
select title 
from film
where rental_rate >= 10;

-- ¿Cuantas peliculas podemos alquilar entre 5 y 10 euros?
select title 
from film
where rental_rate between 5 and 10;

-- ¿Cuantas peliculas menor de 5€ y duración menor de 100 mins?
select title 
from film
where rental_rate <5 and length <100;

-- ¿Qué precio de alquiler tienen estas peliculas?
select rental_rate, title
from film
where title in ('Giant Troopers','Gilbert Pelican','Gilmore Boiled');


-- ¿Qué rating tiene la película "Ali Forever"?¿Cuál es su duración?
select title,rating,length as duracion
from film
where title in ('Ali Forever');

-- ¿Nos falta por informar algún precio de alquiler en nuestra base de datos?
select title,rental_rate 
from film
where rental_rate is null;

-- Primero WHERE y despúes ORDER | SELECT * DEVUELVE TODAS LAS COLUMNAS
-- ORDER BY Column1, Column2... ColumnN DESC | ASC limit 10

-- Desea obtener un listado de las peliculas por orden de duración (de menos duración a más duración)

select title,length 
from film
order by length asc; 

-- Listado de 5 peliculas más cortas

select title,length 
from film
order by length asc
limit 5;

-- Clausula GROUP BY
-- EXTRACT para extraer fechas/mins/ de un valor fecha
-- Agrupar por numero de peliculas
select rating, count(title)
from film
group by rating;

-- Agrupar por precio medio del aquiler
select rating, round(avg(rental_rate),2)
from film
group by rating;

-- Agrupar por precio minimo de alquiler
select rating, min(rental_rate)
from film
group by rating;

-- Agrupar por precio máximo de alquiler
select rating, max(rental_rate)
from film
group by rating;

-- Agrupar por duración media
select rating, round(avg(length)) as duracion_en_minutos
from film
group by rating;

-- Pelicula más antigua
select rating, min (release_year)
from film
group by rating;

-- Pelicula más antigua
select rating, max (release_year)
from film
group by rating;

-- Pelicula más antigua fecha
select rating, min (extract(year from last_update))
from film
group by rating;

-- Pelicula más antigua
select rating, max (extract(year from last_update))
from film
group by rating;

-- Where sirve para tablas reales. Having es para filtrar ya en la tabla de resultados pero no en la tabla real.
-- HAVING es mas pesado que WHERE porque en WHERE las operaciones ya han sido previamente filtrados y en HAVING no (primero se hace la operación y después filtra)

-- Ratings con más de +200 peliculas
select rating, count(distinct (title)) as conteo
from film
group by rating
having count(distinct (title)) >= 200;


-- Ratings con precio medio de alquiler superior a 3
select rating, round( avg(rental_rate),2)
from film
group by rating
having avg(rental_rate) >= 3;

-- Inner Join sirve para filtrar. Solo te devuelve los resultados que coincidan igual en ambas tablas.

-- SELECT table1.column1, table2.column2
-- FROM table1 
-- AS para renombar columnas, y un espacio para tablas

select (concat(a.first_name,' ',A.last_name)) as full_name  , B.address  as direction, C.city, CO.country
from customer A
left join address B on A.address_id = B.address_id
left join city C on B.city_id = C.city_id
left join country CO on C.country_id = CO.country_id;


-- https://sqlformat.org/ Te sirve para dejar bonito la línea de código.

-- Mismo código tras formateo:
SELECT (concat(a.first_name, ' ', A.last_name)) AS full_name ,
       B.address AS direction,
       C.city,
       CO.country
FROM customer A
LEFT JOIN address B ON A.address_id = B.address_id
LEFT JOIN city C ON B.city_id = C.city_id
LEFT JOIN country CO ON C.country_id = CO.country_id;

-- Obten solamente las peliculas que tienen un actor que tenga un apellido que empiece por la letra C

SELECT distinct (concat(a.first_name, ' ', A.last_name)) AS full_name --, F.title 
FROM film F
LEFT JOIN film_actor FA ON F.film_id  = FA.film_id 
LEFT JOIN actor A ON a.actor_id  = FA.actor_id
WHERE A.first_name  not LIKE 'T%'
--group by (concat(a.first_name, ' ', A.last_name))

--  ¿Cuántos actores tiene cada película?

select F.title , count(FID.actor_id)
from film_actor FID
left join film f on f.film_id = FID.film_id
group by F.film_id
order by count(FID.Actor_id) desc;

-- Siempre que se crea una tabla, se tiene que poner el nombre del esquema.

-- CREATE TABLE

create table public.reviews_jr(
film_id int2 not null,
customer_id int2 not null,
review_date date not null,
review_description varchar);

-- Pelicula ID 4 cliente id 7 "La pelicula es un poco aburrida" "hoy"

insert into reviews_jr (film_id,customer_id,review_date,review_description)
values (4,7,'10-11-2023','La peli era un mondongo, y su actriz la Jackeline también')

-- FEchas en comillas simples

-- UPDATE
update public.reviews_jr
set review_description = 'Comoquieras apareció en la sala y me firmó un autografo'
where review_description = 'La peli era un mondongo, y su actriz la Jackeline también'

-- DELETE
delete 
from public.reviews_jr
where review_description = 'Comoquieras apareció en la sala y me firmó un autografo'

-- RENOMBAR
alter table public.reviews_jc
rename column review_date
to review_date_2;

-- CAMBIAR TIPO COLUMNA
alter table public.reviews_jr 
alter column review_date type varchar;

-- BORRAR TABLA
drop table public.reviews_jr

-- SUBCONSULTAS (Todas las peliculas que están en inglés)
SELECT film.title, 
       (SELECT L.name 
        FROM language L 
        WHERE L.language_id = film.language_id) AS language_name
FROM film
WHERE film.language_id = 1;

-- AQUELLOS CLIENTES QUE VIVEN EN UNA DIRECCIÓN QUE EMPIEZA POR A
SELECT CONCAT(customer.first_name, ' ', customer.last_name) AS full_name,
       (SELECT A.address 
        FROM address A 
        WHERE A.address_id = customer.address_id AND A.address LIKE 'A%' and A.address is not null) AS address
FROM customer