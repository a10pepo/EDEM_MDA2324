import requests
import time
print('Hello world!')

file = open("./CHUCKO/Results/chucky.txt", "a")
url = "https://api.chucknorris.io/jokes/random"

for i in range(5):
    # Esperar 5 segundos entre iteraciones
    time.sleep(5)
    print(i)
    # Crear una solicitud para la API
    response = requests.get(url)

    # Accede al json clave: "value" (diccionario)
    joke = response.json()["value"]

    # Escribe el chiste en el .txt
    file.write(joke + "\n")
