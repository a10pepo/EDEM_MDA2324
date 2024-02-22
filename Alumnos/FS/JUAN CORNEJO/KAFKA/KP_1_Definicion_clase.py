import random
import time
import json
import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
from confluent_kafka import Producer, Consumer, KafkaError

class emergencia:
    tipo_emergencia = {
        "Accidentes de tráfico": ["Policia", "Ambulancia", "Bomberos"],
        "Problemas médicos agudos": ["Ambulancia"],
        "Incendios": ["Bomberos"],
        "Delitos en progreso": ["Policia", "GEOs", "Ejercito"],
        "Situaciones de peligro para la seguridad pública": ["Policia", "GEOs", "Ejercito"],
        "Desastres naturales": ["Bomberos", "UME", "Servicios de emergencia"],
        "Emergencias químicas o radiológicas": ["Bomberos", "Servicios de emergencia"],
        "Personas desaparecidas": ["Policia"],
        "Rescates": ["Bomberos", "Forestales"],
        "Emergencias en el mar o montañas": ["Guardia Costera", "Forestales"],
        "Accidentes laborales": ["Ambulancia", "Bomberos"],
        "Emergencias ambientales": ["Servicios de emergencia", "Bomberos"]
        }
    fake = Faker('es_ES')
    def __init__(self):
        self.tipo_emergencia = random.choice(list(emergencia.tipo_emergencia))
        self.cuerpo_necesario = random.choice(emergencia.tipo_emergencia[self.tipo_emergencia])
        if self.cuerpo_necesario in ["GEOs","Ejercito","UME"]:
            self.grado = random.choice(["Urgencia extrema","Urgente"])
        else:
            grados_urgencia = ['Leve', 'Moderado', 'Urgente', 'Urgencia extrema']
            probabilidades = [0.35, 0.35, 0.20, 0.10]
            self.grado = np.random.choice(grados_urgencia,p=probabilidades)
        self.localizacion = emergencia.fake.city()
        self.fecha = emergencia.generar_fecha_aleatoria()
        if self.cuerpo_necesario == "Ambulancia":
            self.requiere_medico = "Si"
        else:
            self.requiere_medico = random.choice(["Si", "No"])
        self.contacto = emergencia.fake.phone_number()
    
    @staticmethod
    def generar_fecha_aleatoria():
        start_date = datetime.today().replace(year=datetime.today().year - 1)
        end_date = datetime.today()
        tiempo_entre_fechas = end_date - start_date
        dias_aleatorios = random.randrange(tiempo_entre_fechas.days)
        fecha_aleatoria = start_date + timedelta(days=dias_aleatorios)
        hora_aleatoria = random.randint(0, 23)
        minutos_aleatorios = random.randint(0, 59)
        segundos_aleatorios = random.randint(0, 59)
        fecha_hora_aleatoria = fecha_aleatoria.replace(hour=hora_aleatoria, minute=minutos_aleatorios, second=segundos_aleatorios)
        return fecha_hora_aleatoria
    
    def to_json(self):
        data = self.__dict__.copy()
        data['fecha'] = self.fecha.strftime('%Y-%m-%d %H:%M:%S')
        return json.dumps(data)

class producer_Kafka:
    def __init__(self, server_address, producer_id, producer_topic):
        self.server_address:str = server_address
        self.client_id:str = producer_id
        self.producer_conf = {
            'bootstrap.servers': server_address,
            'client.id': producer_id
        }
        self.producer = Producer(self.producer_conf)
        self.producer_topic:str = producer_topic
    def send_data_to_kafka(self,data):
        def delivery_report(err, msg):
            if err is not None:
                print(f'Message delivery failed: {err}')
            else:
                print(f'Message delivered to {msg.topic()} [{msg.partition()}]')
        self.producer.produce(self.producer_topic,data.encode('utf-8'), callback=delivery_report)
        self.producer.poll(0)
        time.sleep(1)
    def flush_producer(self):
        self.producer.flush()

class consumer_and_producer_Kafka:
    def __init__(self, consumer_server_address, consumer_id, consumer_topic,producer_server_address,producer_id,producer_topic):
        self.consumer_server_address:str = consumer_server_address
        self.consumer_id:str = consumer_id
        self.consumer_topic = consumer_topic
        self.consumer_conf = {
            'bootstrap.servers': consumer_server_address,
            'group.id': consumer_id,
            'auto.offset.reset': 'earliest' 
        }
        self.consumer = Consumer(self.consumer_conf)
        self.consumer_topic:str = consumer_topic
        self.consumer.subscribe([self.consumer_topic])
        
        self.producer_server_address:str = producer_server_address
        self.producer_id:str = producer_id
        self.producer_conf = {
            'bootstrap.servers': producer_server_address,
            'client.id': producer_id
        }
        self.producer = Producer(self.producer_conf)
        self.producer_topic:str = producer_topic
    def processing_messages(self):
        fake = Faker('es_ES')
        try:
            while True:
                msg = self.consumer.poll(1.0)

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
                        mensaje['DIRECCION'] = fake.street_address()
                        self.produce_to_kafka(json.dumps(mensaje))
                        print(f'Mensaje modificado: {mensaje}')
                    else:
                        print(f'Mensaje sin modificación: {mensaje}')
        except KeyboardInterrupt:
            pass
        
        finally:
            self.consumer.close()
            self.flush_producer()
   
    def produce_to_kafka(self, message):
        def delivery_report(err, msg):
            if err is not None:
                print(f'Message delivery failed: {err}')
            else:
                print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

        self.producer.produce(self.producer_topic, message.encode('utf-8'), callback=delivery_report)
        self.producer.poll(0)

    def flush_producer(self):
        self.producer.flush()