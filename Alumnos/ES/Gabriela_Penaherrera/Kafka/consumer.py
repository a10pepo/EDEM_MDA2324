from confluent_kafka import Consumer, KafkaError
import json

# Configuración del consumidor
config = {
    'bootstrap.servers': 'localhost:9092',  
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'  
}

# Crear un consumidor
consumer = Consumer(config)

# Suscribirse a un tópico
topic_kafka = 'rickandmorty'  
consumer.subscribe([topic_kafka])

# Loop infinito de consumo de mensajes del topic
try:
    while True:
        # Esperar mensajes
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # No se encontraron más mensajes en la partición
                continue
            else:
                print(f"Error al recibir mensaje: {msg.error()}")
                break

        # Procesar el mensaje
        character = json.loads(msg.value().decode('utf-8'))
        print(f"Mensaje recibido: Nombre: {character['name']}, Especie:{character['species']}, Genero: {character['gender']}, Imagen: {character['image']}")
        
except KeyboardInterrupt:
    pass
finally:
    # Cerrar el consumidor al salir
    consumer.close()



