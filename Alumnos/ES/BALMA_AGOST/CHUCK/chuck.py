print("hola mundo")


import requests
import time 

url = 'https://api.chucknorris.io/jokes/random'
response = requests.get(url)

import requests
import time

url = 'https://api.chucknorris.io/jokes/random'

try:
    while True:
        # Realiza una solicitud GET a la API
        response = requests.get(url)

        # Verifica si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Procesa la respuesta en formato JSON
            data = response.json()
            print(data['value'])
        else:
            # Muestra un mensaje de error si la solicitud no fue exitosa
            print(f'Error en la solicitud. Código de estado: {response.status_code}')

        # Espera 3 segundos antes de hacer la siguiente solicitud
        time.sleep(3)

except KeyboardInterrupt:
    # Maneja la interrupción del teclado (Ctrl+C) para salir del bucle
    print("¡Bucle interrumpido por el usuario!")

with open("results.txt", "a") as f:
 
# las comillas value para acceder solo a esa parte
    response = requests.json()["value"]
# Escribe el chiste en el archivo txt
    f.write(response+ "\n")



