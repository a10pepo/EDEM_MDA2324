from confluent_kafka import Consumer, KafkaError
import time
from json import dumps
from confluent_kafka import Producer
from data.functions import *

def kconsumer(topic):
    config = {
        'bootstrap.servers': 'localhost:9092',  
        'group.id': 'python-consumer-group',
        'auto.offset.reset': 'earliest'  
    }
    consumer = Consumer(config)
    consumer.subscribe([topic])
    try:
        while True:
            msg = consumer.poll(1.0)  # Lee nuevos mensajes cada 1 segundo
            
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print("No hay más mensajes en esta partición.")
                else:
                    print("Error al recibir mensaje: {}".format(msg.error()))
            else:
                print('Nuevo mensaje: {}'.format(msg.value().decode('utf-8')))
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
        
def kproducer(topic, columns, results):
    config = {
        'bootstrap.servers': 'localhost:9092',
        'client.id': 'python-producer'
    }
    producer = Producer(config)
    topic_kafka = topic
    for row in results:
        data = {}
        for i in range(len(columns)):
            if isinstance(row[i], datetime.datetime):
                data[columns[i]] = row[i].strftime("%Y-%m-%d %H:%M:%S")
            else:
                data[columns[i]] = row[i]
        data_str = dumps(data)
        data_bytes = data_str.encode('utf-8')
        key = str(data.get('tu_columna_clave', '')).encode('utf-8')
        producer.produce(topic=topic_kafka, value=data_bytes, key=key)
        print("Enviando dato: {} al tema {}".format(data, topic_kafka))
        time.sleep(1)
        
    producer.flush()
    if producer.flush() != 0:
        print("Algunos mensajes no se entregaron")