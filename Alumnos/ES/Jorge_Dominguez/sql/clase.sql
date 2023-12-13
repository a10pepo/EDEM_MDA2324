--EJERCICIO 1
select title, rental_rate, replacement_cost, concat(round((rental_rate / replacement_cost) * 100, 2), '%') as percent 
from film f

--EJERCICIO 2
select title, floor(replacement_cost / rental_rate) as recuperaçao
from film f

--EJERCICO 3
select count(title) as counta
from film f

--EJERCICIO 4
select max(rental_rate) as maxim
from film

--EJERCICIO 5
select avg(rental_rate) as media
from film f

--EJERCICIO 6
select stddev(rental_rate) as variacion
from film f

--EJERCICIO 7
select min(replacement_cost) as minimo
from film f

--EJERCICIO 8
select max(replacement_cost) as maximo
from film f

--EJERCICO 9
select *
from actor
where first_name ilike 'a%'

--EJERCICO 10
select count(title)
from film f
where rental_rate > 10

--EJERCICIO 11
select count(title)
from film f
where rental_rate between 5 and 10

--EJERCICIO 11
select count(title)
from film f
where rental_rate < 5 and rental_duration < 100

--EJERCICIO 11
select title, rental_rate
from film f
where title in ('Giant Troopers', 'Gilbert Pelican', 'Gilmore Boiled')

--EJERCICiO 12
select title, rating, length
from film f
where title = 'Ali Forever'

--EJERCICIO 13
select *
from film f
where rental_rate is null

--EJERCICIO 14
select title, description, length
from film f
order by length asc
limit 5

--BORJA CABO MANAGER
select title, description, round((rental_rate/length),4) as caro
from film f
order by caro desc
limit 1

--JULIAN MERINO MANAGER
select title, description, rental_rate, release_year
from film f
where rental_rate < 3
order by release_year asc
limit 10

--EJERCICIO 15
select rating, count(*) as count,
round(avg(rental_rate),2) as avgrate,
round(min(rental_rate),2) as minrate,
round(max(rental_rate),2) as maxrate,
round(avg(length),2) as avglenght,
max(release_year) as maxyear,
min(release_year) as minyear
from film f
where length > 55
group by rating, release_year
having count(title) > 200 and avg(rental_rate) > 3

--EJERCICIO 16
select rating, count(title)
from film
group by rating
having count(title) > 200

select rating, avg(rental_rate)
from film
group by rating
having avg(rental_rate) between 1 and 3 

select rating, avg(length)
from film f
group by rating
having avg(length) between 115 and 200

select distinct (rating)
from film
where rating::text like 'P%' --para convertir la variable en texto

--EJERCICIO 17
select c.first_name, c.last_name, a.district, a.address, ct.city, a.postal_code, co.country
from customer c 
left join address a on c.address_id = a.address_id
left join city ct on a.city_id = ct.city_id 
left join country co on ct.country_id = co.country_id 
order by co.country asc

select co.country, count(co.country)
from country co
left join city ct on co.country_id  = ct.country_id
left join address a on ct.city_id = a.city_id
left join customer c on a.address_id = c.address_id
group by co.country 
order by count(co.country) desc

--EJERCICIO 18
select f.title, a.first_name, a.last_name 
from film f
inner join film_actor fa on f.film_id = fa.film_id 
inner join actor a on fa.actor_id = a.actor_id
where a.last_name ilike 'c%'

select f.title, count(a.actor_id)
from actor a
join film_actor fa on a.actor_id = fa.actor_id
join film f on fa.film_id = f.film_id
group by f.title
order by count(a.actor_id) desc

select f.title, count(a.actor_id)
from actor a
join film_actor fa on a.actor_id = fa.actor_id
join film f on fa.film_id = f.film_id
group by f.title
having count(a.actor_id) > 2

select f.title, count(a.actor_id)
from actor a
join film_actor fa on a.actor_id = fa.actor_id
join film f on fa.film_id = f.film_id
group by f.title
order by count(a.actor_id) desc
limit 1

--TABLAS

create table if not exists public.reviews_jorgeredbull(
film_id int2,
customer_id int2,
review_date date,
review_description varchar(50),
CONSTRAINT jorge_pkey PRIMARY KEY (customer_id, film_id),
CONSTRAINT jorgeredbull_cust_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customer(customer_id) ON DELETE RESTRICT ON UPDATE CASCADE,
CONSTRAINT jorgeredbull_film_id_fkey FOREIGN KEY (film_id) REFERENCES public.film(film_id) ON DELETE RESTRICT ON UPDATE CASCADE
)

insert into TABLA (film_id, customer_id, review_date, descripcion_reseña)
values ('X','X', 'X','X')

update TABLA
set review_description = 'X'
where customer_id = 'X'

alter table TABLA
add VARIABLE varchar(50);

delete 
from reviews_jorgeredbull 
where VARIABLE = 'X'

drop table reviews_jorgeredbull

--EJERCICIO 19 (CLASE 30 NOVIEMBRE)
create view a_jorgeredbull as
select cu.first_name, cu.last_name, cu.email, a.address, ct.city, co.country
from customer cu
join address a on cu.address_id = a.address_id
join city ct on a.city_id = ct.city_id
join country co on ct.country_id = co.country_id
where first_name ilike 'a%'

select title, description
from film f
where language_id in (select language_id from
language l where l.name = 'English')



select first_name, last_name 
from customer cu
where address_id in (select a.address_id from 
address a where a.address like '1%')


select cu.first_name, cu.last_name, cu.customer_id
from customer cu
where cu.customer_id in (
    select py.customer_id
    from payment py
    group by py.customer_id
    having sum(py.amount) > 190
);

select cu.first_name, cu.last_name, sum(py.amount) as total_payment
from customer cu
join payment py on cu.customer_id = py.customer_id
group by cu.customer_id, cu.first_name, cu.last_name
having sum(py.amount) > 190;

select sum(amount) as la_suma
from payment p
where p.customer_id in (
select customer_id 
from payment cu
group by cu.customer_id
having sum(amount) > 190
);

with my_sub_query as (
select customer_id, sum(amount)
from payment
group by customer_id
having sum(amount) > 190
)
select  first_name, last_name
from my_sub_query s
inner join customer cu on s.customer_id = cu.customer_id

with jorgeredbull as (
select customer_id, sum(amount) as amount
from payment cu
group by cu.customer_id
having sum(amount) > 190
)
select sum(amount)
from jorgeredbull s

with numveces as (
select r.customer_id, count(r.rental_id) as counta
from rental r
group by r.customer_id)
select cu.first_name, cu.last_name, nv.counta
from numveces nv
join customer cu on nv.customer_id = cu.customer_id
order by counta desc

with numveces as (
select f.film_id, f.title, count(f.film_id) as counta
from film f
group by f.film_id
)
select cu.first_name, cu.last_name, nv.title, nv.counta
from numveces nv
join inventory inv on nv.film_id = inv.film_id
join rental rt on inv.inventory_id = rt.inventory_id
join customer cu on rt.customer_id = cu.customer_id

 with numveces as ( select
 cu.customer_id, f.film_id, f.title, count(rt.rental_id) as counta
 from customer cu
 join rental rt ON cu.customer_id = rt.customer_id
 join inventory inv ON rt.inventory_id = inv.inventory_id
 join film f ON inv.film_id = f.film_id
 group by cu.customer_id, f.film_id, f.title
)
select cu.first_name, cu.last_name, nv.title, nv.counta
from  numveces nv
join  customer cu on nv.customer_id = cu.customer_id
order by nv.counta desc

with numveces as ( select
 cu.customer_id, f.film_id, f.title, count(rt.rental_id) as counta
 from customer cu
 join rental rt ON cu.customer_id = rt.customer_id
 join inventory inv ON rt.inventory_id = inv.inventory_id
 join film f ON inv.film_id = f.film_id
 where extract(year from rt.rental_date) between 2005 and 2006
 group by cu.customer_id, f.film_id, f.title
)
select cu.first_name, cu.last_name, nv.title, nv.counta
from  numveces nv
join  customer cu on nv.customer_id = cu.customer_id
order by nv.counta desc
