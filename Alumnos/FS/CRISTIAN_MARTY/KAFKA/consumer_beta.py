import time
from confluent_kafka import Consumer, KafkaError
from json import loads

class MeteorologiaRealTimeConsumer:
    def __init__(self, bootstrap_servers='localhost:9092', group_id='python-consumer-group', auto_offset_reset='earliest'):
        self.config = {
            'bootstrap.servers': bootstrap_servers,
            'group.id': group_id,
            'auto.offset.reset': auto_offset_reset
        }
        self.consumer = Consumer(self.config)
        self.topic_consumer = 'METEOROLOGIA_BI_STREAM'
        self.city_data = {}

    def subscribe_to_topic(self):
        self.consumer.subscribe([self.topic_consumer])

    def print_bar(self, value, max_value):
        bar_length = 20
        scaled_value = int((value / max_value) * bar_length)
        return '*' * scaled_value + '-' * (bar_length - scaled_value)

    def process_message(self, msg_json):
        city = msg_json['NOMBRE_CIUDAD']
        temperature = msg_json.get('TEMPERATURA', 0)
        humidity = msg_json.get('HUMEDAD', 0)
        wind_speed = msg_json.get('VELOCIDAD_VIENTO', 0)

        self.city_data[city] = {'Temperature': temperature, 'Humidity': humidity, 'Wind Speed': wind_speed}

        # Limpiar la consola
        print("\033c")

        # Imprimir gráfico de barras en tiempo real
        for city, data in self.city_data.items():
            print(f"{city}:")
            print(f"   Temperatura: {self.print_bar(data['Temperature'], 40)} {data['Temperature']}°C")
            print(f"   Humedad:    {self.print_bar(data['Humidity'], 100)} {data['Humidity']}%")
            print(f"   Viento:  {self.print_bar(data['Wind Speed'], 40)} {data['Wind Speed']} km/h")
            print("\n")

    def consume_messages(self):
        try:
            while True:
                msg = self.consumer.poll(1.0)  # Lee nuevos mensajes cada 1 segundo

                if msg is not None:
                    if msg.error():
                        if msg.error().code() == KafkaError._PARTITION_EOF:
                            print("No hay más mensajes en esta partición.")
                        else:
                            print("Error al recibir mensaje: {}".format(msg.error()))
                    else:
                        # Procesar el mensaje recibido.
                        msg_value_str = msg.value().decode('utf-8')

                        # Deserializar el mensaje JSON
                        msg_json = loads(msg_value_str)

                        # Procesar el mensaje
                        self.process_message(msg_json)

                        # Esperar antes de la próxima actualización
                        time.sleep(1)

        except KeyboardInterrupt:
            pass
        finally:
            # Cerrar el consumidor al detener la aplicación Python
            self.consumer.close()

if __name__ == "__main__":
    meteorologia_consumer = MeteorologiaRealTimeConsumer()
    meteorologia_consumer.subscribe_to_topic()
    meteorologia_consumer.consume_messages()
