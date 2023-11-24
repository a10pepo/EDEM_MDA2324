print("Hola Mundo")

import requests
import json
import time
#response_api = requests.get("https://api.chucknorris.io/jokes/random")

#print(response_api.json)

while True:
    response_api = requests.get("https://api.chucknorris.io/jokes/random")
    data = response_api.json()
    with open("/Users/carlosbuenrostrovalverde/Documents/GitHub/EDEM_MDA2324/Alumnos/ES/CARLOS_BUENROSTRO_VALVERDE/CHUCK/value.txt", "a") as file:
        file.write(data["value"] + "\n")
    time.sleep(5)

    print(data["value"])