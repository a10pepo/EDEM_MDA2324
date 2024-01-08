from confluent_kafka.admin import AdminClient, NewTopic

# Configura la conexión al cluster de Kafka
admin_client = AdminClient({
    "bootstrap.servers": "localhost:9092"  # Asegúrate de usar tus propios servidores aquí
})

# Obtener la lista actual de topics
topic_list = admin_client.list_topics().topics

# Filtrar los topics no internos (que no comienzan con "_")
non_internal_topics = [topic for topic in topic_list if not topic.startswith("_")]

# Borrar los topics no internos
if non_internal_topics:
    delete_futures = admin_client.delete_topics(non_internal_topics)
    for topic, future in delete_futures.items():
        try:
            future.result()  # Bloquea hasta que la eliminación del topic se complete
            print(f"Topic {topic} eliminado con éxito.")
        except Exception as e:
            print(f"No se pudo eliminar el topic {topic}: {e}")
else:
    print("No hay topics no internos para eliminar.")