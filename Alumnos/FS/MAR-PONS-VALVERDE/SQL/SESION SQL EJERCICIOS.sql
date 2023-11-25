--EJERCICIO1 
--QUE PORCENTAJE SUPONE EL COSTE DE ALQUILER SOBRE EL COSTE DE REEMPLAZAR. 
--OFRECE UN RESLTADO REDONDEADO A DOS DECIMALES Y RENOMBRA LA COLUMNA. 

select title, 
rental_rate,
replacement_cost, 
ROUND((rental_rate/replacement_cost)*100, 2) as porcentaje_coste_alquier
from public.film 

--si quisiera mostrar el porcentaje pondria CONCAT(ROUND((rental_rate/replacement_cost)*100, 2), '%') as porcentaje_coste_alquier
-- La funcion CONCAT convierte mi función ROUND en un strng, al que luego le añado el % que es otro string.

--EJERCICIO2
--¿CUANTAS VECES TIENE QUE ALQUILAR CADA PELICULA PARA IGUALAR O SUPERAR EL COSTE DE REEMPLAZAR LA PELICULA?
-- DA UN RESULTADO ENTERO Y RENOMBRA LA PELICULA.

select title, 
rental_rate, 
replacement_cost,
CEIL((replacement_cost/rental_rate)) as pelicula_reemplazada
from public.film

--LA FUNCION CEIL ES COMÚN PARA MUCHOS LENGUAJES. AQUI REDONDEA EL ENTERO SUPERIOR. 

--EJERCICIO3
--¿ CUÁNTAS PELICULAS HAY DISPONIBLES?

--select max(film_id) from public.film;
select count((distinct (tittle))
from public.film;

--¿PELICULA MÁS BARATA)

select min(replacement_cost) from public.film;

--PELICULA MAS CARA

select max(replacement_cost) from public.film;

--PRECIO MEDIO DE ALQUILER

select avg(rental_rate) from public.film;

--VARIABILIDAD DE PRECIOS TENEMOS.

select variance(replacement_cost) from public.film;

--COSTE MAS PEQUEÑO DE REEMPLAZO

select min(replacement_cost) from public.film;

--COSTE MAS GRANDE DE REEMPLAZO

select max(replacement_cost) from public.film

--EJERCCICIO4
--PELICULAS A ALQUILAR ENTRE 5 Y 10€.
select title
from film
where rental_rate between 5 and 10;

--PELICULAS A ALQUILAR CON MENOS DE 5€ Y CON DURACION MENOR A 100 MINUTOS.

select title
from film
where rental_rate < 5 and film.length <100;

--QUE PRECIO DE ALQUILER TIENEN LAS SIGUIENTES PELICULAS:
--GIANT TROOPERS, GILBERT PELICAN Y GILMORE BOILED

select rental_rate, film
from film 
where title in ('Giant Troppers', 'Gilbert Pelican','Gilmore Boiled');

--El responsable de tienda esta interesado en conocer mejor las peliculas que tienen en tienda. 
--desea conocer un listado de peliculas por orden de duracion ( de menos duracion a mas duracion)
--quiere conocer los titulos de las 5 peliculas más cortas del videoclub.

select title, length
from film 
order by length asc;

select title, length
from fil m 
order by length asc
limit 5;


--QUE RATING TIENE LA PELICULA 'ALI FOREVER' ¿CUAL ES SU DURACION?

select title, rating, length as duracion
from film 
where title in ('Ali Forever');

-- ¿nos falta por informar algun precio de alquiler en nuestra base de datos?

select title,rental_rate
from film 
where rental_rate is null;

--EJERCICIO GROUP BY
--OBTEN POR RATING:
--Nº DE PELICULAS:
select rating, count(title)
from film 
group by rating;

--PRECIO MEDIO ALQUILER
select rating, avg (rental_rate)
from film 
group by rating; 

--EL MINIMO PRECIO ALQUILER
select rating, min(rental_rate)
from film 
group by rating;

--EL MÁXIMO PRECIO ALQUILER
select rating, max(rental_rate)
from film 
group by rating;

--LA DURACIÓN MEDIA DE LAS PELICULAS
select rating, round(avg (length))
from film
group by rating;


--EL AÑO DE LA PELICULA MÁS ANTIGUA
select rating, min (extract(year from last_update))
from film 
group by rating;

--EL AÑO DE LA PELICULA MÁS NUEVA
select rating, max (extract(year from release_year))
from film 
group by rating

--EJERCICIO HAVING
--OBTENG POR RATING:
--nº de peliculas y quedate únicamente con aquellos rating que tengan más de 200 películas.
select rating, count(title)
from film 
group by rating 
having count(title)>200;

--El precio medio de alquiler y quédate únicamente con aquellos rating que tenga un precio medio superior a 3
select rating, avg(rental_rate)
from film
group by rating 
having avg(rental_rate)>3;

--La duración media de las películas y quédate con aquellos rating que tengan una duración media mayor a 115 minutos
select rating, round(avg(length))
from film 
group by rating 
having round(ag(length)) >115;

--EJERCICIO CREAR TABLA
--Desde el videoclub estamos empezando a guardar las opiniones de los clientes referentes a una película. Esta información queremos guardarla en base de datos
--para que podamos analizarla:
--● film_id
--● customer_id
--● review_date
--● review_description
--Llama a esta tabla “reviews” seguido de la inicial de tu nombre y tu apellido. Por ejemplo, reviews_ng sería el nombre que le daría.

create table public.reviews_MPV(
film_id int2 not null,
customer_id int2 not null,
review_date date not null,
review_description varchar)

--INSERTAR COLUMNAS EN LA TABLA: lo que definimos con varchar va con comillas simples, lo que no es entero no. 

insert into reviews_MPV (film_id, customer_id, review_date,review_description)
values (4,7,'10-11-2023','La película es un poco aburrida')

--ACTUALIZACION DE REGISTROS DE UNA TABLA.

update reviews_cvm 
set review_description = 'La película es bastante divertida y para todo los públicos'
where review_description = 'Cristiano el mejor'


select * --veo mis cambios anteriores con la sentencia .

from reviews_cvm


--borrar algo más.

delete 

--CAMBIAR TABLAS A NIVEL DE COLUMNAS

alter table reviews_acn action;
alter table reviews_acn 
drop column review_descrption

--RENOMBRAR COLUMNA:
alter table reviews_acn 
rename column review_description
to review_opinion;

--AÑADIR UNA COLUMNA

alter table reviews_acn 
add column review_stars varchar;

select *
from reviews_acn ra

--VISTA: guardan una sentencia dentro de otra.

--Crea una vista que se llame como tu nombre y apellidos e introduce 
 --todos los campos que te resulten interesantes de las películas y sus actores.

create view my_view_of_MPV as
select actor_id,first_name,last_name
from public.actor a 
where first_name like'%';

select *
from my_view_of_mpv ;

--existen las vistas materializadas que son vistas que se convierten en un archivo y las no materializadas no se convierten. 
--materializar para ahorrar minutos.

--SUBCONSULTAS: siempre entre paréntesis. ilike=que contenga mayusculas y minusculas. like al contrario.

SELECT actor_id, first_name, last_name, last_update
FROM public.actor
where first_name in (select first_name from public.actor where last_name ilike 'C%')

--Obtén haciendo una subconsulta en la cláusula WHERE, todas aquellas películas que están en el idioma de inglés

select *  
from film 
where language_id in (select language_id from "language" l  where name ='English' )

--Obtén haciendo una subconsulta en la cláusula WHERE, todos aquellos clientes que viven en una dirección que empieza por A
select *
from customer 
where address_id in (select address_id  from address where address like '%A%')--no sale nada poniendo un solo%.




