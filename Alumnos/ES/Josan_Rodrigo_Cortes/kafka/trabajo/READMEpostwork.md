
1. Use case
El caso de uso que he elegido para obtener datos en stream es la generación de usuarios aleatorios.
Para ello, el producer.py se conecta a una api que le proporciona usuarios ficticios y lo envía al topic de kafka: 'randomuserdata'. Defino varias variables que almacenan caracteristicas del usuario y el programa las imprime por pantalla.

Desde el mismo topic el consumidor lee los archivos almacenados por el productor en kafka y los imprime, pero añadiendo el string 'Nuevo mensaje:numero'.

2. Dataset selected 
Tras levantar el docker-compose, crear el mismo topic que hay en los scripts y abrir la consola de ksql, vemos que los mensajes del productor pueden imprimirse y el consumidor los lee. Aunque tengo que reconocer que dada la extructura del mensaje, cuando ejecuto querys, no consigo generar la información deseada.

2. Final architecture implemented 

Siguiendo la escructura del Docker-Compose proporcionado desarrollo en python los scripts del productor y del consumidor.

3. Json examples of your data json model 

Ejemplos del productor:
---------------------
 Nombre: Lorik, apellido: Klakegg, pais: Norway, email: lorik.klakegg@example.com y username: angrygoose960
---------------------
 Nombre: Liva, apellido: Johansen, pais: Denmark, email: liva.johansen@example.com y username: brownkoala415

 Ejemplos del consumidor:

Nuevo mensaje:14, Nombre: Noa, Apellido: Fournier, País: France, Email: noa.fournier@example.com, Username: beautifulbear172
Nuevo mensaje:15, Nombre: Priska, Apellido: Durand, País: Switzerland, Email: priska.durand@example.com, Username: bluefrog814
Nuevo mensaje:16, Nombre: Antonio, Apellido: Santiago, País: Spain, Email: antonio.santiago@example.com, Username: silvergoose807


4. **Evidence** of the Application has run end to end providing the expected results. With screenshots of the different step:

Screenshot folder

Josan

