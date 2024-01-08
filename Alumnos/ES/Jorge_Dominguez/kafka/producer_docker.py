from json import dumps, loads
from confluent_kafka import Producer
from unidecode import unidecode 
import time
import random

def sin_acentos(text):
    return unidecode(text)

def read_ccloud_config(config_file):
    with open(config_file) as fh:
        return dict(line.strip().split('=', 1) for line in fh if line.strip() and line[0] != "#")

def cargar_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return loads(file.read())
    except FileNotFoundError:
        return {}

def enviar_mensaje(producer, topic, num_messages=100, min_sleep_time=1, max_sleep_time=5):
    nombre_archivo = 'reviews.json'
    eljson = cargar_json(nombre_archivo)

    with open('reviews.json', 'r', encoding='utf-8') as json_file:
        reviews = loads(json_file.read()).get('reviews', [])

    for e, review in enumerate(reviews[eljson.get('review_count', 0):], start=eljson.get('review_count', 0)):
        review_message = {
            'review': sin_acentos(review.get('review', '')),
            'estrellas': review.get('estrellas', '')
        }
        data_str = dumps(review_message).encode('utf-8')
        key = str(e).encode('utf-8')
        
        producer.produce(topic=topic, value=data_str, key=key)
        print("Sending data: {} to topic {}".format(review_message, topic))
        
        sleep_time = random.uniform(min_sleep_time, max_sleep_time)
        time.sleep(sleep_time)

    producer.flush()
    
    if producer.flush() != 0:
        print("Some messages failed to be delivered")

# Configuración del productor Kafka
config = {
    'bootstrap.servers': 'kafka:29092', 
    'client.id': 'python-producer'
}

producer = Producer(config)

topic_kafka = 'tripadvisor'

enviar_mensaje(producer, topic_kafka)
