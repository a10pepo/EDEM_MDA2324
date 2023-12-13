select count(title) as cuenta, rating
from film f 
group by rating 
having count(title) > 200;

select avg(rental_rate), rating 
from film f 
group by rating 
having avg(rental_rate) between 1 and 3

select avg(length), rating 
from film f 
group by rating 
having avg(length) > 115 and avg(length) < 200; 

select f.rating  
from film f 
group by rating
having rating::text like 'P%';

select count(c.first_name) as numero_clientes, c2.country  
from customer c
inner join address a
on c.address_id = a.address_id 
inner join city ct 
on ct.city_id = a.city_id
inner join country c2 
on ct.country_id = c2.country_id
group by c2.country

select count(c.first_name) as numero_clientes, c2.country  
from customer c, address a, city ct, country c2 
where c.address_id = a.address_id and ct.city_id = a.city_id and ct.country_id = c2.country_id
group by c2.country
order by count(c.first_name) desc

select f.title, a.first_name, a.last_name 
from film f, film_actor fa, actor a
where f.film_id = fa.film_id and fa.actor_id = a.actor_id and a.last_name like 'C%'
order by f.title 

select count(a.actor_id) as numero_actores, f.title
from film f, film_actor fa, actor a
where f.film_id = fa.film_id and fa.actor_id = a.actor_id
group by f.title 
order by count(a.first_name) desc 

select count(a.actor_id) as numero_actores, f.title
from film f, film_actor fa, actor a
where f.film_id = fa.film_id and fa.actor_id = a.actor_id
group by f.title 
having (count(a.first_name) > 2)
order by count(a.first_name) desc 

create view view_reyes as 
select count(a.actor_id) as numero_actores, f.title
from film f, film_actor fa, actor a
where f.film_id = fa.film_id and fa.actor_id = a.actor_id
group by f.title 
order by count(a.first_name) desc 
limit 1;

create table reviews_reyes(
	film_id serial4 not null,
	customer_id serial4 not null,
	review_date timestamp not null,
	review_description varchar(50),
	constraint reviews_reyes_filmid_fkey FOREIGN KEY (film_id) references film(film_id),
	constraint reviews_reyes_customerid_fkey FOREIGN KEY (customer_id) references customer(customer_id)
	ON DELETE RESTRICT ON UPDATE CASCADE );
	
create table reviews_reyes(
	film_id serial4 not null,
	customer_id serial4 not null,
	review_date timestamp not null,
	review_description varchar(50),
	constraint reviews_reyes_filmid_pkey PRIMARY KEY (film_id, customer_id)
	);

INSERT INTO reviews_jorgeredbull (jorje_es_toni_cuquerella,jose_mota_es_mi_padre,antonio_lobato_es_mi_padre) 
VALUES (9, 14, 'Tengo envidia de reyes');

INSERT INTO reviews_jorgeredbull (film_id,customer_id,review_date,review_description) 
VALUES (9, 1, '2020-12-31', 'Tengo envidia de reyes');

ALTER TABLE reviews_jorgeredbull DROP COLUMN soy_muy_muy_muy_muy_inutil;

select *
from reviews_jorgeredbull 

select *
from reviews_chbc

update reviews_chbc
set review_description = 'Perdona tio, no volvera a pasar'
where film_id = 10

update reviews_jorgeredbull
set review_description = 'SOY TU ORDENADOR, DEJA DE PEGARME JORJE POR FAVOR'
where film_id = 10

alter table reviews_jorgeredbull 
rename column film_id
to jorje_es_toni_cuquerella

ALTER TABLE reviews_jorgeredbull RENAME COLUMN review_date TO SOY_MUY_MUY_MUY_MUY_INUTIL;

ALTER TABLE reviews_chbc ALTER COLUMN soy_un_inutil TYPE VARCHAR, ALTER COLUMN customer_id TYPE VARCHAR

