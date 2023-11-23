print("Hola mundo")

import requests
import json
import time

respuesta_api = requests.get("https://api.chucknorris.io/jokes/random")

#print(respuesta_api.json())

while True:
    respuesta_api = requests.get("https://api.chucknorris.io/jokes/random")
    data = respuesta_api.json()
    
    with open("/Users/andresrsalamanca/Documents/GitHub/EDEM_MDA2324/Alumnos/ES/ANDRES_RONCANCIO/CHUCK/value.txt" , "a") as file:
        file.write(data["value"] + "\n")
   
    time.sleep(5)
    

    #print (data["value"])
    
