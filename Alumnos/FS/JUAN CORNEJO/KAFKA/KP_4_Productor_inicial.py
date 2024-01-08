from confluent_kafka import Producer
from KP_1_Definicion_clase import emergencia
import json
import time

def activar_productor_inicial():
    # Crear una lista de registros de emergencia
    registros_emergencia = [emergencia() for _ in range(250)]

    # Organizar los registros por fecha y así simulamos tiempo real.
    registros_emergencia.sort(key=lambda x: x.fecha)
    
    # Configuración del productor de Kafka
    producer_conf = {
        'bootstrap.servers': 'kafka:29092',
        'client.id': 'python-producer'
    }
    producer = Producer(producer_conf)

    def delivery_report(err, msg):
        if err is not None:
            print(f'Message delivery failed: {err}')
        else:
            print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

    # Enviar los registros
    for emergencia_instance in registros_emergencia:
        emergencia_json = emergencia_instance.to_json()
        producer.produce('T1_Recepcion_avisos', emergencia_json.encode('utf-8'), callback=delivery_report)
        producer.poll(0)
        time.sleep(1)  # Espera 2 segundo antes de enviar el siguiente registro

    producer.flush()
