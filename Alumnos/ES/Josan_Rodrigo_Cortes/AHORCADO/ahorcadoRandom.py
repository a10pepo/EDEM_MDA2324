import random
import csv


palabras = []

with open('palabras.csv') as csvfile:
    words = csv.reader(csvfile, delimiter=',')
    for row in words:
        for word in row:
            palabras.append(word.lower())
   
print(palabras)

totalintentos=0

for palabra in palabras:
    abcedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","y","z"]
    huecos=len(palabra)
    longitudABC=len(abcedario)
    intentos=0
    while huecos>0:        
        letraAzar= random.choice(abcedario)
        for letra in palabra:
            veces = palabra.count(letraAzar)
            if veces>=1:               
                huecos-=veces
                intentos+=1
                abcedario.remove(letraAzar)
                break
            else:
                abcedario.remove(letraAzar)
                intentos+=1
                break  
    totalintentos+=intentos 
print(f'Usando letras generadas al azar, el programa necesita {totalintentos} intentos para adivinar las palabras:{palabras}')
                
    
        
