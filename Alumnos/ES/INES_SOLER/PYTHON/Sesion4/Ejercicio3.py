'''
Realiza una petición HTTPs a la ruta https://randomuser.me/api y muestra por consola el nombre y los apellidos retornados por la API
'''

import requests

respuesta = requests.get('https://randomuser.me/api/')
retorno = respuesta.json()
print(f'El nombre es {retorno["results"][0]["name"]["first"]} {retorno["results"][0]["name"]["last"]}')