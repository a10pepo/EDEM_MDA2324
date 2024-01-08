from confluent_kafka.admin import AdminClient , NewTopic
admin_client = AdminClient({
    "bootstrap.servers": "localhost:9092"
})

# Obtiene la lista de tópicos
topics = admin_client.list_topics().topics

# Imprime la lista de tópicos, excluyendo los tópicos internos
print("Lista de Tópicos (excluyendo tópicos internos):")
for topic in topics:
    if not topic.startswith("_"):  # Filtra tópicos que no comienzan con "_"
        print(topic)