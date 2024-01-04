# ***************************** RETOS BÁSICOS *****************************

# Reto 1: Desde tu cuenta de replit.com crea un nuevo proyecto. En dicho proyecto, dentro 
# del archivo main.py crea variables que representen los siguientes datos de un contacto:
# # Una vez hayas creado todas las variables, muéstralas por consola haciendo uso 
# # de la función print().

# nombre = "Carlos"
# apellidos = "Buenrostro Valverde"
# edad = 28
# email = "cbuenrostrovalverde@gmail.com"
# telefono = 696295383
# casado = False
# con_hijos = False
# lista_amigos = ["Pablo,", "Alejandro", "Javi", "Borja"]
# peliculas_vistas = {
#     "titulo": "Spiderman",
#     "titulo_2" : "Spiderman_2",
#     "titulo_3" : "Bienvenidos a Zombieland",
#     "titulo_4" : "El Señor de los Anillos"}

# print(f'{nombre}, {apellidos}, {edad}, {email}, ¿está casado? {casado}, ¿tiene hijos? {con_hijos}')
# for n in lista_amigos:
#   print(n)
# for p, t  in peliculas_vistas.items():
#   print(f"{p}: {t}")

# # Reto 2: Escribe un programa capaz de mostrar todos los números impares desde un número 
# # de inicio y otro final.


# # Reto 3: Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden 
# # inverso**.**

# lista_numeros = list(range(0,101))

# lista_numeros_reversed = list(reversed(lista_numeros))

# print(lista_numeros_reversed)


# # Reto 4: Escribe un programa que sea capaz de mostrar los elementos de una lista 
# # en orden inverso al original.

# lista_numeros_2 = list(range(0, 11))

# lista_numeros_2_reversed = list(reversed(lista_numeros_2))

# print(lista_numeros_2_reversed)

# # Reto 5: Programa por consola que pida contraseña. Es admin. 

# password = "admin"

# print("Introduzca contraseña por favor: ")

# while input() != password:
#     print("ERROR. Introduzca la contraseña correcta por favor.")
# else:
#   print("Bienvenido al programa señor ADMIN")


# # Reto 6: Escribe un programa que pregunte al usuario su edad y muestre por pantalla si
# # es mayor de edad o no.

# print("Bienvenido al programa. Introduzca su edad, por favor")

# edad = int(input())

# if edad >= 18:
#   print("Eres mayor de edad. Puedes acceder al programa.")
# else:
#   print("Lo siento, no puedes acceder al siguiente programa.")

# # Reto 7: Escribe un programa que tenga dos variables. Una de ellas representa la contraseña de 
# # un usuario y la otra un texto introducido. El programa debe poder mostrar por
# # pantalla si las dos cadenas de texto son iguales sin tener en cuenta mayus o minus.

# user_password = "contraseña"
# texto = input("Para cambiar su contraseña, introduzca la antigua: ")

# if user_password == texto.lower():
#   print("Las contraseñas son iguales.")
# else:
#   print("Las contraseñas no son iguales.")

# Reto 8: Escribe un programa que pueda decirte si un número (numero entero) es primo o no.
# def es_primo(num):
#   for n in range(2, num):
#       if num % n == 0:
#           print("No es primo", n, "es divisor")
#           return False
#   print("Es primo")
#   return True

# Reto 9: Escribe un programa que pueda decirte si un año (número entero) es bisiesto o no

# def leap_year():
#     year: int = int(input("Intruduzca el año: "))
#     if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#         print(f'El {year} es bisiesto')
#     else:
#         print(f'El {year} no es bisiesto. Pruebe con otra fecha.')

# leap_year()

# Reto 10: Escribe un programa que guarde en una variable el siguiente contenido: {'titulo':'El Más Allá','aka':'E tu vivrai nel terrore - Laldilà','director':'Lucio Fulci', 'año':1981, 'país':'Italia'}

# pelicula: dict = {'titulo':'El Más Allá',
#                   'aka':'E tu vivrai nel terrore - Laldilà',
#                   'director':'Lucio Fulci',
#                   'año':1981,
#                   'país':'Italia'}

# print(pelicula)

# Reto 11: Escribe un programa que pida al usuario los siguientes datos por consola:
# def crear_peli():
#     pelicula = dict()
#     pelicula['Título'] = input("Introduzca el nombre de la película: ")
#     pelicula['Director'] = input("Introduzca el nombre del director: ")
#     pelicula['Año'] = int(input("Introduzca el año de la película: "))
#     pelicula['País'] = input("Introduzca el país de la película: ")

# crear_peli()
# print('pelicula')

# Reto 12: Escribe un programa que almacene en una lista (Array) todos los nombres de los alumnos del curso Programación para No Programadores y los muestre en por pantalla.
# lista_alumnos = ['Carlos', 'Luis', 'Diego', 'Balma', 'Andrés', 'Hugo']

# for n in lista_alumnos:
#     print(n)

# Reto 13: Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.
# import math
# def area_triangulo():
#     partes = dict()
#     partes['Base'] = float(input("Introduzca la base (cm) del triángulo: "))
#     partes['Altura'] = float(input("Introduzca la altura (cm) del triángulo: "))
#     print((partes['Altura']*partes['Base'])/2)

# def area_circulo(radio):
#     return(math.pi*(radio**2))

# Reto 14: Escribe una función que use la función del área del círculo para devolver el volumen de un cilindro, obteniendo por parámetro la longitud del mismo.

# Reto 15: Escribe una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
# def cuadrados(lista):
#     for numero in lista:
#         print(numero**2)
# lista = [1, 2, 3, 4, 5, 6]

# cuadrados(lista)

# Reto 16: Crea un script que sea capaz de restar dos fechas y muestra el resultado por consola
# from datetime import datetime
# nacimiento = datetime(1995, 2, 9, 15, 0, 0)
# diferencia = datetime.now() - nacimiento
# print(diferencia)

# Reto 17: Partiendo de la siguiente tupla = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
# Realiza las siguientes operaciones:
# tupla = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
# # Encontrar los elementos de 3 a 5
# print(tupla[3 : 6])
# # Encontrar los 6 primeros elementos
# print(tupla[0 : 6])
# # Muestra la tupla desde el 5 elemento hasta el final
# print(tupla[5 : ])
# # Muestra toda la tupla haciendo uso de [:]
# print(tupla[ : ])
# # Muestra todos los elementos desde la posición 2 a la 9 de dos en dos
# print(tupla[1 : 8 : 2])
# # Devuelve la tupla con un salto cada 4 elementos
# print(tupla[ :  : 2])
# # Usa un step negativo para mostrar la tupla desde la posición 9 a la 2
# print(tupla[8 : 1 : -1])

# Reto 18: Crea una función que sea capaz de eliminar un caracter concreto de una cadena de texto. La función debe tener la siguiente firma:
# def eliminar(str, n):
#     principio = str[: n]
#     final = str [n + 1 :]
#     return principio + final

# def solucion():
#     print(eliminar('Madrid', 0))
#     print(eliminar('Madrid', 2))
#     print(eliminar('Madrid', 5))

# ***************************** RETOS INTERMEDIOS Y AVANZADOS *****************************

# Reto 1: Tienda de discos musicales.
# from datetime import datetime

# discos = [
#     {
#         "Nombre" : "21st Century Breakdown",
#         "Artista" : "Green Day",
#         "Año" : "2009",
#         "Precio" : 19.99,
#         "Género" : "Rock"

#     },
#     {
#         "Nombre" : "Sin Noticias de Holanda",
#         "Artista" : "Melendi",
#         "Año" : 2003,
#         "Precio" : 17.99,
#         "Género" : "Pop"
#     }
#     ,
#     {
#         "Nombre" : "Summoning",
#         "Artista" : "Stronghold",
#         "Año" : 1999,
#         "Precio" : 18.99,
#         "Género" : "Black Metal"
#     },
#     {
#         "Nombre" : "Grey With Breaks",
#         "Artista" : "Lowfish",
#         "Año" : 2003,
#         "Precio" : 12.99,
#         "Género" : "Electro"
#     }]

# def calculo_descuento(precio, descuento):
#     genero = discos['genero']
#     if genero == "Black Metal" or genero == "Electro":
#         return precio * 0.3
#     else:
#         return 0

# print("Discos disponibles:")
# for idx, disco in enumerate(discos, start=1):
#     print(f"{idx}. {disco['Nombre']} - {disco['Artista']} - Género: {disco['Género']} - Precio: ${disco['Precio']}")

# ticket = []
# ahorro = 0

# while True:
#     seleccion = input("Bienvenido al programa. Elija un disco para comprar o pulse 0 para salir.")
#     if seleccion == 0:
#         break
#     try:
#         seleccion = int(seleccion)
#         if 1 <= seleccion <= len(discos):
#             disco_elegido = discos[seleccion -1]
#             ticket.append(disco_elegido)
#             descuento = calculo_descuento(disco_elegido['Precio']), disco_elegido['Género']
#             ahorro =+ descuento
#             print(f'Has seleccionado {disco_elegido["Nombre"]} a tu compra')
#         else:
#             print('Pulsa un botón correcto.')
#     except ValueError:
#         print('Selecciona un número válido.')

# total_ticket = sum(discos['Precio'] for disco in ticket) - ahorro
# fecha_compra = datetime.now()

# print('--- Ticket de compra ---')
# print(f'Fecha de la compra: {fecha_compra}')
# print(f'Descuento total de la compra: {descuento}')
# print(f'El total de la compra ha sido: {total_ticket}')

# Reto 2: El programa debe preguntar el artículo y su precio y añadirlo a una variable (diccionario u objeto literal), hasta que el usuario decida terminar ("Introducir otro elemento al carrito (Si / No)".
# Una vez el usuario decida no introducir más elementos al carrito, debe mostrar por pantalla la lista de la compra y el coste total.
