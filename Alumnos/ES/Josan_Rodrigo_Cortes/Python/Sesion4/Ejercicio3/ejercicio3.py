""" Ejercicio 3
Realiza una petición HTTPs a la ruta https://randomuser.me/api y muestra por consola el nombre y los
 apellidos retornados por la API
 """

import requests
import json

url = "https://randomuser.me/api"

respuesta = requests.get(url)


datos=respuesta.json()
results=datos['results']
#Lo he hecho de esta forma primero porque me cuesta menos pensar a donde quiero entrar, aunque despues
# lo he conseguido anidando los diferentes índices.

# datos1=results[0]
# name=datos1['name']
# nombre=name['first']
# apellido=name['last']
# print(datos)
# print('---------------------')
# print(results)
# print('---------------------')
# print(datos1)
# print('---------------------')
# print(name)
# print('---------------------')
# print(f' Nombre: {nombre}')
# print(f' Apellido: {apellido}')

resultsNombre=datos['results'][0]['name']['first']
resultsApellido=datos['results'][0]['name']['last']
print(f' Nombre: {resultsNombre}')
print(f' Apellido: {resultsApellido}')



