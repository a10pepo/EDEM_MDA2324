from confluent_kafka import Consumer, KafkaError

# Configuración del consumidor
config = {
    'bootstrap.servers': 'localhost:9092',  
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'  
}

consumer = Consumer(config)

topic = 'compras' 

# Suscribirse al tema
consumer.subscribe([topic])

try:
    while True:
        # Recibir mensajes del consumidor
        msg = consumer.poll(1.0) 
        
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print("No hay más mensajes en esta partición.")
            else:
                print("Error al recibir mensaje: {}".format(msg.error()))
        else:
            # Imprimir el mensaje recibido
            print('Nuevo mensaje: {}'.format(msg.value().decode('utf-8')))

except KeyboardInterrupt:
    pass
finally:
    # Cerrar el consumidor
    consumer.close()
