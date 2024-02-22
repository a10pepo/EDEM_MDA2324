from confluent_kafka import Consumer, KafkaError

# Configuraciones
conf = {
    'bootstrap.servers': 'localhost:9092', 
    'group.id': 'my_consumer_group',
    'auto.offset.reset': 'earliest'
}

# Creo instancia del consumidor
consumer = Consumer(conf)

# Suscripcion al topic de Kafka
topic = 'topic_tiempo'
consumer.subscribe([topic])

# Bucle infinito de lectura de mensajes
try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print("No hay más mensajes en esta partición.")
            else:
                print("Error al recibir mensaje: {}".format(msg.error()))

        # Imprime el valor del mensaje
        print(f"Mensaje recibido: {msg.value().decode('utf-8')}")

except KeyboardInterrupt:
    pass

finally:
    # Cierra el consumidor
    consumer.close()
