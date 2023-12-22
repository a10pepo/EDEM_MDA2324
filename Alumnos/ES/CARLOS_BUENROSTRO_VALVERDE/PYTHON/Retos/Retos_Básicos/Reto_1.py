# Reto 1: Desde tu cuenta de replit.com crea un nuevo proyecto. En dicho proyecto, dentro 
# del archivo main.py crea variables que representen los siguientes datos de un contacto:
# Una vez hayas creado todas las variables, muéstralas por consola haciendo uso 
# de la función print().

nombre = "Carlos"
apellidos = "Buenrostro Valverde"
edad = 28
email = "cbuenrostrovalverde@gmail.com"
telefono = 696295383
casado = False
con_hijos = False
lista_amigos = ["Pablo,", "Alejandro", "Javi", "Borja"]
peliculas_vistas = {
    "titulo": "Spiderman",
    "titulo_2" : "Spiderman_2",
    "titulo_3" : "Bienvenidos a Zombieland",
    "titulo_4" : "El Señor de los Anillos"}

print(f'{nombre}, {apellidos}, {edad}, {email}, ¿está casado? {casado}, ¿tiene hijos? {con_hijos}')
for n in lista_amigos:
  print(n)
for p, t  in peliculas_vistas.items():
  print(f"{p}: {t}")