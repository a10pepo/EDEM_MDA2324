print("Hola Mundo")



import requests
import json
import time

response= requests.get("https://api.chucknorris.io/jokes/random")
print(response.json())

while True :
    response = requests.get("https://api.chucknorris.io/jokes/random")
    chiste = response.json()
    with open(r"C:\Users\gabyp\Documents\GitHub\EDEM_MDA2324\Alumnos\ES\Gabriela_Penaherrera\CHUCK\value.txt", "a") as file:
        file.write(chiste["value"] + '\n')

    #time.sleep(5)
    #print(chiste['value'])

    






