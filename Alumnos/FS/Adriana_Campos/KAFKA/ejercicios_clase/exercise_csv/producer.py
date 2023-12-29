import time
from json import dumps
from confluent_kafka import Producer
import re
import csv


# Configuración del productor
config = {
    'bootstrap.servers': 'localhost:9092',  # Cambia esto con la dirección de tu servidor Kafka
    'client.id': 'python-producer'
}

# Crear un productor
producer = Producer(config)


topic_kafka = 'readcsv'


# Cambia el nombre del archivo CSV según tu necesidad
csv_file = '/Users/adrianacamposnarvaez/Documents/GitHub/EDEM_MDA2324/Alumnos/FS/Adriana_Campos/KAFKA/ejercicios_clase/exercise_csv/Final_Transaction.csv'

count = 0

with open(csv_file, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if not row:
            continue  # Ignorar líneas vacías
        line = row[0]  # Supongamos que la columna que deseas enviar como frase es la primera (índice 0)
        time.sleep(2)
        print(line.strip() + "\n")

        # Send the entire line as a single message (phrase)
        data_bytes = line.strip()  # Encode string to bytes
        key = str(count)
        producer.produce(topic=topic_kafka, value=data_bytes, key=key)  # Send bytes
        count += 1

        # After your loop where you send messages:
        producer.flush()

# Optionally, you can check if there are any messages that failed to be delivered:
if producer.flush() != 0:
    print("Some messages failed to be delivered")