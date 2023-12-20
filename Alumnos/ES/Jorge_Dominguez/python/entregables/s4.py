#A partir de las respuestas a los dos últimos ejercicios de la Sesión 3:
#Crea una función que reciba un rango de números como parámetro y muestre por consola únicamente los valores primos
#Crea una función que pueda evaluar si un número (pasado por parámetro) es primo o no
#Crea una función que reciba un año y pueda indicarte con True o False si es un año bisiesto o no.

def es_primo(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))

def mostrar_primos_en_rango(inicio, fin):
    primos = [num for num in range(inicio, fin + 1) if es_primo(num)]
    print(f'Números primos de {inicio} a {fin}:')
    print(*primos)

def es_bisiesto(anyo):
    return (anyo % 4 == 0 and anyo % 100 != 0) or (anyo % 400 == 0)

mostrar_primos_en_rango(1, 100)

numero_evaluar = 53
if es_primo(numero_evaluar):
    print(f'{numero_evaluar} es un número primo.')
else:
    print(f'{numero_evaluar} no es un número primo.')

anio_evaluar = 2024
if es_bisiesto(anio_evaluar):
    print(f'{anio_evaluar} es un año bisiesto.')
else:
    print(f'{anio_evaluar} no es un año bisiesto.')
    
#Crea un proyecto Plantilla de Python que disponga de un archivo requirements.txt y un .venv que pueda ser ejecutado desde Visual Studio Code
#Realiza una petición HTTPs a la ruta https://randomuser.me/api y muestra por consola el nombre y los apellidos retornados por la API

import requests

url='https://randomuser.me/api'
response = requests.get(url)
data = response.json()
user_info = data['results'][0]['name']
first_name = user_info['first']
last_name = user_info['last']
print(f"Nombre y apellidos: {first_name} {last_name}")
