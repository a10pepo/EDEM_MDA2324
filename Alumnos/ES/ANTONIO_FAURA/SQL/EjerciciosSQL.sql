

-- QUE PORCENTAJE SUPONE EL COSTE DE ALQUILER SOBRE EL COSTE DE REMPLAZAR?

select title, rental_rate, replacement_cost, concat(round((rental_rate / replacement_cost)*100,2),'%')  AS coste_alquiler_sobre_compra
from film f


-- CUANTAS VECES TENGO QUE ALQUILAR CADA PELICULA PARA IGUALAR EL COSTE DE REMPLAZAR LA PLEICULA EN NUMEROS ENTEROS

select title, rental_rate, replacement_cost, floor(replacement_cost/rental_rate) AS punto_marginal
from film f
order by punto_marginal desc;


select count(title) as titulo, 
max(rental_rate) as max_price,
min(rental_rate) as min_price,
avg(rental_rate) as avge_precio,
stddev(rental_rate) as price_variation
from film f


select * 
from film f 
where title = 'Academy Dinosaur'


select title
from film f
where rental_rate <5


select *
from actor
where first_name ilike 'a%'


select title
from film
where rental_rate >4

select count(title) as titulo
from film
where rental_rate between 2 and 4


select title, rental_rate
from film f
where title ilike 'gi%'


select title, rating, length
from film f 
where title ilike 'ali forever'


select title, rental_rate
from film f 
where rental_rate is null 


select title, length 
from film f
order by length asc
limit 5


-- pelicula mas cara por minuto de alquilar

select title, (rental_rate / length) as borja
from film f 
order by borja desc
limit 1


-- 10 peliculas mas antiguas, cuyo precio de alquiler sea menor a 3 euros

select title, release_year, rental_rate 
from film f 
where rental_rate <3
order by release_year asc
limit 10


select rating, count(title) as cantidad,
avg(rental_rate) as precio_medio,
min(rental_rate) as precio_minimo,
max(rental_rate) as precio_maximo,
avg(length) as duracion_media,
max(release_year) as older,
min(release_year) as latest
from film f
where duration
group by rating
having count(title) > 200 and avg(rental_rate) > 3


select count(title), rating
from film f 
group by rating
having count(title) > 200


select count(title), rating, avg(rental_rate)
from film f 
group by rating
having avg(rental_rate) between 1 and 3 


select count(title), rating, avg(length) 
from film f 
group by rating
having avg(length) between 115 and 200 


select distinct rating
from film f 
where rating::text ilike 'P%'   --rating::text para pasarlo a texto porque tenemos letra y numero


select c.first_name, c.address_id, a.address, a.city_id, ct.city, ct.country_id, co.country
from customer c
inner join address a on c.address_id = a.address_id
inner join city ct on a.city_id = ct.city_id 
inner join country co on ct.country_id = co.country_id 


select distinct co.country, count(c.first_name)
from customer c 
inner join address a on c.address_id = a.address_id
inner join city ct on a.city_id = ct.city_id 
inner join country co on ct.country_id = co.country_id 
group by co.country
order by count(c.first_name) desc


select title, first_name, last_name
from film f
inner join film_actor fa on f.film_id = fa.film_id
inner join actor act on fa.actor_id =  act.actor_id 
where last_name ilike 'C%'


select distinct f.title, count(a.actor_id)
from actor a 
inner join film_actor fa on a.actor_id = fa.actor_id 
inner join film f on fa.film_id = f.film_id
group by f.film_id 
order by count(a.actor_id) desc


select distinct f.title, count(a.actor_id)
from actor a 
inner join film_actor fa on a.actor_id = fa.actor_id 
inner join film f on fa.film_id = f.film_id
group by f.film_id
having count(a.actor_id) > 2
order by count(a.actor_id) asc


create table public.reviews_tonifaura (
film_id int2 not null,
customer_id int2 not null,
review_date date not null,
review_description varchar(50) not null,
CONSTRAINT reviews_tonifaura_pkey PRIMARY KEY (film_id, customer_id)
)


insert into reviews_pgarcia (film_id, customer_id, review_date, new_rating)
values ('0330', '3300', '2023-11-29', 'tal')


update review_jarupu 
set review_description = 'SUS CRIP CION'
where review_description = 'pero q dices broder'


insert into reviews_jorgeredbull (film_id, customer_id, review_date, review_description)
values ('0330', '3300', '2023-11-29', 'Soy tu PC estoy herido llevame al worten')


-----Aqui descubrí que DBeaver no guarda automaticamente, por lo que la practica de las subconsultas ha desaparecido
--de todas formas, el ejercicio largo está aqui:
--    |
--    |
--    V

--El número de veces que un cliente ha alquilado una película.

with customer_y_rental as (
select c.first_name, c.last_name, r.rental_id
from customer c 
left join rental r on r.customer_id = c.customer_id),
  
rental_e_inventory as (
select r.rental_id, i.inventory_id
from rental r 
left join inventory i on i.inventory_id = r.inventory_id),
  
inventory_y_film as (
select i.inventory_id, f.film_id, f.title
from inventory i 
left join film f on f.film_id = i.film_id)

select cr.first_name, cr.last_name, iyf.title, count(*) as num_rentals
from customer_y_rental cr
left join rental_e_inventory re on cr.rental_id = re.rental_id
left join inventory_y_film iyf on re.inventory_id = iyf.inventory_id
group by cr.first_name, cr.last_name, iyf.title
order by 
num_rentals desc;
