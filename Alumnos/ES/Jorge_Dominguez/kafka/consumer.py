from confluent_kafka import Consumer, KafkaException
from unidecode import unidecode
from json import loads

def sin_acentos(text):
    return unidecode(text)

def procesar_mensaje(message):
    key = message.key().decode('utf-8')
    value = loads(message.value().decode('utf-8'))
    
    print("Received message with key {} and value {}".format(key, value))

def kafka_consumer(config, topic):
    try:
        consumer = Consumer(config)
        consumer.subscribe([topic])

        while True:
            message = consumer.poll(timeout=1.0)
            if message is None:
                continue
            if message.error():
                if message.error().code() == KafkaException._PARTITION_EOF:
                    continue
                else:
                    print(message.error())
                    break

            procesar_mensaje(message)

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__ == '__main__':
    consumer_config = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'python-consumer-group',
        'auto.offset.reset': 'earliest'
    }
    
    producer_config = {
        'bootstrap.servers': 'localhost:9092',
        'client.id': 'python-producer'
    }

    topic_kafka = 'tripadvisor'

    kafka_consumer(consumer_config, topic_kafka)