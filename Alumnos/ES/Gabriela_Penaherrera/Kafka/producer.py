from confluent_kafka import Producer
import json
import requests
import time

# Configuración del productor
config = {
    'bootstrap.servers': 'localhost:9092',  
    'client.id': 'python-producer'
}

# Crear un productor
producer = Producer(config)

topic_kafka = 'rickandmorty'

try:
    while True:
        # Obtener un nombre de personajes de la API
        url = 'https://rickandmortyapi.com/api/character'
        response = requests.get(url)
        characters = response.json()['results']

        for character in characters:
            try:
                producer.produce(topic_kafka, value=json.dumps(character))
                time.sleep(3)
                print(f"Mensaje enviado: {character}")
            except Exception as e:
                print(f"Error al enviar mensaje: {str(e)}")

except KeyboardInterrupt:
    pass
finally:
    # Cerrar el productor al salir
    producer.flush()










