print('Hola Mundo')


# para instalar las bibliotecas: pip install requests
import requests
import json

# En este script, primero importamos las bibliotecas requests y json para realizar solicitudes HTTP y analizar la respuesta JSON, 
# respectivamente. Luego, definimos la URL de la API y hacemos una solicitud GET utilizando la función requests.get(). 
# La respuesta se almacena en la variable response, y luego usamos la función json.loads() para analizar el contenido de la respuesta 
# en formato JSON. Finalmente, imprimimos el valor del chiste aleatorio utilizando la clave value del diccionario data.
# Para guardar el texto que hago del API pongo: 

# Listado= []

from requests.models import Response
url= 'https://api.chucknorris.io/jokes/random'
response= requests.get(url)
data = json.loads(response.text)
print(data['value'])

# listado.append(data['value'])
 #print(Listado)

 #API EN BUCLE.

#Primero crear el bucle para sacar chistes:

if(n_jokes < 11 and n_jokes > 0):
    for n in range(n_jokes)
    response= requests.get(url)
    data = json.loads(response.text)
    chuck_jockes



