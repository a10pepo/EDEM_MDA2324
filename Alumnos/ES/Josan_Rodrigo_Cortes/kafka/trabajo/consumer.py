from confluent_kafka import Consumer, KafkaError
import json

# Configuración del consumidor
config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my_consumer_group',
    'auto.offset.reset': 'earliest'
}

# Crear un consumidor
consumer = Consumer(config)

# Suscribirse al tema
kafka_topic = 'randomuserdata'
consumer.subscribe([kafka_topic])

try:
    mensaje = 0
    while True:
        # Esperar mensajes
        msg = consumer.poll(2.0)  # Espera 2 segundos por nuevos mensajes

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # Fin de la partición, no es un error
                continue
            else:
                print(f"Error en el mensaje: {msg.error()}")
                break
        
        mensaje += 1
        # Decodificar el valor del mensaje desde JSON
        try:
            message_data = json.loads(msg.value().decode('utf-8'))
        except json.decoder.JSONDecodeError as e:
            print(f"Error al decodificar el mensaje JSON: {e}")
            continue

        # Imprimir los campos del mensaje
        print(f"Nuevo mensaje:{mensaje}, Nombre: {message_data['nombre']}, Apellido: {message_data['apellido']}, País: {message_data['pais']}, Email: {message_data['email']}, Username: {message_data['username']}")

except KeyboardInterrupt:
    pass
finally:
    # Cerrar el consumidor al salir
    consumer.close()
