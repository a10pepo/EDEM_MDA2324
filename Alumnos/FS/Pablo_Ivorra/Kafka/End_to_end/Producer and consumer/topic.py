from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka.admin import KafkaError

# Configura la conexión con el servidor Kafka
bootstrap_servers = 'localhost:9092'  # Cambia esto con la dirección de tu servidor Kafka

# Crea una instancia del administrador de Kafka
admin_client = AdminClient({'bootstrap.servers': bootstrap_servers})

# Define la configuración del nuevo topic (con el nombre 'pricelist')
new_topic = NewTopic('pricelist', num_partitions=1, replication_factor=1)

# Intenta crear el topic utilizando el administrador
fs = admin_client.create_topics([new_topic])

# Espera a que se complete la creación del topic
for topic, f in fs.items():
    try:
        f.result()  # Espera hasta que se complete la operación o maneja excepciones
        print(f"Topic '{topic}' creado exitosamente.")
    except KafkaError as e:
        print(f"Error al crear el topic '{topic}': {e}")
    except Exception as e:
        print(f"Otro error: {e}")

# Cierra la conexión con el administrador de Kafka
admin_client.close()

