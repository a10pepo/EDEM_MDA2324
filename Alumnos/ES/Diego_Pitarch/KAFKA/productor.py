import time
from json import dumps
from confluent_kafka import Producer

def read_ccloud_config(config_file):
    conf = {}
    with open(config_file) as fh:
        for line in fh:
            line = line.strip()
            if len(line) != 0 and line[0] != "#":
                parameter, value = line.strip().split('=', 1)
                conf[parameter] = value.strip()
    return conf

def read_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()

def print_and_produce_messages(file_path, topic_kafka):
    producer = Producer(read_ccloud_config("postwork.properties"))

    for e, line in enumerate(read_file_content(file_path)):
        # Print the line
        print(line)

        # Send the line as a Kafka message
        data = {'libro.txt': line}
        data_str = dumps(data)
        data_bytes = data_str.encode('utf-8')
        key = str(e).encode('utf-8')
        producer.produce(topic=topic_kafka, value=data_bytes, key=key)
        print("")
        time.sleep(2)  

    
    producer.flush()

    # Optionally, you can check if there are any messages that failed to be delivered:
    if producer.flush() != 0:
        print("Some messages failed to be delivered")

# Reemplaza 'libro.txt' y 'topic_postwork' con las rutas y nombres correctos
print_and_produce_messages('libro.txt', 'topic_postwork')



