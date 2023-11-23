# REQUERIMIENTOS PREVIOS
import requests
from requests.models import Response
import nltk
nltk.download ('punkt')
nltk.download ('averaged_perceptron_tagger')
import time
URL : str = "https://api.chucknorris.io/jokes/random"
lista_chistes = []
diccionario_conteo_sustantivos ={}

#CREACIÓN FUNCIÓN
def chistes_Chuck_norris (numero_chistes):
    #LLAMADA A LA API
    for numero in range (numero_chistes):
            respuesta : Response = requests.get(URL)
            datos = respuesta.json()
            frase_chuck: str = datos["value"]
            lista_chistes.append(frase_chuck)

    for chiste in lista_chistes:
        print (f'\n - {chiste}\n')
    print (f'Se han escrito {len(lista_chistes)} chistes')
    #IDENTIFICAR SUSTANTIVOS
    is_noun = lambda pos: pos[:2] == 'NN'
    tokenized = nltk.word_tokenize(' '.join(lista_chistes)) 
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 
    #CONTEO DE SUSTANTIVOS
    for word in nouns:
     diccionario_conteo_sustantivos [word] = 0
    for word in nouns:
        if word in diccionario_conteo_sustantivos:
            diccionario_conteo_sustantivos [word] += 1  
        else:
            diccionario_conteo_sustantivos [word] = 1 
    #IMPRIMIR LISTA DE SUSTANTIVOS MÁS VISUAL
    lista_sustantivos_ordenada = dict(sorted(diccionario_conteo_sustantivos.items(),key=lambda item: item[1], reverse=True))
    print("\nLISTA DE SUSTANTIVOS:")
    print("-" * 40)
    print("{:<20} {:<20}".format("Sustantivo", "Frecuencia"))
    print("-" * 40)
    for sustantivo, frecuencia in lista_sustantivos_ordenada.items():
        print("{:<20} {:<20}".format(sustantivo, frecuencia))
    #BUCLE PARA QUE SE REPITA Y ACUMULE CADA 5 SEGUNDOS. SE AUTOPARA EN 10. 
while True:
    chistes_Chuck_norris(1)
    time.sleep(5)
    if diccionario_conteo_sustantivos.get("Chuck", 0) >= 10 or diccionario_conteo_sustantivos.get("Norris", 0) >= 10:
        print ("Final de la prueba")
        break
    
chistes_Chuck_norris()