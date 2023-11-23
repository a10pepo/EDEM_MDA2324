import requests
import json
import time
print("Descargando bromas de Chuck Norris...")

url = "https://api.chucknorris.io/jokes/random"

with open("chuck/results/results.txt","a") as f:
    for i in range(10):
        time.sleep(3)
        response = requests.get(url)
        la_broma = response.json()["value"]
        f.write(la_broma + "\n")
