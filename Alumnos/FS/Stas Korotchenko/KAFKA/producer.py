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

topic_kafka = 'frase'


try:
    while True:
        # Получить цитату из API
        url = 'https://favqs.com/api/qotd'
        response = requests.get(url)
        quote_data = response.json()['quote']
        body = quote_data['body']
        author = quote_data['author']
        likes = quote_data['favorites_count']

        try:
            producer.produce(topic_kafka, value=json.dumps({'body': body, 'author': author, 'likes': likes}))
            time.sleep(3)
            print(f"Mensaje enviado - Cita: {body}, Author: {author}, Likes: {likes}")
        except Exception as e:
            print(f"Error al enviar mensaje: {str(e)}")


except KeyboardInterrupt:
    pass
finally:
    # Cerrar el productor al salir
    producer.flush()