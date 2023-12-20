# Exercise 5: KSQL

## Objectives

1) Produce messages from a Python application.
2) Use KSql to query the messages


## Run Kafka in your computer with Docker
Simple scenario: 1 zookeeper + 1 Kafka broker.

Start the ZooKeeper and Kafka container.

```sh
$ docker-compose up -d
```

Status:

```sh
$ docker-compose ps
      Name                  Command            State                     Ports
-------------------------------------------------------------------------------------------------
lab1_kafka_1       /etc/confluent/docker/run   Up      0.0.0.0:9092->9092/tcp
lab1_zookeeper_1   /etc/confluent/docker/run   Up      0.0.0.0:2181->2181/tcp, 2888/tcp, 3888/tcp
```

## Command Line , create a new Kafka topic

Run the command line producer:

```sh
docker-compose exec kafka kafka-topics --create --topic palabras --partitions 1 --replication-factor 1 --if-not-exists --bootstrap-server localhost:9092
```

## Run the Producer Python App from VisualStudio


```sh
docker-compose exec ksql-cli ksql http://host.docker.internal:8088
```


## Open KSql in a console, and query the data
docker-compose exec ksql-cli bash -c 'echo -e "\n\n⏳ Waiting for KSQL to be available before launching CLI\n"; while [ $(curl -s -o /dev/null -w %{http_code} http://ksql-server:8088/) -eq 000 ] ; do echo -e $(date) "KSQL Server HTTP state: " $(curl -s -o /dev/null -w %{http_code} http://ksql-server:8088/) " (waiting for 200)" ; sleep 5 ; done; ksql http://ksql-server:8088'

⏳ Waiting for KSQL to be available before launching CLI

      ===========================================
      =        _  __ _____  ____  _             =
      =       | |/ // ____|/ __ \| |            =
      =       | ' /| (___ | |  | | |            =
      =       |  <  \___ \| |  | | |            =
      =       | . \ ____) | |__| | |____        =
      =       |_|\_\_____/ \___\_\______|       =
      =                                         =
      =  Streaming SQL Engine for Apache Kafka® =
      ===========================================
Copyright 2017-2019 Confluent Inc.

CLI v5.4.1, Server v<unknown> located at http://ksql-server:8088

https://docs.confluent.io/current/ksql/docs/developer-guide/syntax-reference.html

```sql
ksql>  SET 'auto.offset.reset' = 'earliest';
```
```sql
ksql> SHOW TOPICS;
```
```
Kafka Topic  | Partitions | Partition Replicas
------------------------------------------------
 orders | 1          | 1
------------------------------------------------
```
```sql
ksql> PRINT 'palabras' FROM BEGINNING;
```

If you have data in an existing Apache Kafka topic, you can create a stream or a table backed by that topic and begin 
streaming the data into ksqlDB:
Any subsequent data produced to the topic will be streamed into ksqlDB, and any data inserted into the new stream will
be written to the Kafka topic automagically.
```sql
ksql> CREATE STREAM palabras_largas
  (palabra VARCHAR)
   WITH (KAFKA_TOPIC='palabras',
        VALUE_FORMAT='JSON');
```

Select all the messages from the stream (topic)
```sql
SELECT valor, LEN(valor) FROM mi_stream emit changes;
```

Select the messages from the stream where the message size is major than 7
```sql
SELECT valor AS mi_valor, LEN(valor) AS longitud FROM mi_stream WHERE LEN(valor) > 7 emit changes;
```


Filter words starting with the letter "t" in a stream named mi_stream
```sql
CREATE STREAM palabras_con_t AS
SELECT *
FROM mi_stream
WHERE valor LIKE 't%';
```

Create a KTable
```sql
CREATE TABLE mi_ktable2 AS
SELECT valor,
count(*)
FROM mi_stream
GROUP BY valor
EMIT CHANGES;
SELECT * FROM mi_ktable2 EMIT CHANGES;
```

Read the KTable
```sql
SELECT * FROM mi_ktable EMIT CHANGES;
```

#### More Exercises
##### Exercise 5.1
Find the words that starts with 'ca', finishes wtith 'o' and the word is longer than 6 characters.

##### Exercise 5.1
show the word transformed in Uppercase. Hint: use a select and using the function UCASE(...)



