import time
from json import dumps
from confluent_kafka import Producer
from faker import Faker
from datetime import datetime, timedelta

class MeteorologiaProducer:
    def __init__(self, bootstrap_servers='localhost:9092'):
        self.config = {
            'bootstrap.servers': bootstrap_servers,
            'client.id': 'python-producer'
        }
        self.producer = Producer(self.config)
        self.topic_kafka = 'meteorologia'
        self.faker = Faker('es_ES')

    def generate_meteorological_data(self):
        fecha_hoy = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        fecha_hora_simulada = fecha_hoy + timedelta(
            hours=self.faker.random_int(min=0, max=23),
            minutes=self.faker.random_int(min=0, max=59),
            seconds=self.faker.random_int(min=0, max=59)
        )

        estacion_meteorologica = {
            "id_registro": self.faker.uuid4(),
            "fecha_hora": fecha_hora_simulada.strftime("%Y-%m-%d %H:%M:%S"),
            "nombre_estacion": self.faker.word(),
            "nombre_ciudad": self.faker.city(),
            "temperatura": self.faker.random_int(min=-10, max=30),
            "humedad": self.faker.random_int(min=0, max=100),
            "velocidad_viento": self.faker.random_int(min=0, max=20),
            "direccion_viento": self.faker.random_element(elements=("Norte", "Sur", "Este", "Oeste")),
            "presion_atmosferica": self.faker.random_int(min=950, max=1050),
            "precipitacion": self.faker.random_int(min=0, max=20),
            "visibilidad": self.faker.random_int(min=1, max=10),
            "nubosidad": self.faker.random_int(min=0, max=100),
            "radiacion_solar": self.faker.random_int(min=0, max=1000),
            "indice_uv": self.faker.random_int(min=0, max=10),
            "precipitacion_acumulada": self.faker.random_int(min=0, max=100),
        }
        return estacion_meteorologica

    def send_data_to_kafka(self, data, key):
        data_str = dumps(data)
        data_bytes = data_str.encode('utf-8')
        key_bytes = str(key).encode('utf-8')
        self.producer.produce(topic=self.topic_kafka, value=data_bytes, key=key_bytes)
        print(f"Sending data: {data} to topic {self.topic_kafka}")
        time.sleep(1)

    def flush_producer(self):
        # After your loop where you send messages:
        self.producer.flush()

        # Optionally, you can check if there are any messages that failed to be delivered:
        if self.producer.flush() != 0:
            print("Some messages failed to be delivered")

if __name__ == "__main__":
    meteorologia_producer = MeteorologiaProducer()

    for i in range(1000):
        meteorological_data = meteorologia_producer.generate_meteorological_data()
        meteorologia_producer.send_data_to_kafka(meteorological_data, i)

    meteorologia_producer.flush_producer()
