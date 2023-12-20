import requests

def obtener_datos():
    url = 'https://randomuser.me/api'

    respuesta = requests.get(url)
    datos = respuesta.json()["results"][0]["name"]

    nombre = datos["first"]
    apellidos = datos["last"]

    print(f'El nombre completo del usuario es: {nombre} {apellidos}')

obtener_datos()
