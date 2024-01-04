# Exercise csv

## Objectives

1) Produce messages from a Python application.
2) Use KSql to query the messages


## Run Kafka in your computer with Docker
Simple scenario: 1 zookeeper + 1 Kafka broker + 1 Ksql server + 1 Ksql CLI.

Start the ZooKeeper and Kafka container.

**To execute below command, make sure you open the terminal under the folder "exercise5/"**
```sh
$ docker-compose up -d
```

## Create a new Kafka topic


```sh
docker-compose exec kafka kafka-topics --create --topic readcsv --partitions 1 --replication-factor 1 --if-not-exists --bootstrap-server localhost:9092
```

## Run the Producer Python  and the Consumer
Execute the ´producer.py´ Python Producer Application. Check that it shows the transactions.

Execute the ´consumer.py´ Python Producer Application. Check that it shows the transactions.


```sh
docker-compose exec kafka kafka-console-consumer --topic readcsv --from-beginning --bootstrap-server localhost:9092
```

If the messages are arriving you are OK. Now Exit with Control-C. You are ready to start to query the messages with KSQL in next steps :)!!!

## Open KSql in a console
```sh
docker-compose exec ksql-cli ksql http://host.docker.internal:8088
````

Check you can see an output like the below one:

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


## Query the messages from a topic with KSQL

```sql
SET 'auto.offset.reset' = 'earliest';
```
```sql
SHOW TOPICS;
```
```
Kafka Topic  | Partitions | Partition Replicas
------------------------------------------------
 palabras | 1          | 1
------------------------------------------------
```
```sql
PRINT 'readcsv' FROM BEGINNING;
```

Press Control-C some times to exit. Be patient, some times take time :)....If it does not stop, close the terminal and 
open a new one under the same folder "exercise5".

If you have data in an existing Apache Kafka topic, you can create a stream or a table backed by that topic and begin 
streaming the data into ksqlDB:
Any subsequent data produced to the topic will be streamed into ksqlDB, and any data inserted into the new stream will
be written to the Kafka topic automagically.
```sql
CREATE STREAM transaction\
(INDICE INT, TRANSACTION_ID INT, TX_DATETIME STRING, CUSTOMER_ID INT, TERMINAL_ID INT, TX_AMOUNT DOUBLE, TX_TIME_SECONDS INT, TX_TIME_DAYS INT, TX_FRAUD INT, TX_FRAUD_SCENARIO INT) \
WITH (KAFKA_TOPIC='readcsv', VALUE_FORMAT='JSON');
```



Select all the messages from the stream (topic), and show what is each word's length.
```sql
SELECT * FROM transaction EMIT CHANGES;
```

```sql
SELECT TRANSACTION_ID FROM transaction EMIT CHANGES;
```

 Queremos ver que operaciones son fraudulentas. 

```sql
SELECT * FROM transaction WHERE TX_FRAUD = 1 EMIT CHANGES;
```

# Another topic

```sql
CREATE STREAM Fraud
WITH (KAFKA_TOPIC='TransactionFraud')
AS
SELECT *
FROM transaction
WHERE TX_FRAUD = 1
EMIT CHANGES;
```

```sql
SELECT TRANSACTION_ID FROM Fraud EMIT CHANGES;
```

#### More Exercises

**Note:** If you are interested in learning more on KSQL you can find developer info here: https://docs.confluent.io/current/ksql/docs/developer-guide/syntax-reference.html
And you can try from this doc to performe another KSQL with the 'palabras' topic.

