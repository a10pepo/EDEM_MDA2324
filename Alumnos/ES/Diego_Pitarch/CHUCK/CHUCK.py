import requests
import time

url = 'https://api.chucknorris.io/jokes/random'

try:
    while True:
        response = requests.get(url)

        # Verifica si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Procesa la respuesta en formato JSON
            data = response.json()
            print("Chiste de Chuck Norris:", data['value'])
        else:
            # Muestra un mensaje de error si la solicitud no fue exitosa
            print(f'Error en la solicitud. Código de estado: {response.status_code}')

        # Espera 3 segundos antes de hacer la siguiente solicitud
        time.sleep(3)

except KeyboardInterrupt:
    # Maneja la interrupción del teclado (Ctrl+C) para salir del bucle
    print("¡Bucle interrumpido por el usuario!")
    



