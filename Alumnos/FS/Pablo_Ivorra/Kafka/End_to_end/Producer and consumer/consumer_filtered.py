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
topic = 'marketcap_filtro'  # El nombre del tópico
consumer.subscribe([topic])

# Loop infinito de consumo de mensajes del tópico
try:
    while True:
        msg = consumer.poll(1.0)  # Leer nuevos mensajes cada 1 segundo
        
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print("No hay más mensajes en esta partición.")
            else:
                print("Error al recibir mensaje: {}".format(msg.error()))
        else:
            # Intentar parsear el mensaje JSON
            try:
                message_data = json.loads(msg.value().decode('utf-8'))
            except json.JSONDecodeError:
                print("El mensaje no es un JSON válido")
                continue
            
            # Filtrar por el mensaje de alerta de compra recomendada
            if message_data.get('alert_message') == "Compra recomendada: BTC está en alza":
                filtered_data = {
                    'price_usd': message_data.get('price_usd'),
                    'volume_usd': message_data.get('volume_usd'),
                    'btc_variation': message_data.get('btc_variation'),
                    'eth_variation': message_data.get('eth_variation'),
                    'alert_message': message_data.get('alert_message'),
                }
                print('Mensaje filtrado:', filtered_data)
            else:
                print('Mensaje no contiene una alerta de compra recomendada, no se procesa.')

except KeyboardInterrupt:
    pass
finally:
    # Cerrar el consumidor al detener la aplicación Python
    consumer.close()


