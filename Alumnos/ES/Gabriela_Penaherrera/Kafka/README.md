# Explicacion del Caso
# Define/explain the Target of your application from a Business Point of view.

La aplicacion creada fue acerca de una serie de television llamada Rick and Morty con la finalidad de poder conocer informacion de los personajes para los fanaticos de la serie. El mismo que contenia id, nombre, status, especie, tipo, genero, origen, localidad, imagen, episodios y la fecha de su creacion. 

Se ejecuto primero un docker compose, donde estan cargados los servicios de zookeper, kafka, ksql y ksqlcli para obtener las imagenes y poder configurar tanto el producer y consumer.

Para la obtencion de datos, se utilizo la Api Rick and Morty/Characters, la misma que a traves de un codigo de productor (producer.py) se encargaba de recibir la informacion de la Api y enviarla a traves de mensajes en formato JSON.  Una vez recibida esta informacion, el consumidor (consumer.py) lo procesaba y leia el mensaje en formato JSON para mostrar los campos de interes de la audiciencia como: nombre, especie, genero e imagen del personaje.

A traves de KSQL se realizo queries para identificar el numero de caracteres de cada nombre o ver los personajes de acuerdo a cada especie. 

Al final se pudo evidenciar una aplicacion end to end, donde se pudo obtener los datos, enviar mensajes, leer la informacion, modificarlo y volver a enviar para tener el mensaje final. Al igual que en KSQL se pudo obtener la informacion a traves de queries solicitada. 

Ej. Producer
{"id": 5, "name": "Jerry Smith", "status": "Alive", "species": "Human", "type": "", "gender": "Male", "origin": {"name": "Earth (Replacement Dimension)", "url": "https://rickandmortyapi.com/api/location/20"}, "location": {"name": "Earth (Replacement Dimension)", "url": "https://rickandmortyapi.com/api/location/20"}, "image": "https://rickandmortyapi.com/api/character/avatar/5.jpeg", "episode": ["https://rickandmortyapi.com/api/episode/6", "https://rickandmortyapi.com/api/episode/7", "https://rickandmortyapi.com/api/episode/8", "https://rickandmortyapi.com/api/episode/9", "https://rickandmortyapi.com/api/episode/10", "https://rickandmortyapi.com/api/episode/11", "https://rickandmortyapi.com/api/episode/12", "https://rickandmortyapi.com/api/episode/13", "https://rickandmortyapi.com/api/episode/14", "https://rickandmortyapi.com/api/episode/15", "https://rickandmortyapi.com/api/episode/16", "https://rickandmortyapi.com/api/episode/18", "https://rickandmortyapi.com/api/episode/19", "https://rickandmortyapi.com/api/episode/20", "https://rickandmortyapi.com/api/episode/21", "https://rickandmortyapi.com/api/episode/22", "https://rickandmortyapi.com/api/episode/23", "https://rickandmortyapi.com/api/episode/26", "https://rickandmortyapi.com/api/episode/29", "https://rickandmortyapi.com/api/episode/30", "https://rickandmortyapi.com/api/episode/31", "https://rickandmortyapi.com/api/episode/32", "https://rickandmortyapi.com/api/episode/33", "https://rickandmortyapi.com/api/episode/35", "https://rickandmortyapi.com/api/episode/36", "https://rickandmortyapi.com/api/episode/38", "https://rickandmortyapi.com/api/episode/39", "https://rickandmortyapi.com/api/episode/40", "https://rickandmortyapi.com/api/episode/41", "https://rickandmortyapi.com/api/episode/42", "https://rickandmortyapi.com/api/episode/43", "https://rickandmortyapi.com/api/episode/44", "https://rickandmortyapi.com/api/episode/45", "https://rickandmortyapi.com/api/episode/46", "https://rickandmortyapi.com/api/episode/47", "https://rickandmortyapi.com/api/episode/48", "https://rickandmortyapi.com/api/episode/49", "https://rickandmortyapi.com/api/episode/50", "https://rickandmortyapi.com/api/episode/51"], "url": "https://rickandmortyapi.com/api/character/5", "created": "2017-11-04T19:26:56.301Z"}

Ej. Consumidor
Mensaje recibido: Nombre: Rick Sanchez, Especie:Human, Genero: Male, Imagen: https://rickandmortyapi.com/api/character/avatar/1.jpeg
Mensaje recibido: Nombre: Morty Smith, Especie:Human, Genero: Male, Imagen: https://rickandmortyapi.com/api/character/avatar/2.jpeg
Mensaje recibido: Nombre: Summer Smith, Especie:Human, Genero: Female, Imagen: https://rickandmortyapi.com/api/character/avatar/3.jpeg




