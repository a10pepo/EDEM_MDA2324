from confluent_kafka import Producer
from KP_1_Definicion_clase import emergencia
from KP_1_Definicion_clase import producer_Kafka
import json

def activar_productor_inicial():
    def get_data_first_producer():
        registros_emergencia = [emergencia() for _ in range(250)]
        registros_emergencia.sort(key=lambda x: x.fecha)
        for emergencia_instance in registros_emergencia:
            emergencia_json = emergencia_instance.to_json()
            First_producer.send_data_to_kafka(emergencia_json)
    First_producer = producer_Kafka ('kafka:29092','python-producer','T1_Recepcion_avisos')
    get_data_first_producer()
    First_producer.flush_producer()