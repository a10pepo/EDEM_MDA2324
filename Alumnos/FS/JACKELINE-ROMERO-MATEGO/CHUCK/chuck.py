import requests
import spacy
import time

#FUNCIÓN PARA SEPARAR SUSTANTIVOS CON SPACY

def separar_sustantivos(texto):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(texto)
    sustantivos = [token.text for token in doc if token.pos_ == "NOUN"]
    return sustantivos

#LLAMADA A LA API DE CHUCK NORRIS

def api_chuck_norris(): 
    accumulated_nouns = {}  
    
    for i in range(10):
        url = 'https://api.chucknorris.io/jokes/random'
        response = requests.get(url)
    
        if response.status_code == 200:
            #El código 200 nos dice que la solicitud fue exitosa
            datos = response.json()
            joke = datos["value"]
            # print("Chiste:", joke)
    
            noun_joke = separar_sustantivos(joke)
            #print("Sustantivos en el chiste:", noun_joke)

            #Bucle que recorre cada sustantivo 
            for sustantivo in noun_joke:
                accumulated_nouns[sustantivo] = accumulated_nouns.get(sustantivo, 0) + 1
    
        else:
            print(f"Error. Código de estado: {response.status_code}")

        time.sleep(10)
    
    print("Diccionario de sustantivos y frecuencias:", accumulated_nouns)

api_chuck_norris()
