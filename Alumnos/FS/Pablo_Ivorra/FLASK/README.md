# API de Medición de Sensores de Robot 🤖

Este proyecto consiste en una API que ofrece datos de medición en tiempo real de sensores de un robot. La API se ha desarrollado utilizando Flask y se basa en una especificación Swagger que define su estructura y funcionalidad.

## Especificación Swagger

La especificación Swagger es el punto de partida para entender cómo funciona la API. Define los puntos finales disponibles, los parámetros necesarios y las respuestas esperadas. En este caso, la especificación Swagger es:

- Ruta `/getLastMeassureBySensor/{sensor}` para obtener la última medición por ID de sensor.
- Parámetro `sensor` en la ruta, que es el ID del sensor.
- Respuestas: 200 (éxito), 400 (sensor no encontrado), 404 (ID no válido).

## Desarrollo de la API con Flask

La API se ha desarrollado utilizando Flask, un framework de Python. El código de la aplicación Flask se encarga de manejar las solicitudes y respuestas de la API. Utiliza datos ficticios de sensores para proporcionar respuestas simuladas.

## Pruebas con Insomnia

He usado Insomnia para probar la API, una herramienta que facilita la realización de solicitudes a la API y la comprobación de las respuestas. He creado solicitudes para diferentes sensores y he verificado que la API responda correctamente a las solicitudes, tanto en casos exitosos como en escenarios de error.
