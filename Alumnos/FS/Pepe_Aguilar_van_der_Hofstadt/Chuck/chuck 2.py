import requests
import pandas as pd

class Sustantivo:
    palabra:str
    veces:int

    def __init__(self, _palabra):
        self.palabra = _palabra
        self.veces = 1
    
    def suma_vez(self):
        self.veces += 1

    def reset(self):
        self.veces = 0




def random_chuck_norris_joke(url: str) -> str:      # Extrae una broma random de chuck norris

    respuesta = requests.get(url)
    estado: int = respuesta.status_code
    datos = respuesta.json()
    if estado == 200 and estado < 300:
        chuck_joke: str = datos['value']
        return(chuck_joke)
    else:
        print(f'error {estado}')
    
def separa_sustantivos(joke:str, todos_sustantivos) -> list:       # separa los sustantivos del resto del chiste
    sustantivos = []
    broma_separada = joke.split()
    for palabra in broma_separada:
        for sust in todos_sustantivos:
            if(palabra.lower() == sust):  
                sustantivos.append(palabra)
    return(sustantivos)

def cuenta_sustantivos(sustantivos_chiste:list):    # Mete en una lista los sustantivos y los cuenta
    for palabra in sustantivos_chiste:
        meter_nuevo = True
        for sust in lista_sustantivos:
            if(sust.palabra == palabra):
                meter_nuevo = False
                sust.suma_vez()
        if(meter_nuevo == True):
            sustantivo_nuevo = Sustantivo(palabra)
            lista_sustantivos.append(sustantivo_nuevo)
            

             


sustantivos_df = pd.read_csv('nounlist.csv', header=None, names=['sustantivos'])
palabras = sustantivos_df['sustantivos'].str.strip('"').tolist()

lista_sustantivos = []

URL:str = 'https://api.chucknorris.io/jokes/random'

txt = open("./results.txt", "w")

for n in range(1000):
    broma = random_chuck_norris_joke(URL)
    sustativos = separa_sustantivos(broma, palabras)
    cuenta_sustantivos(sustativos)

for palabras in lista_sustantivos:
    txt.write(f'{palabras.palabra},{palabras.veces};')

txt.close()











