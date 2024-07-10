import time
from json import dumps
from confluent_kafka import Producer
import re

# Configuración del productor
config = {
    'bootstrap.servers': 'localhost:9092',  # Cambia esto con la dirección de tu servidor Kafka
    'client.id': 'python-producer'
}

# Crear un productor
producer = Producer(config)


topic_kafka = 'lineas'

file1 = open('Final_Transaction.csv',encoding="utf8")
Lines = file1.readlines()
 
count = 0

for line in Lines:
    time.sleep(2)
    print(line.strip() + "\n")

    # Send the entire line as a single message (phrase)
    data_bytes = line.strip()  # Encode string to bytes
    key = str(count)
    producer.produce(topic=topic_kafka, value=data_bytes, key=key)  # Send bytes
    count += 1


# Optionally, you can check if there are any messages that failed to be delivered:
if producer.flush() != 0:
    print("Some messages failed to be delivered")