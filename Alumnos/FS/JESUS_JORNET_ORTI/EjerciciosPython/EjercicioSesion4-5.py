"""
5. Realiza una petición HTTPs a la ruta https://randomuser.me/api y muestra por 
consola el nombre y los apellidos retornados por la API
"""

import requests

URL = "https://randomuser.me/api"

res = requests.get(URL)
data = res.json()

nombre = data['results'][0]['name']['first']
apellido = data['results'][0]['name']['last']

print(f'{nombre} {apellido}')