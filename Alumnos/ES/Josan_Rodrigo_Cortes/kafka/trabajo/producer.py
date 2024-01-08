import time
import requests
from confluent_kafka import Producer
import json

# Configuración del productor
bootstrap_servers = 'localhost:9092'
kafka_topic = 'randomuserdata'
client_id = 'random-username-producer'

# Crear un productor
config = {
    'bootstrap.servers': bootstrap_servers,
    'client.id': client_id
}
producer = Producer(config)

try:
    while True:
        # Obtener un nombre de usuario aleatorio de la API
        url = "https://randomuser.me/api/"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            # Extraer campos específicos
            nombre = data["results"][0]["name"]["first"]
            apellido = data["results"][0]["name"]["last"]
            pais = data['results'][0]['location']['country']
            email = data['results'][0]['email']
            username = data['results'][0]['login']['username']

            print('---------------------')
            print(f' Nombre: {nombre}, apellido: {apellido}, pais: {pais}, email: {email} y username: {username}')
            

            # Construir el diccionario
            message_data = {
                "nombre": nombre,
                "apellido": apellido,
                "pais": pais,
                "email": email,
                "username": username
            }

            # Convertir a JSON y enviar al tema de Kafka
            producer.produce(topic=kafka_topic, value=json.dumps(message_data))

            # Esperar 5 segundos antes de enviar el próximo mensaje
            time.sleep(2)
        else:
            print(f"Error al hacer la solicitud. Código de estado: {response.status_code}")

except KeyboardInterrupt:
    pass
finally:
    # Cerrar el productor al salir
    producer.flush()

