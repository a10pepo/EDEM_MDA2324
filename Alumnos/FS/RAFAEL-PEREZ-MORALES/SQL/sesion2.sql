-- Ejercicio 8 --

SELECT c.first_name, c.last_name, a.address, a.address2, a.district, a.postal_code, a.phone
FROM customer c
JOIN address a ON c.address_id = a.address_id;

SELECT c.first_name, c.last_name, a.address, a.address2, a.district, a.postal_code, a.phone, ci.city
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id;

SELECT c.first_name, c.last_name, a.address1, a.address2, a.district, a.postal_code, a.phone, ci.city, co.country
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id;

-- Ejercicio 9 --
SELECT title, f.title,
       a.last_name
FROM film f
INNER JOIN film_actor fc ON
fc.film_id = f.film_id
INNER JOIN actor a ON
fc.actor_id = a.actor_id
WHERE a.last_name LIKE 'C%';

SELECT TITLE, COUNT(first_name)
FROM film f
INNER JOIN film_actor fc ON
    fc.film_id = f.film_id
INNER JOIN actor a ON
    fc.actor_id = a.actor_id
GROUP BY 1
HAVING COUNT(last_name) > 6
ORDER BY 2 DESC;

-- Ejercicio 10 --
CREATE TABLE IF NOT EXISTS public.reviews_rp (
film_id int2 NOT NULL,
customer_id int2 NOT NULL,
review_date date NOT NULL,
review_description varchar,
CONSTRAINT reviews_pkey PRIMARY KEY (film_id, customer_id)
CONSTRAINT film_actor_actor_id_fkey FOREIGN KEY (customer_id) REFERENCES
customer(customer_id) ON DELETE RESTRICT ON UPDATE CASCADE,
CONSTRAINT film_actor_film_id_fkey FOREIGN KEY (film_id) REFERENCES film(film_id) ON
DELETE RESTRICT ON UPDATE CASCADE
);

-- Ejercicio 11 --
insert INTO public.reviews_rp
(film_id,customer_id,review_date,review_description)
VALUES (4, 7, '10-11-2023', 'La película es un poco aburrida');

-- Ejercicio 12 --
UPDATE public.reviews_rp
SET review_description = 'La película es bastante divertida y para todo los públicos'
WHERE customer_id = 7 and film_id = 4;

-- Ejercicio 13 --
ALTER TABLE reviews
ADD COLUMN review_stars int2;

ALTER TABLE reviews
RENAME COLUMN review_description TO review_opinion;

ALTER TABLE reviews
ALTER COLUMN review_stars TYPE varchar;

ALTER TABLE reviews
DROP COLUMN review_stars;

DELETE
FROM public.reviews_rp
WHERE customer_id = 7;

drop table public.reviews_rp;