from confluent_kafka import Consumer, KafkaError
import json

# Configuración del consumidor
consumer_config = {
    'bootstrap.servers': 'localhost:9092',  # Cambia esto con la dirección de tu servidor Kafka
    'group.id': 'my_consumer_group',  # Cambia esto al ID de tu grupo de consumidores
    'auto.offset.reset': 'earliest'
}

# Crea una instancia del consumidor
consumer = Consumer(consumer_config)

# Suscribe al topic "marketcap"
consumer.subscribe(['marketcap'])

try:
    while True:
        # Lee un mensaje de Kafka
        msg = consumer.poll(1.0)

        if msg is None:
            continue

        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print('Llegó al final de la partición')
            else:
                print(f'Error en el mensaje: {msg.error()}')
        else:
            # Procesa el mensaje JSON recibido
            mensaje_json = msg.value().decode("utf-8")
            datos = json.loads(mensaje_json)
            
            # Accede a los valores específicos que necesitas
            usd_info = datos.get("USD")
            
            if usd_info is not None:  # Verifica que "usd_info" no sea None
                total_market_cap = usd_info.get("total_market_cap")
                total_volume_24h = usd_info.get("total_volume_24h")
                total_volume_24h_reported = usd_info.get("total_volume_24h_reported")
                altcoin_market_cap = usd_info.get("altcoin_market_cap")
                altcoin_volume_24h = usd_info.get("altcoin_volume_24h")
                altcoin_volume_24h_reported = usd_info.get("altcoin_volume_24h_reported")
                timestamp = usd_info.get("timestamp")
            
                # Imprime los valores
                print("Total Market Cap:", total_market_cap)
                print("Total Volume 24h:", total_volume_24h)
                print("Total Volume 24h Reported:", total_volume_24h_reported)
                print("Altcoin Market Cap:", altcoin_market_cap)
                print("Altcoin Volume 24h:", altcoin_volume_24h)
                print("Altcoin Volume 24h Reported:", altcoin_volume_24h_reported)
                print("Timestamp:", timestamp)
            else:
                print("El campo 'USD' no está presente en los datos recibidos")

except KeyboardInterrupt:
    pass

finally:
    # Cierra el consumidor
    consumer.close()

