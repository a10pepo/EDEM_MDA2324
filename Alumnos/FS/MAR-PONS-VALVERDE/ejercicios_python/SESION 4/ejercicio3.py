#Realiza una petición HTTPs a la ruta https://randomuser.me/api y 
#muestra por consola el nombre y los apellidos retornados por la API

import requests
import json

from requests.models import Response
url= 'https://randomuser.me/api/'
response= requests.get(url) #aqui realizo la solicitud GET a la API
data = json.loads(response.text) # le digo que me devuelva los datos en formato JSON.

results=data.get('results', []) #extraigo nombre y apellidos del usuario
if results:
    user=results[0]
    name=user.get('name', {}).get('first')
    last_name=user.get('name', {}).get ('last')
    print(f'name: {name}')
    print(f'last_name: {last_name}')
else:
    print('we don´t find users results.')

