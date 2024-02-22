from confluent_kafka import Consumer, Producer, KafkaError
import json
from faker import Faker

def activar_consumidor_productor():
    # Configuración del consumidor
    config = {
        'bootstrap.servers': 'kafka:29092',  
        'group.id': 'python-consumer-group-99',
        'auto.offset.reset': 'earliest'  
    }

    # Crear un consumidor
    consumer = Consumer(config)
    producer = Producer({'bootstrap.servers': 'kafka:29092'})

    # Suscribirse a un tópico
    topic = 'T2_Centro_112'  # El nombre del tópico
    consumer.subscribe([topic])

    # Faker para generar direcciones aleatorias
    fake = Faker('es_ES')

    # Loop infinito de consumo de mensajes del topic
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
                mensaje = json.loads(msg.value().decode('utf-8'))
                if mensaje['REQUIERE_MEDICO'] == 'Si':
                    # Añadir dirección aleatoria sin salto de línea
                    mensaje['DIRECCION'] = fake.street_address()
                    # Enviar mensaje modificado al productor
                    producer.produce('T2.1_Sanitarios_112', json.dumps(mensaje).encode('utf-8'))
                    print(f'Mensaje modificado: {mensaje}')
                else:
                    # No modifica el mensaje, solo lo imprime
                    print(f'Mensaje sin modificación: {mensaje}')

    except KeyboardInterrupt:
        pass
    finally:
        # Cerrar el consumidor al parar la Aplicación Python
        consumer.close()
        producer.flush()
