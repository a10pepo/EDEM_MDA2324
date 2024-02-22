#Explicación Postwork

#Para poder realizar este trabajo he utilizado un archivo txt (KAFKA\libro.txt) de un libro de la saga Juego de Tronos.

#El primer paso es inicializar el consumidor y el productor. Creamos el topic y lo configuramos para poder enviar/recibir los datos.
#Los datos que se van mandando por consola es cada una de las lineas que encontramos dentro del txt.

#Con esto funcionando, levantamos el contenedor de docker con el siguiente comando docker-compose exec ksql-cli ksql http://host.docker.internal:8088 para poder procesar los datos mediante KSQL.


#Creamos un topic (en este caso, topic_postwork) y realizamos las búsquedas que vemos en las fotos 
#(palabras que empiezan por a y conteo de cuantas veces sale cada palabra)