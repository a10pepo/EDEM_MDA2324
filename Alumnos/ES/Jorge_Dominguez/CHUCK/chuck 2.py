import requests
import time

print('Hello World')


with open("jokes.txt", "a") as f:

    for i in range(200):
        print(i)
        time.sleep(2)

        # Solicitud a la API
        response = requests.get("https://api.chucknorris.io/jokes/random")

        # las comillas "value" para acceder solo a esa parte
        joke = response.json()["value"]

        # Escribe el chiste en el archivo TXT
        f.write(joke + "\n")