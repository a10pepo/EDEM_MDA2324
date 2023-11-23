import time
import requests
print("Hello World")


# Crea un archivo TXT para guardar los chistes´
with open("joke.txt", "a") as f:

    # Bucles para obtener X chistes de la API

    for i in range(200):
        # Cada 5 segundos
        time.sleep(1)
        print(i)
        
        # Crer solicitud a la API
        response = requests.get("https://api.chucknorris.io/jokes/random")

        # "Value", porque es la parte que necesitamos, el chiste.
        joke = response.json()["value"]

        # Escribe el articulo en el archivo TXT
        f.write(joke + "\n")

    


