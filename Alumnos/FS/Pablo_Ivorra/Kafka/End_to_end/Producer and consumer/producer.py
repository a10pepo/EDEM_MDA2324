import time
from json import dumps
from confluent_kafka import Producer
import requests

# Configuración del productor
config = {
    'bootstrap.servers': 'localhost:9092',  # Cambia esto con la dirección de tu servidor Kafka
    'client.id': 'python-producer'
}

# Crear un productor
producer = Producer(config)

# URL de la API
api_url = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest?CMC_PRO_API_KEY=0c58c479-77a7-40d6-a7cd-21eeb593f831'

# Nombre del topic
topic_kafka = 'marketcap'

for e in range(100):
    # Realizar solicitud a la API
    response = requests.get(api_url)
    
    # Obtener datos de la respuesta de la API
    data = response.json()
    
    # Convertir los datos a formato JSON
    message = dumps(data)
    
    # Enviar el mensaje
    producer.produce(topic_kafka, message)

    # Asegurarse de que todos los mensajes se han enviado
    producer.flush()

    # Esperar un tiempo antes de la próxima solicitud
    time.sleep(10)