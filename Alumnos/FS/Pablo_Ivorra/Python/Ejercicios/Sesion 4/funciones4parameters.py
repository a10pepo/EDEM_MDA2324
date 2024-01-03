
#A partir de las respuestas a los dos últimos ejercicios de la Sesión 3:
#Crea una función que reciba un rango de números como parámetro y muestre por consola únicamente los valores primos
#Crea una función que pueda evaluar si un número (pasado por parámetro) es primo o no
#Crea una función que reciba un año y pueda indicarte con True o False si es un año bisiesto o no.
#Crea un proyecto Plantilla de Python que disponga de un archivo requirements.txt y un .venv que pueda ser ejecutado desde Visual Studio Code
#Realiza una petición HTTPs a la ruta https://randomuser.me/api y muestra por consola el nombre y los apellidos retornados por la API


def mostrar_primos(rango_min, rango_max):
    for numero in range(rango_min, rango_max + 1):
        primo = True
        if numero < 2:
            primo = False
        else:
            for i in range(2, numero):
                if numero % i == 0:
                    primo = False
        if primo:
            print(numero)

# Uso de la función
mostrar_primos(1, 100)

def numero_es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

# Prueba de la función
print(numero_es_primo(11))

def ano_es_bisiesto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Prueba de la función
print(ano_es_bisiesto(2020))

#Request a la API

import requests

def get_random_user():
    r = requests.get('https://randomuser.me/api/')
    data = r.json()
    nombre = data['results'][0]['name']['first']
    apellido = data['results'][0]['name']['last']
    print('El nombre es: ' + nombre + ' y el apellido es: ' + apellido)

# Llamada a la función
get_random_user()
