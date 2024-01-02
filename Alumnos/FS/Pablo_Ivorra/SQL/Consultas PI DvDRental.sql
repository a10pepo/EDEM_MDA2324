#Consultas de sql exportadas de DBeaver

SELECT 
    f.title AS Titulo,
    f.rental_rate AS Tarifa_Alquiler,
    f.replacement_cost AS Costo_Reemplazo,
    ROUND((f.rental_rate / f.replacement_cost) * 100, 2) AS Porcentaje_Alquiler_Costo
FROM 
    film f;
   
   
   ----- Consulta de ciudades por país
   
SELECT 
    pais.country AS Pais, 
    COUNT(ciudad.city_id) AS Numero_Ciudades
FROM 
    country pais 
JOIN 
    city ciudad ON pais.country_id = ciudad.country_id 
GROUP BY 
    pais.country_id;

   ------Consulta del porcentaje del coste de alquiler sobre remplazo
   
   SELECT 
    titulo,
    tarifa_alquiler,
    costo_reemplazo,
    ROUND((tarifa_alquiler / costo_reemplazo) * 100, 2) AS Porcentaje_Renta_Sobre_Reemplazo
FROM 
    (SELECT title AS titulo, rental_rate AS tarifa_alquiler, replacement_cost AS costo_reemplazo FROM film) AS subconsulta;
   
   ------Consulta de actores


   SELECT 
    id_actor,
    nombre,
    apellido,
    ultima_actualizacion
FROM 
    (SELECT actor_id AS id_actor, first_name AS nombre, last_name AS apellido, last_update AS ultima_actualizacion FROM public.actor) AS actores;
   
   ---Consulta de películas con relación entre el coste re reemplazo y la tarifa de alquiler:
   
   SELECT 
    titulo,
    tarifa_alquiler,
    costo_reemplazo,
    ROUND(costo_reemplazo / tarifa_alquiler, 2) AS Relacion_Costo_Alquiler
FROM 
    (SELECT title AS titulo, rental_rate AS tarifa_alquiler, replacement_cost AS costo_reemplazo FROM film) AS peliculas;

   ---Consulta de estadística de películas:
   
   SELECT 
    COUNT(film_id) AS Numero_Peliculas,
    MAX(rental_rate) AS Pelicula_Mas_Cara,
    MIN(rental_rate) AS Pelicula_Mas_Barata,
    AVG(rental_rate) AS Promedio_Renta,
    COUNT(DISTINCT rental_rate) AS Diversidad_Precios,
    MIN(replacement_cost) AS Costo_Reemplazo_Minimo,
    MAX(replacement_cost) AS Costo_Reemplazo_Maximo
FROM 
    film;

   -----Consulta de películas con tarifa de alquiler menor a 5:
   
  SELECT 
    titulo
FROM 
    (SELECT title AS titulo FROM film WHERE rental_rate < 5) AS peliculas_baratas;

   -----Consulta de actores con nobre que comienza con "A"
   
   SELECT 
    nombre
FROM 
    (SELECT first_name AS nombre FROM actor WHERE first_name LIKE 'A%') AS actores_con_a;

   -------Consulta de películas con tarifa de alquiler mayor a 10:
   
   SELECT 
    titulo
FROM 
    (SELECT title AS titulo FROM film WHERE rental_rate > 10) AS peliculas_costosas;

   -------Consulta de películas con tarifa de alquiler entre 5 y 10
   
   SELECT 
    titulo
FROM 
    (SELECT title AS titulo FROM film WHERE rental_rate BETWEEN 5 AND 10) AS rango_medio_peliculas;

   
   ------ Creación tablas y vistas
   
   CREATE TABLE IF NOT EXISTS public.reviews_cf(
    id_pelicula INT2 NOT NULL,
    id_cliente INT2 NOT NULL,
    fecha_revision DATE NOT NULL,
    descripcion_revision VARCHAR(100),
    CONSTRAINT cf_reviews_pkey PRIMARY KEY (id_pelicula, id_cliente)
);

CREATE VIEW vista_pablo_ivorra AS
SELECT 
    DISTINCT calificacion,
    COUNT(calificacion) AS numero_peliculas,
    ROUND(AVG(tarifa_alquiler), 2) AS precio_medio,
    MIN(tarifa_alquiler) AS precio_minimo,
    MAX(tarifa_alquiler) AS precio_maximo,
    ROUND(AVG(duracion), 0) AS duracion_media,
    MIN(EXTRACT(YEAR FROM ultima_actualizacion)) AS año_minimo,
    MAX(EXTRACT(YEAR FROM ultima_actualizacion)) AS año_maximo
FROM 
    (SELECT rating AS calificacion, rental_rate AS tarifa_alquiler, LENGTH, last_update AS ultima_actualizacion FROM film) AS subconsulta
GROUP BY 
    calificacion
HAVING 
    COUNT(*) > 200;
