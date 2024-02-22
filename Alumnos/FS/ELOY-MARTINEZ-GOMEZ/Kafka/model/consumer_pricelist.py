from confluent_kafka import Consumer, KafkaError, Producer
import json
        
config = {
        'bootstrap.servers': 'localhost:9092',  
        'group.id': 'python-consumer-group',
        'auto.offset.reset': 'earliest'  
}
consumer = Consumer(config)
consumer.subscribe(["pricelist"])

producer = Producer(config)

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
            print('Pricelist AAPL: {}'.format(message))
            message = json.loads(message)
            
            # VARIATIONS
            variation_ex = (message["high"]/message["low"]-1)*100
            variation_in = (message["close"]/message["open"]-1)*100
            variations_message = {
                "id": message['id'],
                "variation_ex": variation_ex,
                "variation_in": variation_in
            }
            producer.produce(topic="variations", value=json.dumps(variations_message).encode('utf-8'))
            print('---------- Variaciones enviadas al topic VARIATIONS ----------')
            
            # ALERTS
            if message['close'] >= 195: # id 76
                alerts_message = {
                    "id": message['id'],
                    "close": message['close'],
                    "volume": message['volume'],
                    "transaction": message['transaction']
                }
                producer.produce(topic='alerts', value=json.dumps(alerts_message).encode('utf-8'))
                print('---------- Alerta enviada al topic ALERTS ----------')
            
            
except KeyboardInterrupt:
    pass
finally:
    consumer.close()

