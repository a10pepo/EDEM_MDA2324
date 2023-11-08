#Realiza una petición HTTPs a la ruta https://randomuser.me/api y muestra por consola el nombre y los apellidos retornados por la API

import requests
from requests.models import Response

URL: str = "https://randomuser.me/api"

def peticionUser ():
    
    respuesta: requests.Response = requests.get(url = URL)
    estado: int = respuesta.status_code
    datos = respuesta.json()
    
    if estado == 200:
        sexo = datos['results'][0]['name']['title']
        nombre = datos['results'][0]['name']['first']
        apellido = datos['results'][0]['name']['last']
        print(f'El usuario random se llama: {sexo} {nombre} {apellido}')
          
peticionUser()