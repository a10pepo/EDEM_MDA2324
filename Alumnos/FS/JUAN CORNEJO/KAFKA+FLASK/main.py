#IMPORTAR RELACIONES
from KP_2_Creacion_topics import creacion_topics
from KP_3_Creacion_streams_KSQL import creacion_streams
from KP_4_Productor_inicial_API import activar_productor_inicial_API
from KP_5_Consumidor_y_productor import activar_consumidor_productor
import time
import threading

#CREACIÓN ESTRUCTURAS KAFKA
print("Por favor, espera unos segundos")
time.sleep(30) #Para asegurar que Kafka se levanta.
creacion_topics()
creacion_streams()

produccion = threading.Thread(target=activar_productor_inicial_API)
cons_y_prod = threading.Thread(target=activar_consumidor_productor)

produccion.start()
cons_y_prod.start()

produccion.join()
produccion.join()

""" activar_productor_inicial_API()
activar_consumidor_productor() """