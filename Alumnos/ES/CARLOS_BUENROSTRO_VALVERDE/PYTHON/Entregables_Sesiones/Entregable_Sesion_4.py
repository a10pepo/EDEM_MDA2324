# EJERCICIO ENTREGABLE 4
# 4.1

# A partir de las respuestas a los dos últimos ejercicios de la Sesión 3:
# 1. Crea una función que reciba un rango de números como parámetro y muestre por consola únicamente los valores primos
def es_primo():
    num = int(input('Indica el número para comprobar si es primo o no: '))
    if num <= 1:
        print(f'El número {num} no es primo')
        return
    
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            print(f'El número {num} no es primo')
            break
    else:
        print(f'El número {num} es primo')

es_primo()


# 2. Crea una función que pueda evaluar si un número (pasado por parámetro) es primo o no


# 3. Crea una función que reciba un año y pueda indicarte con True o False si es un año bisiesto o no.
def leap_year(year):
    year: int = int(input("Intruduzca el año: "))
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

#4.2
# Crea un proyecto Plantilla de Python que disponga de un archivo requirements.txt y un .venv que pueda ser ejecutado desde Visual Studio Code

# El siguiente ejercicio se realizó en clase junto a Martín. En el resto de la carpeta se puede encontrar los archivos requirements.txt y el .VEMV creado en visual studio.


#4.3
# Realiza una petición HTTPs a la ruta https://randomuser.me/api y muestra por consola el nombre y los apellidos retornados por la API
import requests
import json

respuesta_API = requests.get('https://randomuser.me/api')
if respuesta_API.status_code == 200:
    data = respuesta_API.json()
print(data["results"][0]["name"]["first"], data["results"][0]["name"]["last"])