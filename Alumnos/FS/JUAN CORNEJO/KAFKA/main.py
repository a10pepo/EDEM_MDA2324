#IMPORTAR RELACIONES
from KP_2_Creacion_topics import creacion_topics
from KP_3_Creacion_streams_KSQL import creacion_streams
from KP_4_Productor_inicial import activar_productor_inicial
from KP_5_Consumidor_y_productor import activar_consumidor_productor
import time

#CREACIÓN ESTRUCTURAS KAFKA
print ("Por favor espera hasta que se levanta Kafka")
time.sleep(30) #Para asegurar que Kafka se levanta.
creacion_topics()
creacion_streams()
activar_productor_inicial()
activar_consumidor_productor()