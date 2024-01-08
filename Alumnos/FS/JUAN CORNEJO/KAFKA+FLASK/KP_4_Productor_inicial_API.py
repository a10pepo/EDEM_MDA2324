from confluent_kafka import Producer
import requests
import time
import json

def activar_productor_inicial_API():
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

    # Solicitar registros de emergencia de la API
    for _ in range(200):
        response = requests.get('http://flask:5000/generar_registros_emergencias/112')
        if response.status_code == 200:
            emergencia_json = response.text
            producer.produce('T1_Recepcion_avisos', emergencia_json.encode('utf-8'), callback=delivery_report)
            producer.poll(0)
        else:
            print(f"Error al obtener datos de la API: {response.status_code}")
        
        time.sleep(1)  # Espera 1 segundo antes de enviar el siguiente registro

    producer.flush()

# Llama a la función para activar el productor

