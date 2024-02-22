Hola Rubén, este es mi postwork. He utilizado los conocimientos de clase para leer un libro al completo.

Esto es lo que he hecho:
    1. He importado un libro en formato txt. 
    2. He creado un topic llamado "ALQUIMISTA" 
    3. Lo he producido a traves de mi producer.py 
    4. He leído todo lo que había producido en el producer en una terminal con este código: docker-compose exec kafka kafka-console-consumer --topic ALQUIMISTA --from-beginning --bootstrap-server localhost:9092    
    5. He abierto Ksql. 
    6. Por último, he realizado algunas querys (hay capturas de pantalla).

Pd: Al principio, creo que hice algo mal ya que me salen demasiados topics.