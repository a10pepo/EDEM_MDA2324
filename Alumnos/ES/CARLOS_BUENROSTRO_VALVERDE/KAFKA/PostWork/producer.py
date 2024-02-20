# Importamos las librerías necesarias para poder realizar el ejercicio.
import time
from json import dumps
from confluent_kafka import Producer
import re
import csv

# Configuración del productor
config = {
    'bootstrap.servers': 'localhost:9092',  # Cambia esto con la dirección de tu servidor Kafka.
    'client.id': 'python-producer'
}

# Crear un productor
producer = Producer(config)

# Creamos el nombre del topic donde almacenaremos los mensajes.
topic_kafka = 'topic_entregable'

# Nombre del archivo .CSV desde el que vamos a enviar los mensajes al topic de Kafka.
csv_file = 'NBA_Player_Stats_2.csv'

# Definimos la función para enviar los datos internos al topic de Kafka.
def send_messages(message, key):
    producer.produce(topic = topic_kafka, value = message, key = key)
    producer.flush()
    print(f'Enviando datos al topic: {topic_kafka}, key: {key}, message: {message}')

# Leemos el archivo CSV y enviaremos sus datos al topic de Kafka.
try:
    with open(csv_file, 'r', encoding = 'utf8') as fichero_csv:
        csv_reader = csv.reader(fichero_csv)
        header = next(csv_reader)
        for row in csv_reader:
            time.sleep(3) # Hacemos que los mensajes se envíen cada 3 segundos.
            message = ','.join(row)
            key = row[0]

            send_messages(message, key)
except Exception as e:
    print(f'Error: {e}')