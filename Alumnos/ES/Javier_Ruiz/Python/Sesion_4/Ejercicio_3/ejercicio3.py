import requests

def obtener_datos_usuario():
    datos_usuario = requests.get("https://randomuser.me/api").json()
    nombre = datos_usuario['results'][0]['name']
    print("Nombre:", nombre['first'])
    print("Apellido:", nombre['last'])

obtener_datos_usuario()