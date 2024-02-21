import time
from json import dumps
from confluent_kafka import Producer
import random

# Configuración del productor Kafka
config = {
    'bootstrap.servers': 'localhost:9092', 
    'client.id': 'python-producer'
}

# Crear una instancia del productor Kafka
producer = Producer(config)

# Definir el tema al que se enviarán los mensajes
topic = 'compras'

# Crea el input data sobre compras
productos = ['iPhone', 'Samsung Galaxy', 'MacBook Pro', 'PlayStation 5']
precios = [999.99, 799.99, 1499.99, 499.99]
cantidades = [1, 2, 3, 4]

# Generar y enviar mensajes al tema
for i in range(10):
    producto = random.choice(productos)
    precio = random.choice(precios)
    cantidad = random.choice(cantidades)
    
    input_data = {
        'producto': producto,
        'precio': precio,
        'cantidad': cantidad
    }

    data_str = dumps(input_data)
    data_bytes = data_str.encode('utf-8')
    key = str(i).encode('utf-8')
    
    # Enviar mensaje al tema
    try:
        producer.produce(topic=topic, value=data_bytes, key=key)
        print("Sending data: {} to topic {}".format(input_data, topic))
    except Exception as e:
        print("Failed to send message:", str(e))
    
    # Vaciar el buffer del productor y esperar a que se envíen todos los mensajes
    producer.flush()

    time.sleep(3)

