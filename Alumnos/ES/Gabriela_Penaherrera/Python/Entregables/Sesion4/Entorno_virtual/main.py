import requests 
respuesta = requests.get('https://randomuser.me/api') 
json = (respuesta.json())

datos_informativos = json['results'][0]
nombre = datos_informativos ['name']['first']
apellido = datos_informativos['name']['last']

print(f'El nombre y apellido es: {nombre} {apellido}')