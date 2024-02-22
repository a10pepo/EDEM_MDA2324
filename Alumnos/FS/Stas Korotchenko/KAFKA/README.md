# Visualización Datos de Random Frases de API


## DESPLIEGUE DE LA APLICACIÓN:
---
1. `docker-compose up -d`
2. Para crear los topics:
   
    `docker-compose exec kafka kafka-topics --create --topic frase --partitions 1 --replication-factor 1 --if-not-exists --bootstrap-server localhost:9092`
    `docker-compose exec kafka kafka-topics --create --topic frase_likes_gt_2 --partitions 1 --replication-factor 1 --if-not-exists --bootstrap-server localhost:9092`
3. Para la creación de streams, debemos entrar ksql-cli con el comando
   
    `docker-compose exec ksql-cli ksql http://host.docker.internal:8088`
4. Después, ejecutar el código para crear los streams y filtrar.

## CASO DE USO
Con la ayuda de la API, obtenemos una frase aleatoria de personas famosas. En la estructura del archivo JSON que se muestra a continuación, observamos que cada frase tiene un campo "like". Por lo tanto, seleccionamos solo las frases que tienen más de 2 "likes". Luego, con la ayuda de ksql, queremos destacar la frase de una persona específica, por ejemplo, por su nombre.

Aquí se practica el uso de la API, la transferencia de datos al tema, un filtrado simple, el envío a otro tema y el procesamiento mediante ksql.

### 1. Adquisición de Datos:

- [producer.py](producer.py) 
- API https://favqs.com/api/qotd
- Transmisión de datos al topic de Kafka llamado 'frase'.


```json
{"qotd_date":"2024-01-24T00:00:00.000+00:00",
"quote":
  {"id":37980,"dialogue":false,"private":false,"tags":["life"],
  "url":"https://favqs.com/quotes/tupac-shakur/37980-it-s-the-game-",
  "favorites_count":2,
  "upvotes_count":0,
  "downvotes_count":0,
  "author":"Tupac Shakur",
  "author_permalink":"tupac-shakur",
  "body":"It's the game of life. Do I win or do I lose? One day they're gonna shut the game down. I gotta have as much fun and go around the board as many times as I can before it's my turn to leave."
  }
}
```
### 2. Filtrado y Enrutamiento:
- [consumer.py](consumer.py)
- Consumo de datos del topic 'frase'.
- Filtrado por 'Likes' > 2.
- Transmitir datos al topic 'frase_likes_gt_2'

### 3. Procesamiento con Ksql
- Consumo de datos del topic 'frase_likes_gt_2'.
- Filtrado de datos por author.

Queries en Ksql
 ```sql
-- Crea un STREAM para consumir datos del topic frase_likes_gt_2
CREATE STREAM frase_stream2
  (Cita STRING, Author STRING, Likes INT)
   WITH (KAFKA_TOPIC='frase_likes_gt_2',
        VALUE_FORMAT='DELIMITED');

-- Select mensaje de Author
SELECT * FROM frase_stream2 WHERE Author = 'Rupert Murdoch' emit changes;

```
