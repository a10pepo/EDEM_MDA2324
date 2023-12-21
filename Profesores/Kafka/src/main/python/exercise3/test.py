import kafka
import confluent_kafka

# Проверка доступности KafkaConsumer из библиотеки kafka-python
if hasattr(kafka, 'KafkaConsumer'):
    print("KafkaConsumer доступен")
else:
    print("KafkaConsumer недоступен")

# Проверка доступности Consumer из библиотеки confluent-kafka
if hasattr(confluent_kafka, 'Consumer'):
    print("Consumer доступен")
else:
    print("Consumer недоступен")