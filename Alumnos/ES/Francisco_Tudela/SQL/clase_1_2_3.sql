
SELECT a.first_name as nombre , a.last_name  as apellido 
FROM actor a

select title, rental_rate, replacement_cost, rental_duration + replacement_cost  as operación
from film f 

select avg(rental_duration)
from film f 

--Ejercicio 1 QUE PORCENTAJE SUPONE EL COSTE DE ALQUILER SOBRE EL COSTE DE REMPLZADO
select title, rental_rate, replacement_cost, concat(round((rental_rate / replacement_cost)*100,2),'%') as resultado_oper
from film f  

--CUANTAS VECES TENGO QUE ALQUILAR UNA PELICULA PARA QUE ME SALGA RENTABLE COMPRAR ESA PELICULA 

select title, rental_rate, replacement_cost, ceil((replacement_cost / rental_rate))  as alquileres_necesarios
from film f 


select count(title) as titulo, 
max(rental_rate) as max_price, 
min(rental_rate) as min_price, 
avg(rental_rate) as avge_precio, 
stddev(rental_rate) as price_variation  
from film f; 

--WHERE

select  *
from  film f 
where title = 'Academy Dinosaur';

select *
from  actor a  
where first_name  iLIKE 'a%';

select title , rental_rate 
from film f 
where f.rental_rate > 4;

select title , rental_rate 
from film f 
where f.rental_rate between 2 and 5;

select title ,rental_rate 
from film f 
where title  ilike 'Gi%'

select title,rating ,length  
from  film f 
where title ilike 'Ali Forever'

select title, rental_rate 
from film f 
where rental_rate  is null 

select title, length 
from film f 
order by length asc 

select title, (rental_rate/ length) as mas_cara
from film f 
order by mas_cara desc
limit(1)

--10 peliculas mas antiguas cuyo precio alquiler no supere los 3 euros
select title, release_year, rental_rate 
from film f
where rental_rate <3
order by release_year desc
limit 10


--GROUP BY
select rating , count(*) film_id,
avg(rental_rate) as precio_medio,
max(rental_rate), 
min(rental_rate), 
avg(length),
min(release_year),
max(release_year)
from film f 
where rental_rate > 2
group by rating 
having count(title)> 100 and avg(f.rental_rate) > 3

--Obtener por rating
select rating ,count(title)
from film f 
group by rating 
having count(title) > 200 

select count(title), rating, avg(rental_rate) 
from film f 
group by rating 
having avg(rental_rate)  between  1 and 3

select rating ,count(title)
from film f 
group by rating 
having count(title) > 200

select count(title), rating , avg(length) 
from  film f 
group by rating 
having avg(length) between  115 and 200 

select distinct rating
from film f 
where rating::text ilike 'P%'

--CLASE 2

select c.first_name , d.address , ct.city , co.country
from customer c 
left join address d on c.address_id = d.address_id
inner join city ct on d.city_id  = ct.city_id
left join country co on ct.country_id  = co.country_id


select distinct  count(cu.first_name), co.country
from customer cu
left join address d on cu.address_id = d.address_id
inner join city ct on d.city_id  = ct.city_id
left join country co on ct.country_id  = co.country_id
group by co.country  

select f.title , ac.first_name , ac.last_name
from film f 
inner join film_actor fa on f.film_id  = fa.film_id
inner join actor ac on fa.actor_id = ac.actor_id
where last_name ilike 'C%'

select f.title , count(fa.actor_id) 
from film f
inner join film_actor fa on f.film_id  = fa.film_id
group by f.title 

select f.title , count(fa.actor_id) 
from film f
inner join film_actor fa on f.film_id  = fa.film_id
group by f.title 
having count(fa.actor_id) > 2


select f.title , count(fa.actor_id) 
from film f
inner join film_actor fa on f.film_id  = fa.film_id
group by 1
order by 2 desc  limit 1


create  table if not exists public.review_tumup (
film_id int2 not null, 
customer_id int2 not null, 
review_data date not null,
review_description varchar(50) not null,
CONSTRAINT review_tumup_pkey PRIMARY key (film_id , customer_id)
)
--CONSTRAINT film_tumup_actor_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customer(customer_id) ON DELETE RESTRICT ON UPDATE CASCADE,
--CONSTRAINT revi_tumup_fkey FOREIGN KEY (film_id) REFERENCES public.film(film_id) ON DELETE RESTRICT ON UPDATE CASCADE


insert into reviews_tonifaura (film_id, id_customer,review_description,review_date)
values (4,7, 'fking papanatas', '2023-11-23');
select * from reviews_tonifaura 

update reviews_tonifaura 
set film_id  =  2
where customer_id = 7

alter table reviews_tonifaura 
rename column customer_id
to id_customer

alter table reviews_tonifaura
ALTER COLUMN film_id TYPE VARCHAR(1000)

alter table reviews_tonifaura 
drop column review_date

--CLASE 3

delete 
from reviews_tonifaura 
where film_id = '3'

drop table reviews_tonifaura

drop table review


create view tumup as 
select distinct  count(cu.first_name), co.country
from customer cu
left join address d on cu.address_id = d.address_id
inner join city ct on d.city_id  = ct.city_id
left join country co on ct.country_id  = co.country_id
group by co.country



select title
from film 
where language_id  in (select language_id  from language l  where name = 'English')


select c.first_name
from customer c
where address_id  in (select address_id  from address a where address like '3%')

select first_name , last_name 
from customer c 
where customer_id in (select customer_id from payment p
group by customer_id 
having sum(amount) > 190)


select first_name , last_name 
from customer c 
where customer_id in (
select customer_id 
from payment p 
group by customer_id 
having sum(amount) = 

(
select  sum(amount)
from payment p 
group by customer_id
order by sum(amount) desc limit 1 
)
)

with top_customers
as (select customer_id,sum(amount) as total_amount
from payment p
group by 1 
having sum(amount) > 190)
select sum(total_amount), count(customer_id)
from top_customers

with n_alquilers as 
(select inventory_id,customer_id, count(rental_id)  as total_alquileres
from rental
group by inventory_id , customer_id
) 
select customer_id,customer_id
from n_alquilers






