-- PRIMEROS EJERCICIOS --

-- Ejercicio 1. Porcentaje alquiler sobre repuesto. 
select title, concat(round(100*rental_rate/replacement_cost, 2)::varchar,'%') as rent_replacement 
from public.film f  
;
-- Ejercicio 2. Tasa de repuesto (break-even)
select f.title, ceiling(f.replacement_cost/f.rental_rate) as tasa_repuesto, f.replacement_cost/f.rental_rate as valor
from film f 
;
-- Ejercicio 3. Cuántas películas hay disponibles?
select count(f.title) as peliculas 
from film f 
;
-- Ejercicio 4. Cuál es el precio más caro?
select max(rental_rate) as precio_maximo 
from film f 
;
-- Ejercicio 5. Precio mínimo?
select min(rental_rate) as precio_min 
from film f 
;
-- Ejercicio 6. Precio medio?
select avg(rental_rate) as avg_price 
from film f 
;
-- Ejercicio 7. Desviación típica?
select stddev(rental_rate) as stdev 
from film f 
;
-- CLÁUSULAS WHERE -- 

-- Todos los datos de la película Academy Dinosaur
select * 
from public.film f 
where title = 'Academy Dinosaur'
;
--Muestra todas las películas que cueste menos de 5€
select title , rental_rate 
from public.film f 
where rental_rate < 5
;
-- OR AND BETWEEN: where columnName between x and y
select title , rental_rate 
from public.film f 
where rental_rate > 1 or title = 'Academy Dinosaur'
;
-- NOT IN ; IN. Cuando el valor esté en la tupla (x,y,z,...) 
select title
from public.film f 	
where title not in ('Academy Dinosaur', 'Wrath Mile')
;

-- NULL values
/* select nombre_cliente
 * from cliente
 * where calle_cliente is/is not null*/

-- MÁS EJERCICIOS --

-- Ejercicio 8. Actores que empiezan por la letra A (ilike no distingue caps)
select first_name, last_name 
from public.actor a 
where a.first_name ilike 'A%' 
;
-- Ejercicio 9. Cuáles son las películas de más de 10€
select title, rental_rate
from public.film f 
where rental_rate > 4
;
-- Ejercicio 10. Cuántas películas entre 3 y 4
select f.title, f.rental_rate
from public.film f 
where rental_rate between 2 and 4
;

-- Ejercicio 11. Qué precio tienen giant troopers, gilbert pelican y gilmore boiled?
select f.title, f.rental_rate 
from public.film f 
where f.title in ('Giant Troopers', 'Gilbert Pelican', 'Gilmore Boiled')
;

-- Ejercicio 12. Rating: Ali Forever -- duración
select f.rating, concat(f.length,' min.')
from public.film f 
where title = 'Ali Forever'
;

-- Ejercicio 13. Is there any null price in films?
select title, rental_rate
from public.film f 
where rental_rate is not null 
;

-- ORDER BY :: Órdenes
select *
from public.film f  
order by title, release_year, rental_rate ;
--limit 10;

-- Listado películas por orden de duración - a +
select title , length
from public.film f 
order by length asc 
;

-- 5 películas más cortas
select title, length
from public.film f 
order by length asc 
limit 5;

-- Película minuto más caro 
select title , concat(length,' min.') , rental_rate, concat(round((rental_rate/length),2),'€ per min.') as pricepermin
from public.film f 
order by pricepermin desc
;

-- 10 Películas más antiguas precio < 3
select title , release_year, rental_rate
from public.film f 
where rental_rate < 3
order by rental_rate 
limit 10;

-- Películas precio inferior a 3
select title 
from public.film f 
where rental_rate < 3
;
-- group by rating - number 
select rating , count(f.title) as number_Films, concat(round(avg(f.rental_rate),2),'€') as avg_price, min(f.rental_rate), max(f.rental_rate), avg(f.length) as avg_length, min(release_year) as oldest,max(release_year) as newest
from public.film f 
group by rating 
;
-- Dejar solo una de rating>200 y precio >3
select rating , count(f.title) as number_Films, concat(round(avg(f.rental_rate),2),'€') as avg_price, min(f.rental_rate), max(f.rental_rate), avg(f.length) as avg_length, min(release_year) as oldest,max(release_year) as newest
from public.film f 
group by rating 
having count(f.title) > 200 and avg(f.rental_rate) > 3;

-- Ahora añadir un where
select f.rating , count(f.title) as number_Films, concat(round(avg(f.rental_rate),2),'€') as avg_price, min(f.rental_rate), max(f.rental_rate), concat(round(avg(f.length)),' min.') as avg_length, min(release_year) as oldest,max(release_year) as newest
from public.film f 
where rental_rate > 3
group by f.rating 
having count(f.title) > 60 ;

-- EJERCICIOS --
-- Obten por rating: 
-- 1) El número de películas y quedarse con los que tengan más de 200
select f.rating, count(f.title) as number_films
from public.film f 
group by f.rating 
having count(f.title) > 200;
-- 2) El precio medio de alquiler y únicamente con avgprics between 1 y 3
select f.rating, avg(rental_rate) as avg_price
from public.film f 
group by f.rating
having avg(rental_rate) between 1 and 3;
-- 3) La duración media de las películas con rating 115<length<200
select f.rating, avg(f.length)
from public.film f 
group by f.rating 
having avg(f.length) between 115 and 200;

-- 4) Únicamente los rating que empiecen por 'P'
select f.rating::varchar
from public.film f
where f.rating::varchar ilike 'P%'
group by f.rating ;

-- CLÁUSULAS JOIN -- 

-- Obtenemos todos los clientes, sus direcciones, país y ciudad.

select c.first_name, c.last_name, c3.country, c2.city, a.address
from public.customer c
left join public.address a
on c.address_id = a.address_id 
left join public.city c2 
on a.city_id = c2.city_id 
left join public.country c3 
on c2.country_id = c3.country_id ;

-- Agrupar clientes por país 

select count(a.address_id) as number_customers, c3.country
from public.address a 
left join public.city c2 
on a.city_id = c2.city_id 
left join public.country c3 
on c2.country_id = c3.country_id 
group by c3.country
;

-- Agrupar clientes por ciudad

select count(a.address_id) as number_customers, c2.city 
from public.address a 
left join public.city c2 
on a.city_id = c2.city_id 
group by c2.city
;

-- NATALIA preguntar

select c.first_name, c.last_name, a.address, c3.country, c2.city
from public.costumer c
inner join public.city c2 
on c.address_id = a.address_id;

-- Obtén solamente las películas que tienen un actor que tenga un apellido que empiece por la letra C
select f.title
from public.film f 
left join public.film_actor fa
on f.film_id = fa.film_id
left join public.actor a  
on fa.actor_id = a.actor_id 
where a.first_name ilike 'C%';

-- Cuántos actores tiene cada película?
select f.title, count(fa.actor_id) as actors_number
from public.film f
left join public.film_actor fa 
on f.film_id = fa.film_id 
group by f.title ;

-- Cuáles son las películas que tienen más de 2 actores?
select f.title, count(fa.actor_id) as actors_number
from public.film f
left join public.film_actor fa 
on f.film_id = fa.film_id 
group by f.title
having count(fa.actor_id)>2;

-- Cuál es la película con más actores?
select f.title, count(fa.actor_id) as actors_number
from public.film f
left join public.film_actor fa 
on f.film_id = fa.film_id 
group by 1
order by 2 desc
limit 10;


-- CREATE TABLE
create table if not exists reviews_pgarcia (
	film_id int2 not null,
	customer_id int2 not null,
	review_date date not null,
	new_rating varchar(50) not null,
	constraint reviews_pgarcia_pkey primary key (film_id)
	);

-- INSERT DATA INTO TABLE
insert into reviews_ls (film_id, customer_id, review_date, review_description)
values (1644,2,2023,'cómo se dice divorcio en árabe?')

;
select *
from reviews_jorgeredbull rj 
;
-- Cambiar valor de una celda.
update reviews_jorgeredbull rj
set review_description = 'josé mota mi ídolo'
where film_id = 10 and customer_id = 2
;
select * 
from reviews_ls 

-- Alterar tablas
alter table reviews_ls 
alter column review_description type varchar(50);

-- Borrar una columna y renombrar.
alter table reviews_ines 
drop column review_description;

alter table reviews_ines_soler 
rename column customer_id
to antonio_lobato_es_mi_padre;

select * 
from reviews_pgarcia rp  ;

-- Borrar una review:
delete 
from reviews_pgarcia 
where fumador_social = 'Muy mala la peli.';

delete 
from reviews_pgarcia 
where film_id in (168,164);

-- Borrar una tabla 
drop table reviews_pgarcia  ;

--  VISTAS  --
create view ten_films_with_most_actors as (
select f.title, count(fa.actor_id) as actors_number
from public.film f
left join public.film_actor fa 
on f.film_id = fa.film_id 
group by 1
order by 2 desc
limit 10);

-- SUBCONSULTAS EN WHERE
select f.title
from public.film f 
where language_id in (select language_id from language l
where l.name ilike 'English%');

/* Obtén haciendo una subconsulta en la cláusula where, 
 * todos aquellos clientes que viven en una dirección que empieza por A */
SELECT    c.first_name,
          c.last_name,
          a.address
FROM      PUBLIC.customer c
LEFT JOIN PUBLIC.address a
ON        c.address_id = a.address_id
WHERE     c.address_id IN
          (
                 SELECT a.address_id
                 FROM   PUBLIC.address a
                 WHERE  a.address ilike '155%')

/* Obtén haciendo una subconsulta en la cláusula where, aquellos clientes que han gastado más de 190€ */

SELECT 	  c.first_name, 
	   	  c.last_name, 
	   	  sum(p2.amount)
FROM 	  public.customer c 
LEFT JOIN public.payment p2 
ON 		  c.customer_id = p2.customer_id 
WHERE 	  c.customer_id IN 
		  (
		  		  SELECT   p2.customer_id 
		  		  FROM public.payment p2  
				  WHERE sum(p2.amount) > 190)
GROUP BY (;



SELECT first_name,
       last_name
FROM   customer c
WHERE  customer_id IN (SELECT customer_id
                       FROM   payment p
                       GROUP  BY customer_id
                       HAVING Sum(amount) = (SELECT Sum(amount)
                                             FROM   payment p
                                             GROUP  BY customer_id
                                             ORDER  BY Sum(amount) DESC
                                             LIMIT  1)) ;
                                            
-- SUBCONSULTAS CON CLÁUSULA WITH --
-- La suma de los clientes que han gastado más de 190€                             
WITH my_sub_query
     AS (SELECT c.first_name,
                c.last_name,
                Sum(p.amount)
         FROM   PUBLIC.customer c
                LEFT JOIN PUBLIC.payment p
                       ON c.customer_id = p.customer_id
         GROUP  BY c.customer_id
         HAVING Sum(p.amount) > 190)
SELECT *
FROM   my_sub_query
WHERE  first_name = 'Karl' 

;

-- El número de clientes que han pagado más de 190€
WITH my_sub_query
     AS (SELECT c.first_name,
                c.last_name,
                Sum(p.amount)
         FROM   PUBLIC.customer c
                LEFT JOIN PUBLIC.payment p
                       ON c.customer_id = p.customer_id
         GROUP  BY c.customer_id
         HAVING Sum(p.amount) > 190)
SELECT Count(first_name), 
FROM   my_sub_query ;

-- El número de veces que un cliente ha alquilado una película:
-- cuántos pedidos cada cliente
WITH my_sub_query
     AS (SELECT c.customer_id,
     			c.first_name,
     			c.last_name,
                f.title
         FROM   PUBLIC.customer c
                LEFT JOIN PUBLIC.rental r
                       ON c.customer_id = r.customer_id
                LEFT JOIN PUBLIC.inventory i
                       ON r.inventory_id = i.inventory_id
                LEFT JOIN PUBLIC.film f
                       ON i.film_id = f.film_id
         order by title)
select customer_id, first_name, last_name, title
from my_sub_query
order by customer_id, title;


SELECT count(c.customer_id),
                f.title
         FROM   PUBLIC.customer c
                LEFT JOIN PUBLIC.rental r
                       ON c.customer_id = r.customer_id
                LEFT JOIN PUBLIC.inventory i
                       ON r.inventory_id = i.inventory_id
                LEFT JOIN PUBLIC.film f
                       ON i.film_id = f.film_id
		 where c.customer_id = 222
		 group by title;
		
		
WITH rental_counts AS (
    SELECT
        c.customer_id,
        c.first_name,
        c.last_name,
        f.title,
        COUNT(*) AS rental_count
    FROM
        PUBLIC.customer c
        LEFT JOIN PUBLIC.rental r ON c.customer_id = r.customer_id
        LEFT JOIN PUBLIC.inventory i ON r.inventory_id = i.inventory_id
        LEFT JOIN PUBLIC.film f ON i.film_id = f.film_id
    GROUP BY
        c.customer_id,
        c.first_name,
        c.last_name,
        f.title
)
SELECT
    first_name,
    last_name,
    title,
    COALESCE(rental_count, 0) AS rental_count
FROM
    rental_counts
ORDER BY
    customer_id,
    title;




                                            
					