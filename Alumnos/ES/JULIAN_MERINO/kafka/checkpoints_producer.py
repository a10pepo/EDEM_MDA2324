import csv
from confluent_kafka import Producer, KafkaException
import json

# Función para el producer
def create_producer(bootstrap_servers):
    """Crea una instancia del productor Kafka."""
    conf = {
        'bootstrap.servers': bootstrap_servers,
        'client.id': 'python_producer'
    }
    return Producer(conf)

# Función para leer el csv con los checkpoints
def read_checkpoint_csv(file_path):
    """Lee del csv los checkpoints de Kilian Jornet y Courtney Dauwalter."""
    data = []

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    return data

if __name__ == "__main__":
    # Kafka bootstrap server (fuera de la red de Docker)
    bootstrap_servers = 'localhost:9092'

    # Kafka topic
    topic = 'checkpoints_log'

    # Crea la instancia del productor Kafka
    producer = create_producer(bootstrap_servers)

    try:
        # Lee los datos del csv
        checkpoint_data = read_checkpoint_csv('./utmb_kj_cd_times.csv')

        for row in checkpoint_data:
            # Extrae datos de la fila del CSV
            elap_distance = float(row['elap_distance'])
            kj_checkpoint = row['kj']
            cd_checkpoint = row['cd']

            # Genera los JSON para Kilian y Courtney
            cd_json = {
                'runner_id': 'Courtney Dauwalter',
                'team': 'Salomon',
                'current_checkpoint': cd_checkpoint,
                'elap_distance': elap_distance
            }

            kj_json = {
                'runner_id': 'Kilian Jornet',
                'team': 'NNormal',
                'current_checkpoint': kj_checkpoint,
                'elap_distance': elap_distance
            }

            # Produce mensajes para Kilian y Courtney
            producer.produce(topic, key='Courtney Dauwalter', value=json.dumps(cd_json))
            print(f"Produced message for Courtney Dauwalter: Elapsed Distance: {elap_distance}, Elapsed Time: {cd_checkpoint}")

            producer.produce(topic, key='Kilian Jornet', value=json.dumps(kj_json))
            print(f"Produced message for Kilian Jornet: Elapsed Distance: {elap_distance}, Elapsed Time: {kj_checkpoint}")

        producer.flush()
        producer.poll(1)

        # Comprueba errores
        if producer.flush(10):
            print("Some messages haven't been delivered...")
        else:
            print("All messages delivered.")

    except KafkaException as e:
        print(f"Kafka Exception: {e}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Asegura que se envía el último mensaje del productor antes de cerrarlo
        producer.flush()
