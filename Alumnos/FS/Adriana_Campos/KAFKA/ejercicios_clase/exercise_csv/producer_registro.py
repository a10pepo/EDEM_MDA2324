import time
from json import dumps
from confluent_kafka import Producer
import csv

# Configuración del productor
config = {
    'bootstrap.servers': 'localhost:9092',  # Cambia esto con la dirección de tu servidor Kafka
    'client.id': 'python-producer'
}

# Crear un productor
producer = Producer(config)

topic_kafka = 'readcsv'

# Cambia el nombre del archivo CSV según tu necesidad
csv_file = '/Users/adrianacamposnarvaez/Documents/GitHub/EDEM_MDA2324/Alumnos/FS/Adriana_Campos/KAFKA/ejercicios_clase/exercise_csv/Final_Transaction.csv'

count = 0

with open(csv_file, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    header = None
    for row in csv_reader:
        if not row:
            continue  # Ignorar líneas vacías

        # Use the first row as headers
        if header is None:
            header = row
            continue

        # Create a dictionary with column names as keys and row values as values
        row_data = dict(zip(header, row))

        # Convert the dictionary to a JSON string
        json_data = dumps(row_data)

        time.sleep(2)
        print(json_data + "\n")

        # Send the entire row as a single message (JSON format)
        data_bytes = json_data.encode('utf-8')  # Encode string to bytes
        key = str(count)
        producer.produce(topic=topic_kafka, value=data_bytes, key=key)  # Send bytes
        count += 1

        # After your loop where you send messages:
        producer.flush()

# Optionally, you can check if there are any messages that failed to be delivered:
if producer.flush() != 0:
    print("Some messages failed to be delivered")