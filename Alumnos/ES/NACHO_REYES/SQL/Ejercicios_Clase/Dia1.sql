-- EJERCICIO 1
select title, 
rental_rate, 
replacement_cost,
concat(round((rental_rate / replacement_cost)*100,2), '%') as porcentaje
from public.film f;

-- EJERCICIO 2
select title, 
rental_rate, 
replacement_cost,
floor((replacement_cost/rental_rate)) as numero_veces
from public.film f;

-- EJERCICIO 3
select COUNT(title)
from public.film f; 

-- EJERCICIO 4
select title, rental_rate  
from public.film
order by rental_rate DESC;

-- EJERCICIO 4
select max(rental_rate) 
from public.film;

-- EJERCICIO 5
select title, rental_rate  
from public.film
order by rental_rate ASC;

-- EJERCICIO 6
select avg(rental_rate) as precio_medio  
from public.film;

-- EJERCICIO 7
select distinct (rental_rate) as precios_distintos  
from public.film
order by precios_distintos desc;

-- EJERCICIO 7
select stddev(rental_rate) as variabilidad  
from public.film;

-- EJERCICIO 8
select title, replacement_cost  
from public.film
where title = 'Academy Dinosaur'
order by replacement_cost DESC;

-- EJERCICIO 9
select title, replacement_cost  
from public.film
order by replacement_cost ASC;

select *
from public.film f 
where title = 'Academy Dinosaur';

select title, rental_rate 
from public.film f 
where rental_rate < 5;

select title, rental_rate 
from public.film f 
where rental_rate between 2 and 5;

select *
from public.film f 
where title not in ('Titanic', 'Casablanca');

-- EJERCICIO 1
select first_name, last_name
from actor a 
where first_name like 'A%';

-- EJERCICIO 2
select title, rental_rate 
from film f  
where rental_rate > 4;

-- EJERCICIO 3
select title, rental_rate 
from film f 
where rental_rate between 2 and 3;

-- EJERCICIO 4
select title, rental_rate, f.length  
from film f 
where rental_rate < 5 and length < 100;

-- EJERCICIO 5
select *
from film f 
where title in ('Giant Troopers', 'Gilbert Pelican', 'Gilmore Boiled')

-- EJERCICIO 6 
select title, rating, length  
from film f 
where title = 'Ali Forever'

-- EJERCICIO 7
select title, rental_rate
from film f 
where rental_rate is null; 

-- EJERCICIO X
select length(f.length::varchar)  
from film f 
where title = 'Ali Forever'

-- EJERCICIO 8
select title, length
from film f 
order by length asc
limit 5;

-- EJERCICIO 9
select title, length, rental_rate, round((rental_rate  / length),7) as coste_por_minuto
from film f
order by coste_por_minuto DESC;

-- EJERCICIO 10
select title, rental_rate, release_year 
from film f 
where rental_rate < 3
order by release_year desc
limit 10;

-- GROUP BY
select rating, count(title) as numero_pelis, round(avg(rental_rate),2) as precio_medio, max(rental_rate) as max_precio, 
min(rental_rate) as min_precio, round(avg(length),2) as dur_media, min(release_year) as peli_mas_antigua, 
max(release_year) as peli_mas_nueva
from film f 
group by rating;

select rating, count(title) as numero_pelis
from film f 
where title not in ('Adaptation Holes', 'Affair Prejudice', 'African Egg')
group by rating 
having count(title) > 200 and avg(rental_rate) > 3; 

select rating, count(title) as numero_pelis
from film f
group by 1
having count(title) > 200 and avg(rental_rate) > 3; 

select rating, avg(rental_rate) as precio_medio
from film f 
group by rating;

select rating, max(rental_rate)
from film f 
group by rating;

select rating, min(rental_rate)
from film f 
group by rating;

select rating, avg(length)
from film f 
group by rating;

select rating, min(release_year)
from film f 
group by rating;

select rating, max(release_year)
from film f 
group by rating;