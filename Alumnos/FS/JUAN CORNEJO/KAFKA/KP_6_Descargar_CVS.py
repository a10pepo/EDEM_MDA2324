from confluent_kafka import Consumer, KafkaError
import json

#POR COMIDAD, MODIFICA AQUÍ TU URL DE DESCARGA
nombre_archivo_AvisosTotales = r'G:\Mi unidad\EDEM\PRUEBAS KAFKA\TOTAL_AVISOS.json'
nombre_archivo_AvisosSanitarios112 = r'G:\Mi unidad\EDEM\PRUEBAS KAFKA\TOTAL_AVISOS_SANITARIOS_112.json'

#DESCARGAR FICHERO JSON TOPIC 1 - AVISOS TOTALES
# Configuración del consumidor
config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'python-consumer-group 99999',
    'auto.offset.reset': 'earliest'
}

# Crear un consumidor
consumer = Consumer(config)

# Suscribirse a un tópico
topic = 'T1_Recepcion_avisos'
consumer.subscribe([topic])

# Lista para almacenar los mensajes
mensajes = []

# Número de intentos sin recibir mensajes antes de salir del bucle
intentos_maximos = 10
intentos_actuales = 0

# Consumir mensajes del topic
try:
    while intentos_actuales < intentos_maximos:
        msg = consumer.poll(1.0)  # Tiempo de espera de 1 segundo
        
        if msg is None:
            intentos_actuales += 1
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # Fin de la partición alcanzado
                continue
            else:
                print("Error al recibir mensaje: {}".format(msg.error()))
        else:
            # Decodificar el mensaje y agregarlo a la lista
            # Asumiendo que los mensajes están en formato JSON
            try:
                mensaje_decodificado = json.loads(msg.value().decode('utf-8'))
                mensajes.append(mensaje_decodificado)
                intentos_actuales = 0  # Restablecer los intentos al recibir un mensaje
            except json.JSONDecodeError as e:
                print(f"Error al decodificar el mensaje: {e}")

except KeyboardInterrupt:
    pass
finally:
    # Cerrar el consumidor
    consumer.close()

# Guardar en JSON


try:
    with open(nombre_archivo_AvisosTotales, 'w', encoding='utf-8') as file:
        json.dump(mensajes, file, ensure_ascii=False, indent=4)

    print(f"Se han guardado {len(mensajes)} mensajes en {nombre_archivo_AvisosTotales}")
except Exception as e:
    print(f"Error al guardar el archivo: {e}")


#DESCARGAR FICHERO JSON TOPIC 2.1 - SANITARIOS 112
# Configuración del consumidor
config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'python-consumer-group 999999',
    'auto.offset.reset': 'earliest'
}

# Crear un consumidor
consumer = Consumer(config)

# Suscribirse a un tópico
topic = 'T2.1_Sanitarios_112'
consumer.subscribe([topic])

# Lista para almacenar los mensajes
mensajes = []

# Número de intentos sin recibir mensajes antes de salir del bucle
intentos_maximos = 10
intentos_actuales = 0

# Consumir mensajes del topic
try:
    while intentos_actuales < intentos_maximos:
        msg = consumer.poll(1.0)  # Tiempo de espera de 1 segundo
        
        if msg is None:
            intentos_actuales += 1
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # Fin de la partición alcanzado
                continue
            else:
                print("Error al recibir mensaje: {}".format(msg.error()))
        else:
            # Decodificar el mensaje y agregarlo a la lista
            # Asumiendo que los mensajes están en formato JSON
            try:
                mensaje_decodificado = json.loads(msg.value().decode('utf-8'))
                mensajes.append(mensaje_decodificado)
                intentos_actuales = 0  # Restablecer los intentos al recibir un mensaje
            except json.JSONDecodeError as e:
                print(f"Error al decodificar el mensaje: {e}")

except KeyboardInterrupt:
    pass
finally:
    # Cerrar el consumidor
    consumer.close()

# Guardar en JSON

try:
    with open(nombre_archivo_AvisosSanitarios112, 'w', encoding='utf-8') as file:
        json.dump(mensajes, file, ensure_ascii=False, indent=4)

    print(f"Se han guardado {len(mensajes)} mensajes en {nombre_archivo_AvisosSanitarios112}")
except Exception as e:
    print(f"Error al guardar el archivo: {e}")