import requests
respuesta = requests.get('https://randomuser.me/api/')

codigo_http = respuesta.status_code

json_respuesta = respuesta.json()

print(respuesta.status_code)
print(respuesta.text)

# Códigos de ERROR: 200 --> Todo bien
                #   300 --> Problemas de conexión
                #   400 --> Errores del cliente
                    # 404 --> Ruta que no existe en la URL
                    # 403 --> Desde ese ordenador no tienes permisos para entrar (Black List)
                #   500 --> Errores en la aplicación del servidor