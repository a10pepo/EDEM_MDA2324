from confluent_kafka import Consumer, KafkaError, Producer
import json

# Configuración del consumidor
config = {
    'bootstrap.servers': 'localhost:9092',  
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'  
}

# Configuración del productor
producer_config = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'python-producer'
}

# Crear un consumidor
consumer = Consumer(config)
producer = Producer(producer_config)

# Suscribirse a un tópico
topic_kafka = 'frase'  
consumer.subscribe([topic_kafka])

# Tópico para mensajes con likes > 2
topic_likes_gt_2 = 'frase_likes_gt_2'

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
        frase = json.loads(msg.value().decode('utf-8'))
        if frase.get('likes') > 2:
            print(f"Mensaje recibido:\nCita: {frase['body']}\nAuthor: {frase['author']}\nLikes: {frase['likes']}")
        
            # Enviar mensaje al otro tópico
            producer.produce(topic_likes_gt_2, value=msg.value())        

except KeyboardInterrupt:
    pass
finally:
    # Cerrar el consumidor al salir
    consumer.close()
    producer.flush()
