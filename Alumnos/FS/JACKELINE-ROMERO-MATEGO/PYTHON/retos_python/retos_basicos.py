#RETO 1: Una vez hayas creado todas las variables, muéstralas por consola haciendo uso de la función print().

"""Nombre = "Jackeline"
Apellidos = "Romero Matego"
Edad = 26
Email = "jackelinerommat@gmail.com"
Teléfono = "680477911"
Casado = False
Con_hijos = False
Lista_amigos = ['Ivan', 'Julia', 'Maria']
Peliculas_vistas = ['Juegos del hambre', 'Spiderman']

print (Nombre,Apellidos,Edad,Email,Teléfono,Casado,Con_hijos,Lista_amigos,Peliculas_vistas)"""

#RETO 2: Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.

"""lista_impares = []
lista_pares = []

for num in range (1, 101):
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)
        
print(lista_impares)"""

#RETO 3: Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.

"""number = list(range(100))

number.reverse()

print(number)"""

#RETO 5: Escribe un programa que sea capaz de pedirle a un usuario por consola** 
#que introduzca una contraseña y mientras que ésta no sea "admin", el programa seguirá pidiéndola
#Si la contraseña es errónea, deberá sacarle un mensaje de error y volver a pedirle la contraseña hasta que
#la introduzca bien. Si el usuario introduce "admin" correctamente, el programa le deberá mostrar un mensaje
# "Bienvenido al programa señor ADMIN" y luego terminar.

    
"""Password = str(input("Introduce tu contraseña\n"))
Password2 = "admin"

while Password != Password2:
    respuesta  = input("La contraseña es incorrecta. Intentándolo de nuevo o escribe 'exit' para salir.\n")
    if respuesta == Password2:
        print("Bienvenido al programa señor ADMIN")
        exit ()
    elif respuesta == "exit":
        break
    else: 
        print(respuesta)
        
if Password == Password2:
        print("Bienvenido al programa señor ADMIN")
        exit()"""

#RETO 6: Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

"""Age = int(input("¿Cuál es tu edad?\n"))

if Age >= 18:
    print("Es mayor de edad.")

else:
    print("Es menor de edad.")"""

"""RETO 7: Escribe un programa que contenga dos variables. 
Una de ellas representa la contraseña de un usuario y la otra un texto introducido. 
El programa debe poder mostrar por pantalla si las dos cadenas de texto son iguales 
sin tener en cuenta mayúsculas y minúsculas.

variable1 = "Hola Mundo"
variable2 = "hola mundo"

if variable1.lower() == variable2.lower():

    print ("Las cadenas de texto son iguales.")

else:
    print ("Las cadenas de texto no son iguales.")"""

#RETO 10: Escribe un programa que guarde en una variable el siguiente contenido:

"""diccionary = {'titulo':'El Más Allá','aka':'E tu vivrai nel terrore - Laldilà','director':'Lucio Fulci', 'anyo':1981, 'país':'Italia'}

print (diccionary['titulo'])
print (diccionary['aka'])
print (diccionary['director'])
print (diccionary['anyo'])
print (diccionary['país'])"""

#RETO 11: Escribe un programa que pida al usuario los siguientes datos por consola:

"""Título de la película
Director
Año
País
E introduzca esos valores en una variable GLOBAL llamada "pelicula"""

"""#Definimos la variable 'pelicula' como un diccionario para poder introducir todos los datos

pelicula = {}

def datos_pelicula():
    
    pelicula["title"] = input("Introduce el título de la película: ")
    pelicula["year"] = input("Introduce el año de la película: ")
    pelicula ["director"] = input("Introduce el director de la película: ")
    pelicula ["country"] = input("Introduce el país de la película: ")

#Llamamos a la función para meter los datos

datos_pelicula()

print("DATOS DE LA PELÍCULA:")
print("Título:", pelicula["title"])
print("Año:", pelicula["year"])
print("Director:", pelicula["director"])
print("País:", pelicula["country"])"""

# RETO 12: Escribe un programa que almacene en una lista (Array) 
# todos los nombres de los alumnos del curso Programación para No Programadores
# y los muestre en por pantalla.

"""students = ["Elena", "Alejandro", "Camila", "Lucas", "Isabella", "Martín", "Valentina", "Sebastián", "Sofía", "Mateo"]

print("Alumnos del curso Programación para No Programadores:")

for name in students:
    print(name)"""
    
#RETO 13: Escribe una función que calcule el área de un triángulo, 
# recibiendo la altura y la base como parámetros y otra función 
# que calcule el área de un círculo recibiendo el radio del mismo.

"""def triangle_area(b, h):
    area = (b * h) / 2
    return area

result_triangle_area = triangle_area(4, 10)
print ("El área del triángulo es:" , result_triangle_area)

# Importamos 'math' para obtener la constante π

import math

def circle_area(r):
    result = math.pi * r**2
    return result

result_circle_area = circle_area(3)
print ("El área del círculo es:", result_circle_area)"""

#RETO 14: Escribe una función que use la función del área del círculo para devolver el volumen de un cilindro, 
# obteniendo por parámetro la longitud del mismo.

"""import math

def circle_area(r):
    result = math.pi * r**2
    return result

def cylinder_vol(r, h):
    area_base = circle_area(r)
    volum = float(area_base * h)
    return volum

result_cylinder_vol = float(cylinder_vol(3, 5))
print ("El volumen del cilindro es:", result_cylinder_vol,"m3")"""

#RETO 15: Escribe una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

"""def mi_funcion(lista):
    resultado = [numero ** 2 for numero in lista]
    return resultado

lista_numeros = [2,4,6,8,10]

lista_al_cuadrado = mi_funcion(lista_numeros)

print (f"La lista original es: {lista_numeros}")
print (f"Los cuadrados de la lista son: {lista_al_cuadrado}")"""

#RETO 16: Crea un script que sea capaz de restar dos fechas y muestra el resultado por consola.

"""from datetime import datetime, date, time, timedelta

hoy = datetime.now().date()

dentro_de_dos_semanas = hoy + timedelta(weeks=2)

resultado = dentro_de_dos_semanas - hoy

print(resultado)"""

#RETO 17: Partiendo de la siguiente tupla, realiza las siguientes operaciones:

"""tupla = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)

# Encontrar los elementos de 3 a 5

print(tupla[3:6])

# Encontrar los primeros 6 elementos

print(tupla[:6])

# Muestra la tupla desde el 5 elemento hasta el final

print(tupla[5:])

# Muestra toda la tupla

print(tupla[:])

# Muestra todos los ementos desde la posición 2 a la 9 de dos en dos

print(tupla[2:9:2])

# Devuelve la tupla con un salto cada 4 elementos

print(tupla[::4])

# Usa un step negativo para mostrar la tupla desde la posición 9 a la 2

print(tupla[::-1])"""

#RETO 18: Crea una función que sea capaz de eliminar un caracter concreto de una cadena de texto. 

"""def eliminar_caracter(cadena, indice):
    
    # cadena: de texto
    # indice: indice del caracter que queremos eliminar
    
    return cadena[:indice] + cadena[indice +1:]

print(eliminar_caracter("Madrid", 0))
print(eliminar_caracter("Madrid", 1))
print(eliminar_caracter("Madrid", 2))
print(eliminar_caracter("Madrid", 3))
print(eliminar_caracter("Madrid", 4))
"""