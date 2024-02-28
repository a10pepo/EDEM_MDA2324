-- SELECT FROM
select f.title, round((f.rental_rate/f.replacement_cost)*100, 3) as porcentaje from film;

select c.country from country c inner join city as ct on c.country_id = ct.country_id group by c.country_id;

select title, rental_rate, replacement_cost, round((rental_rate / replacement_cost)*100, 3) as porcentaje
from (select title, rental_rate, replacement_cost from film) as consulta;
   
select first_name from actor where first_name like 'A%';
   
select title from film where rental_rate between 5 and 10;

-- CREATE, INSERT, UPDATE, DELETE
create table if not exists public.reviews_emart(
    film int not null,
    client int not null,
    description text,
    created_at date not null
)

insert into public.reviews_emart values (1, 1, 'description', '23-01-2022');

update public.reviews_emart set description = 'none' where year(created_at) < 2023;

delete from public.reviews_emart where description = 'none';