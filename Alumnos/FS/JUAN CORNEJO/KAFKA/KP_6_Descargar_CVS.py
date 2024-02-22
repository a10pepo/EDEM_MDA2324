from confluent_kafka import Consumer, KafkaError
import json

nombre_archivo_AvisosTotales = r'G:\Mi unidad\EDEM\PRUEBAS KAFKA\TOTAL_AVISOS.json'
nombre_archivo_AvisosSanitarios112 = r'G:\Mi unidad\EDEM\PRUEBAS KAFKA\TOTAL_AVISOS_SANITARIOS_112.json'

config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'python-consumer-group 99999',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(config)
topic = 'T1_Recepcion_avisos'
consumer.subscribe([topic])
mensajes = []
intentos_maximos = 10
intentos_actuales = 0
try:
    while intentos_actuales < intentos_maximos:
        msg = consumer.poll(1.0)
        if msg is None:
            intentos_actuales += 1
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print("Error al recibir mensaje: {}".format(msg.error()))
        else:
            try:
                mensaje_decodificado = json.loads(msg.value().decode('utf-8'))
                mensajes.append(mensaje_decodificado)
                intentos_actuales = 0
            except json.JSONDecodeError as e:
                print(f"Error al decodificar el mensaje: {e}")

except KeyboardInterrupt:
    pass
finally:
    consumer.close()



try:
    with open(nombre_archivo_AvisosTotales, 'w', encoding='utf-8') as file:
        json.dump(mensajes, file, ensure_ascii=False, indent=4)

    print(f"Se han guardado {len(mensajes)} mensajes en {nombre_archivo_AvisosTotales}")
except Exception as e:
    print(f"Error al guardar el archivo: {e}")


config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'python-consumer-group 999999',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(config)
topic = 'T2.1_Sanitarios_112'
consumer.subscribe([topic])
mensajes = []
intentos_maximos = 10
intentos_actuales = 0

try:
    while intentos_actuales < intentos_maximos:
        msg = consumer.poll(1.0)
        
        if msg is None:
            intentos_actuales += 1
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print("Error al recibir mensaje: {}".format(msg.error()))
        else:
            try:
                mensaje_decodificado = json.loads(msg.value().decode('utf-8'))
                mensajes.append(mensaje_decodificado)
                intentos_actuales = 0
            except json.JSONDecodeError as e:
                print(f"Error al decodificar el mensaje: {e}")

except KeyboardInterrupt:
    pass
finally:
    consumer.close()


try:
    with open(nombre_archivo_AvisosSanitarios112, 'w', encoding='utf-8') as file:
        json.dump(mensajes, file, ensure_ascii=False, indent=4)

    print(f"Se han guardado {len(mensajes)} mensajes en {nombre_archivo_AvisosSanitarios112}")
except Exception as e:
    print(f"Error al guardar el archivo: {e}")