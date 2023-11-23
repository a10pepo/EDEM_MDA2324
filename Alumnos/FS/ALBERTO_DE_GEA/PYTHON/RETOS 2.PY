#RETO 1
nombre = "Alberto"
apellidos = "De Gea"
edad = 23
email = "albertopla1966@gmail.com"
telefono = 689628823

Soltero = True
Casado = False

Hijos = False
NoHijos = True

misAmigos = ["Jorge", "Miguel", "y Alejandro"]

peliculas_vistas = {
  2020: "El Padrino",
  2022: "Sin tiempo para morir"
}
año1 = 2022
pelicula1 = "Sin tiempo para morir"
pelicula = peliculas_vistas[año1]
año2 = 2020
pelicula2 = "El Padrino"
pelicula = peliculas_vistas[año2]

print(f'Hola mi nombre es {nombre} {apellidos}. Tengo {edad} años. '
  f'Mi correo electrónico es {email} y mi número {telefono}.'
  f'{"Estoy soltero" if Soltero else "Soy casado"}.'
  f'{"No tengo hijos" if Hijos else "Tengo hijos"}.'
  f'Mis amigos son ' + ', '.join(misAmigos)+'.'
  f'Mis peliculas favoritas son {pelicula1} y {pelicula2} y las vi en los años {año1} y {año2}.')

#RETO 2
"Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final."

"Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]"



listanumerosImpares = []
listanumerosPares = []

for numero in range(2,8):
  if numero % 2 != 0:
    listanumerosImpares.append(numero)


for numero in range(2,8):
  if numero % 2 == 0:
    listanumerosPares.append(numero)
    
print("Impares:")
for impar in listanumerosImpares:
  print(f'{impar}')
print("Pares:")
for par in listanumerosPares:
  print(f'{par}')

#reto 3
"Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso**.**"
miRange = (1,101)
listamisNumeros = []
for numero in range (101, 0, -1):
  if numero %1 == 0:
    listamisNumeros.append(numero)

print("Numeros Inversos:")
for numero in listamisNumeros:
  print(f'{numero}')

#Reto 4

"Escribe un programa que sea capaz de mostrar los elementos de una lista en orden inverso al original. Por ejemplo: teniendo [1,2,3,4,5] el programa debe mostrar por pantalla [5,4,3,2,1]"

miLista = [1,2,3,4,5]
miLista.reverse()
print(miLista)

# Reto 5
"""Escribe un programa que sea capaz de pedirle a un usuario por consola** que introduzca una contraseña y mientras que ésta no sea "admin", el programa seguirá pidiéndola

Si la contraseña es errónea, deberá sacarle un mensaje de error y volver a pedirle la contraseña hasta que la introduzca bien. Si el usuario introduce "admin" correctamente, el programa le deberá mostrar un mensaje "Bienvenido al programa señor ADMIN" y luego terminar.

NOTA: Para pedir por pantalla y guardarlo en una variable llamada password debes hacer uso de password:str = input('Introduce una contraseña')"""

while True:
  password = input('Introduce una contraseña: ')
  if password == 'admin':
      print('Bienvenido al programa, señor ADMIN')
      break
  else:
      print('Contraseña incorrecta. Inténtalo de nuevo.')

#Reto 6
"Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no."

while True:
  edad = input('Que edad tienes?')
  if int(edad) >= 18:
    print("Entonces eres mayor de edad")
    break
  else:
    if int(edad) < 18:
      print("Entonces eres menor de edad")
    break
    
#Reto 7
"Escribe un programa que contenga dos variables. Una de ellas representa la contraseña de un usuario y la otra un texto introducido. El programa debe poder mostrar por pantalla si las dos cadenas de texto son iguales sin tener en cuenta mayúsculas y minúsculas."

myPassword = "admin"

while True:
  password = input('User password: ')
  myPassword = password.lower()
  password = password.lower()
  if password == 'admin':
      print('Bienvenido, sr. ADMIN')
      break
  else:
      print('Contraseña incorrecta. Inténtalo de nuevo.')

#Reto 8

"Escribe un programa que pueda decirte si un número (número entero) es primo o no"

def primo(num):
 if num < 2: 
   return False
 for i in range(2, num): 
   if num % i == 0: 
    return False
 return True 

for _ in range(5):
  num = int(input("Introduce un numero: "))
  if primo(num):
    print("El numero es primo.")
  else: 
    print("El numero no es primo.")

#Reto 9
"Escribe un programa que pueda decirte si un año (número entero) es bisiesto o no"


def bisiesto(year):
  if (year% 4 == 0 and year%100 != 0) or (year % 400 == 0):
    return True
  else:
    return False

for num in range(1900, 2500):
  if bisiesto(num):
    print(f"{num} es bisiesto")

for _ in range(5):
  num = int(input("Introduce un año: "))
  if bisiesto(num):
    print("El año es bisiesto.")
  else: 
    print("El año no es bisiesto.")

#Reto 10 y Reto 11

"Escribe un programa que guarde en una variable el siguiente contenido"

"luego"
"Escribe un programa que pida al usuario los siguientes datos por consola"
"Título de la película"
"Director"
"Año"
"País"
"E introduzca esos valores en una variable GLOBAL llamada pelicula"

# Guardamos el diccionario en una variable llamada 'contenido'
contenido = {
    'titulo': 'El Más Allá',
    'aka': 'E tu vivrai nel terrore - Laldilà',
    'director': 'Lucio Fulci',
    'año': 1981,
    'país': 'Italia'
}

# Función para pedir datos al usuario y crear el diccionario 'pelicula'
def obtener_datos_pelicula():
    global pelicula  # Declarando la variable 'pelicula' como global para que sea accesible fuera de la función
    pelicula = {}  # Inicializamos un diccionario vacío
    pelicula['titulo'] = input("Título de la película: ")
    pelicula['director'] = input("Director: ")
    pelicula['año'] = int(input("Año: "))
    pelicula['país'] = input("País: ")

# Llamamos a la función para obtener los datos
obtener_datos_pelicula()

# Imprimimos el diccionario 'pelicula'
print("La película ingresada es:")
print(pelicula)

# Reto 12

#Escribe un programa que almacene en una lista (Array) todos los nombres de los alumnos del curso Programación para No Programadores y los muestre en por pantalla.

miLista = ['Alberto', 
  'Sergi',
  'Miguel',
  'Alejandro',
  'Sara',
  'Jose María',
  'Jorge'
]

print("Alumnos del curso:")
for alumnos in miLista:
  print(alumnos)