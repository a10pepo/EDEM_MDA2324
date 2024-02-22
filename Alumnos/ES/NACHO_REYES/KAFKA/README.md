Realizo este .md para poder explicar cual es mi caso de uso del entregable de Kafka. Este, hace referencia a la obtención de datos sobre las coordenadas de un vehículo que comite en el Dakar 2024 (ahora que esta en curso) a través de un sensor de posicionamiento.

Además de indicar la longitud y la latitud del punto donde se encuentra el vehículo, se envía un Id único de cada uno de los registros y también el nombre del punto de control por el que se ha circulado la última vez.

La forma del json empleado ha sido la siguiente:

```json
{
    "id_coord": 'X',
    "latitud": 'X',
    "longitud": 'X',
    "punto_control": 'X'
    }
```

Además, después de haber ejecutado el docker-compose, se ha realizado unas breves consultas ksql para comprobar cual puede ser una de las utilidades y facilidades de obtención y consulta de la información recopilada.