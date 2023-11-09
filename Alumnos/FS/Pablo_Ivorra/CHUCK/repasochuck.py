
import requests
from requests.models import Response
URL : str = "https://api.chucknorris.io/jokes/random"

lista_chistes = []

#DEFINICIÓN DE FUNCIÓN
def chistes_Chuck_norris ():
    f = open("results.txt", "w")
    for numero in range (1,11):
                respuesta : Response = requests.get(URL)
                datos = respuesta.json()
                frase_chuck: str = datos["value"]
                f.write(f'{frase_chuck}\n')

#EJECUCIÓN DE FUNCIÓN
chistes_Chuck_norris()
