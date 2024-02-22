# Proyecto Kafka
Para utilizar KAFKA y aprovechar la virtud de mensajería en tiempo real, se ha escogido un caso de uso que pueda encajar en esa necesidad. 
El caso de uso es el sistema de alertas de emergencias y 112.

# Proceso general
El proceso entero de generación de información, producción de mensajería y consumo se ha dockerizado, de tal forma que el docker-compose ya debería levantar todo el proceso. 

Este, se puede ver en el siguiente flujograma:

![Alt text](<Flujograma del proceso.jpeg>)

Los avisos por emergencia llegan a un Topic de entrada, estos se re-dirigen en función del grado de urgencia hacia dos topics distintos. Los casos No Urgentes son re-dirigidos a sus respectivas áreas. Aquellos que sí son urgentes, son analizados. Si necesitan un médico (o el cuerpo necesario es Médicos), se consulta la dirección de destino para poder enviar la ambulacia y se envía al Topic de Sanitarios 112. En caso de no necesitar ambulancia, se envían al Topic del Centro de Mando.


No obstante, el proceso de consumo, almacenamiento y descarga de los resultados en formato JSON se ha realizado de forma externa por facilidad y flexibilidad en cuanto a la carpeta de descarga.

**IMPORTANTE**: Una vez ejecutado el docker-compose, el proceso puede tardar unos minutos entre que se levanta y crea todo el sistema y se empiezan a enviar mensajes. Cabe recordar que por limitaciones de conocimiento mio, aunque en la realidad este proceso sería instanteno, al estar dentro de un mismo docker el proceso se ejecuta de forma secuencial, por lo que, hasta que no se han enviado todos los mensajes (250, 1 cada segundo), no se empiezan a consumir, modificar y enviar al tramo final. Se puede comprobar la evolución mediante el comando "docker-compose logs script_python". De la misma forma, se puede comprobar también en la interfaz del Control Center "http://localhost:9021/clusters".

# Proceso detallado e inventario de archivos de la carpeta:
* **Dockerfile** - Almacena la información para generar la imagen que copie todos los scripts necesarios y arranque el script main.py
* **Docker-compose** - Contiene todos los contenedores necesarios para ejecutar el proceso (sin incluir la descarga y visualización de resultados en Power BI, partes que, por facilidad y flexibilidad, están por fuera del proceso.)
* **KP_1_Definicion_clase**: Se define los atributos y caracteristicas de la clase "Emergencia"
* **KP_2_Creacion_topics**: Se crean los topics necesarios para el flujo de información.
* **KP_3_Creacion_streams_KSQ**L: Se crean los STREAMS de re-dirección de información mediante KSQL
* **KP_4_Productor_inicial**: Se generan los registros en base a la definición de la clase y se envían al Topic asignado.
* **KP_5_Consumidor_y_productor**: Consume la información del Topic T2.Centro_112, se comprueba si necesita un médico y en caso afirmativo, se añade una dirección aleatoria. Posteriomente, se produce la información y se envía al Topic T2.1_Sanitarios_112
* **KP_6_Descargar_CVS**: Descarga la información en formato json. Se ejecuta por fuera del docker-compose.
* **TOTAL_AVISOS**: json con la información de todos los avisos recibidos en el Topic 1 descargada tras haber ejecutado el proceso.
* **TOTAL_AVISOS_SANITARIOS_112**: json con la información de todos los avisos médicos. Este fichero sirve para comprobar que todo el proceso se ha ejecutado de forma correcta. Se puede comprobar que los avisos en este fichero también existen en el general, solo que en ese no incluyen la dirección.
* **Analisis_emergencias.pbix** : PowerBi con una visualización sencilla e ilustrativa de cómo se podrían reflejar los resultados.
* **Main.py**: Para buscar la mayor facilidad y lectura, este fichero únicamente contiene importaciones y las cuatro funciones globales para ejecutar el proceso.
* **Requirements.txt**: Librerias externas utilizadas y necesarias para arrancar el proceso.

NOTA: Adiconalmente, la carpeta cuenta con funcionalidades auxiliares (por favor, tened en cuenta que algunas pueden no estar completamente actualizadas) que han sido necesarias en el proceso de creación, como son Borrar Queries emitidas de SQL; un consumer básico, Comprobar Topics "NO INTERNOS" activos, su borrado etc.

# Otras consideraciones:
* Se ha tenido especial cuidado en la generación de información para que sea lo más realista posible, buscando que exista coherencia entre los eventos, los cuerpos asignados, y la urgencia. (No tiene sentido que el grado de urgencia sea leva y se llame a los GEOS, o que haya un Atraco y se llame a un bombero)
* De la misma forma, para simular el tiempo real y la similitud con la realidad, los eventos se generan de forma cronológica (es decir, el primero mensaje siempre es de una fecha más antigua que el segundo, y así sucesivamente)
* Para garantizar que Kafka se ha levantado antes de comenzar, se ha añadido un time.sleep de 30 segundos al main.py
* Ha sido especialmente costoso la gestión de la comunicación de los productores y consumidores una vez están dockerizados ya que no se puede llamar al localhost (ya que están dentro del container)
* Para activar el docker-compose, revisar que no haya contenedores ni imagenes previas que puedan chocar con esta (contenedores/imagenes con mismo nombre etc.)
* Importante tener en cuenta el rol de group-id a la hora de consumir mensajes para asegurar que se muestran todos.
