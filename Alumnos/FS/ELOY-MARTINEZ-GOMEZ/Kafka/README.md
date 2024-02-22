### END2END - KAFKA 
---

#### Proyecto
En este proyecto, utilizamos la API de polygon.io para monitorear el control de inversiones mediante la creación de alertas de precios. Hacemos uso de Kafka para el manejo del flujo de datos en tiempo real, complementado con KSQL para el procesamiento y filtrado de streams.

***Nota***: *La api limita nuestra actividad, por lo que recreamos lo que sería la llamada a la API haciendo una consulta SQL, obteniendo todos los datos introducidos anteriormente (desde la API) y recorriendolos uno a uno. Si se tratase del caso de uso real, simplemente cambiariamos los datos de la consulta sql por los devueltos por la API.*

#### Arquitectura
La arquitectura involucra varios componentes clave:
- **API de Polygon.io**: Utilizada para obtener datos de inversiones.
- **Base de Datos MySQL**: Almacena los datos descargados de la API.
- **Kafka**: Gestiona el flujo de datos en tiempo real a través de varios topics.

## Caso de Uso de Kafka
---
Apache Kafka sirve para el procesamiento de datos en tiempo real. Así es como usamos Kafka en nuestra configuración:

1. **Productor al Topic `Pricelist`**: Los datos se envían a un topic de Kafka llamado "Pricelist".
2. **Consumidores para el Procesamiento de Datos**: Los datos se leen de "Pricelist", se procesan y se filtran según diferentes casos de uso.
3. **Enrutamiento de Datos a Topics**: Los datos procesados se envían a los topics "Alertas" o "Variaciones de Precios".
4. **KSQL para Filtrado Avanzado**: Utilizamos KSQL para filtrar aún más los datos de los topics "Alertas" y "Variaciones de Precios" en un nuevo topic.
5. **Visualización de Datos**: La salida final se lee y se muestra en el terminal en Visual Studio.

#### Escenario: Identificación de Oportunidades de Compra
Nos enfocamos particularmente en identificar posibles oportunidades de compra analizando las variaciones de precios y los umbrales de precios establecidos. Por ejemplo, si el precio supera los $195 y la variación es mayor al 5%, señala una oportunidad de compra ***- caso inventado para dar unos parámetros -***.

## DESPLIEGUE DE LA APLICACIÓN:
---
1. `docker-compose up -d`
2. Una vez levantado el docker y comprobado que la tabla se ha creado, ejecutamos para la ingestión de los datos el comando: `python3 model/data/data_ingestion.py`
3. `docker exec -it kafka bash` - En caso de tener problemas con el nombre, ejecutar `docker ps` 
    y ejecutar `docker exec -it [NOMBRE_O_ID_DEL_CONTENEDOR_KAFKA] bash`
4. En el propio bash, ejecutar los siguientes comandos para crear los topics: 
    `kafka-topics --create --topic pricelist --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1`
    `kafka-topics --create --topic alerts --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1`
    `kafka-topics --create --topic variations --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1`
    `kafka-topics --create --topic buy --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1`
5. Para la creación de streams, debemos entrar ksql-cli con el comando `docker exec -it ksql_cli ksql http://ksql-server:8088`
6. Después, ejecutar el siguiente código para crear los streams:
    ```sql
    CREATE STREAM alerts_stream (id VARCHAR, time STRING)
    WITH (KAFKA_TOPIC='alerts', VALUE_FORMAT='JSON');

    CREATE STREAM variations_stream (id VARCHAR, variation_ex DOUBLE, variation_in DOUBLE)
    WITH (KAFKA_TOPIC='variations', VALUE_FORMAT='JSON');

    CREATE STREAM buy_stream WITH (KAFKA_TOPIC='buy') AS
    SELECT a.id
    FROM alerts_stream a
    INNER JOIN variations_stream v WITHIN 5 MINUTES ON a.id = v.id
    WHERE ABS(v.variation_ex) > 0.02;
    ```
7. Por último, podemos ver los mensajes recibidos en los topics lanzando su consumidor:
    -   `python3 nombre_consumidor.py` (IOS)
    -   `python nombre_consumidor.py` (Windows)

---
#### Continuidad de la aplicación
En el caso se quisiera continuar la aplicación y que los parámetros utilizados fueran veráces, se podría desarrollar un sistema de aviso por mail o un dashboard de seguimiento en el cuál veas un detalle del seguimiento o conectar un broker para hacer un bot de trading... 