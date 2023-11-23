print("Hola mundo")

import requests
import json 
import time

#response_API = requests.get('https://api.chucknorris.io/jokes/random')
#print(response_API.json())

while True:
    response_API = requests.get('https://api.chucknorris.io/jokes/random')
    joke_data = response_API.json()

    with open('C:\Users\hugof\OneDrive\Documentos\GitHub\EDEM_MDA2324\Alumnos\ES\HUGO_MARIA\CHUCK\value.txt', 'a') as file:
        file.write(joke_data['value'] + '\n')

    time.sleep(5)

