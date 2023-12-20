with subq_inventory as (
	select film_id, inventory_id
	from inventory
),
subq_film as (
	select film_id, title
	from film),
subq_rental as(
	select customer_id, rental_id, inventory_id, rental_date
	from rental
)
select subqf.title, c.customer_id, c.first_name, c.last_name, count(subqr.rental_id) as rental_count, extract(year from subqr.rental_date) as rental_year
from customer c
join subq_rental subqr
	on c.customer_id = subqr.customer_id
join subq_inventory subqi
	on subqr.inventory_id = subqi.inventory_id
join subq_film subqf
	on subqi.film_id = subqf.film_id
group by subqf.title, c.customer_id, extract(year from subqr.rental_date)
having extract(year from subqr.rental_date) in (2005, 2006)
order by rental_count desc;