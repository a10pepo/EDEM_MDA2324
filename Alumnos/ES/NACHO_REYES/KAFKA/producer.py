from datetime import datetime, timedelta
from json import dumps, loads
from confluent_kafka import Producer
import time
import random

def cargar_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return loads(file.read())
    except FileNotFoundError:
        return {}


def mandar_datos_kafka(producer, topic, num_messages=30, min_sleep_time=1, max_sleep_time=5):
    nombre_archivo = 'dakar.json'
    eljson = cargar_json(nombre_archivo)

    with open('dakar.json', 'r', encoding='utf-8') as json_file:
        coords = loads(json_file.read()).get('coords', [])

    for e, coord in enumerate(coords[eljson.get('coords_count', 0):], start=eljson.get('coords_count', 0)):
        coord_message = {
            'id': (coord.get('id', '')),
            'latitud': coord.get('latitud', ''),
            'longituf': (coord.get('longitud', '')),
            'punto_control': coord.get('punto_control', '')
        }
        data_str = dumps(coord_message).encode('utf-8')
        key = str(e).encode('utf-8')

        producer.produce(topic=topic_dakar, value=data_str, key=key)
        print("Sending data: {} to topic {}".format(coord_message, topic))

        sleep_time = random.uniform(min_sleep_time, max_sleep_time)
        time.sleep(sleep_time)

    producer.flush()

    if producer.flush() != 0:
        print("Some messages failed to be delivered")


config = {
    'bootstrap.servers': 'kafka:29092',  # Cambia esto con la dirección de tu servidor Kafka
    'client.id': 'python-producer'
}
producer = Producer(config)

topic_dakar = 'topic_dakar'
mandar_datos_kafka(producer, topic_dakar)