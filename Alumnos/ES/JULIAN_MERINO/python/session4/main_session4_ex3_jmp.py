import requests
import json

respuesta = requests.get('https://randomuser.me/api')
#print(respuesta.text)

names = json.loads(respuesta.text)
print(names["results"][0]["name"]["first"], names["results"][0]["name"]["last"])
#json_respuesta = respuesta.json()