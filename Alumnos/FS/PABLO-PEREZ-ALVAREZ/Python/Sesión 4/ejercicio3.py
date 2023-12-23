import requests

import requests

def obtener_datos_usuario():
    url = "https://randomuser.me/api"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos_usuario = respuesta.json()["results"][0]["name"]
        return datos_usuario
    else:
        print(f"Error al hacer la petición: {respuesta.status_code}")
        return None

if __name__ == "__main__":
    datos_usuario = obtener_datos_usuario()

    if datos_usuario:
        print("Nombre:", datos_usuario["first"])
        print("Apellido:", datos_usuario["last"])