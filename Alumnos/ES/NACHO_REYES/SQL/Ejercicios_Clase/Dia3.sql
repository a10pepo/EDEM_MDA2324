-- SUBCONSULTAS

select title, language_id 
from film f
where language_id in (select language_id
from language l
where l."name"::text = 'English')


select title, language_id 
from film f
where language_id in (
select language_id
from language l
where l.language_id = '1')

select first_name, last_name
from customer
where address_id in (
					select address_id
					from address
					where address like '1%')
					
select first_name, last_name
from customer
where customer_id  in (
					select customer_id 
					from payment
					group by customer_id
					having sum(amount) > 190)
					
select sum(amount) as suma_top4
from payment
where customer_id  in (
					select customer_id 
					from payment
					group by customer_id
					having sum(amount) > 190)

-- SUBCONSULTAS CON WITH
					
with my_sub as
	(select customer_id 
 	from payment
 	group by customer_id
 	having sum(amount) > 190)
select sum(amount) as suma_top4
from payment p, my_sub ms
where p.customer_id = ms.customer_id

with my_sub as
	(select customer_id 
 	from payment
 	group by customer_id
 	having sum(amount) > 190)
select count(customer_id) as numero_clientes
from my_sub


select f.film_id 
from inventory i, film f, rental r, customer c
where f.film_id = i.film_id and r.inventory_id = i.inventory_id and 



select film_id 
from film

select *
from rental


with sub1 as
(select customer_id, count(rental_id) as numero_pelis
from rental
group by customer_id, rental_id)
select c.first_name, c.last_name, numero_pelis
from customer c, sub1
where c.customer_id = sub1.customer_id

select count(inventory_id), customer_id as numero_pelis
from rental
group by customer_id
order by count(inventory_id) desc

(select customer_id, count(rental_id) as numero_pelis
from rental
group by customer_id, rental_id)

with sub1 as
(select r.customer_id , count(r.rental_id) as numero_veces_alquilada, f.film_id
from rental r, inventory i, film f
where f.film_id = i.film_id and r.inventory_id = i.inventory_id
group by r.customer_id, f.film_id)
select c.first_name, c.last_name, f.title, s1.numero_veces_alquilada
from customer c, sub1 s1, film f
where s1.customer_id = s1.customer_id and s1.film_id = f.film_id
order by numero_veces_alquilada desc


with sub1 as
(select r.customer_id , count(r.rental_id) as numero_veces_alquilada, f.film_id, extract(year from rental_date) as year_rental_date
from rental r, inventory i, film f
where f.film_id = i.film_id and r.inventory_id = i.inventory_id
group by 1, 3, 4)
select c.first_name, c.last_name, f.title, s1.numero_veces_alquilada, s1.year_rental_date
from customer c, sub1 s1, film f
where s1.customer_id = s1.customer_id and s1.film_id = f.film_id
order by numero_veces_alquilada desc