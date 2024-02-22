from kfunctions import kconsumer, kproducer
from confluent_kafka import Consumer, KafkaError
import json
        
config = {
        'bootstrap.servers': 'localhost:9092',  
        'group.id': 'python-consumer-group',
        'auto.offset.reset': 'earliest'  
}
consumer = Consumer(config)
consumer.subscribe(["buy"])
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
            # Mostrar el mensaje recibido
            message = msg.value().decode('utf-8')
            print('Oportunidad de compra detectada: {}'.format(message))
            
except KeyboardInterrupt:
    pass
finally:
    consumer.close()

