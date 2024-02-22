from confluent_kafka import Consumer, KafkaError, Producer
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
input_topic = 'marketcap'  # El nombre del tópico de entrada
output_topic = 'marketcap_filtro'   # El nombre del tópico de salida
consumer.subscribe([input_topic])

# Configuración del productor
producer_conf = {
    'bootstrap.servers': 'localhost:9092'
}
producer = Producer(producer_conf)

# Loop infinito de consumo de mensajes del tópico de entrada
try:
    while True:
        msg = consumer.poll(1.0)  # Lee nuevos mensajes cada 1 segundo

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print("No hay más mensajes en esta partición.")
            else:
                print("Error al recibir mensaje: {}".format(msg.error()))
        else:
            # Obtener el valor del mensaje
            message_value = json.loads(msg.value().decode('utf-8'))

            # Seleccionar campos específicos
            timestamp = message_value.get('status', {}).get('timestamp', 'N/A')
            eth_dominance = message_value.get('data', {}).get('eth_dominance', 'N/A')
            btc_dominance = message_value.get('data', {}).get('btc_dominance', 'N/A')

            # Construir el nuevo mensaje en formato de texto
            new_message = f"Timestamp = {timestamp}\nCoin = USD\nEth_dominance = {eth_dominance}\nBtc_dominance = {btc_dominance}\n"

            # Publicar en el tópico de salida
            producer.produce(output_topic, key=None, value=new_message.encode('utf-8'))
            print(f'Mensaje publicado en {output_topic}: {new_message}')

except KeyboardInterrupt:
    pass
finally:
    # Cerrar el consumidor y el productor al parar la aplicación Python
    consumer.close()
    producer.flush()
