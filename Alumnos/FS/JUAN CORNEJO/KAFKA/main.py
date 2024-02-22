from KP_2_Creacion_topics import creacion_topics
from KP_3_Creacion_streams_KSQL import creacion_streams
from KP_4_Productor_inicial import activar_productor_inicial
from KP_5_Consumidor_y_productor import activar_consumidor_productor
import time
import threading

print("Por favor, espera unos segundos")
time.sleep(30)
creacion_topics()
time.sleep(15)
creacion_streams()

produccion = threading.Thread(target=activar_productor_inicial)
cons_y_prod = threading.Thread(target=activar_consumidor_productor)

produccion.start()
cons_y_prod.start()

produccion.join()
produccion.join()