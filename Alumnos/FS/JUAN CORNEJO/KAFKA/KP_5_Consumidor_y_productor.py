from KP_1_Definicion_clase import consumer_and_producer_Kafka

def activar_consumidor_productor():
    consumer_and_producer_1 = consumer_and_producer_Kafka(
        'kafka:29092','python-consumer-group-99','T2_Centro_112',
        'kafka:29092','python-producer2','T2.1_Sanitarios_112'
    )

    consumer_and_producer_1.processing_messages()