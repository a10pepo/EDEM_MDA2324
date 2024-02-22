from confluent_kafka.admin import AdminClient, NewTopic

admin_config = {
    'bootstrap.servers': 'localhost:9092',
}

admin_client = AdminClient(admin_config)


topic_list = [NewTopic("marketcap_filtro", num_partitions=3, replication_factor=1)]

# Crear el tópico
fs = admin_client.create_topics(topic_list)


for topic, f in fs.items():
    try:
        f.result()  
        print("Tópico {} creado".format(topic))
    except Exception as e:
        print("Falló la creación del tópico {}: {}".format(topic, e))
