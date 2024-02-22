from confluent_kafka.admin import AdminClient, NewTopic

def creacion_topics():
    admin_client = AdminClient({
        "bootstrap.servers": "kafka:29092"
    })
    topic_names = ["T1_Recepcion_avisos", "T2_Centro_112", "T3_No_Urgencias", "T2.1_Sanitarios_112", "T2.2_Centro_de_mando",'T3.1_Medicos', 'T3.2_Bomberos', 'T3.3_Forestales', 'T3.4_Guardia_Costera','T3.5_Policia', 'T3.6_Servicios_de_emergencia' ] 
    new_topics = [NewTopic(topic, num_partitions=1, replication_factor=1) for topic in topic_names]
    futures = admin_client.create_topics(new_topics)
    for topic, future in futures.items():
        try:
            future.result()  
            print(f"Topic {topic} creado con éxito.")
        except Exception as e:
            print(f"No se pudo crear el topic {topic}: {e}")