# Abecedario ordenado por recurrencia de aparición:
import csv

palabras = []

with open('palabras.csv') as csvfile:
    words = csv.reader(csvfile, delimiter=',')
    for row in words:
        for word in row:
            palabras.append(word.lower())


totalintentos=0

for palabra in palabras:
    abecedario=['e','a','o','s','r','n','i','d','l','c','t','u','m','p','b','g','v','y','q','h','f','z','j','ñ','x','k','w']
    
    huecos=len(palabra)
    intentos=0
    while huecos>0:

        for letraabc in abecedario:
            veces = palabra.count(letraabc)
            if veces>=1:               
                huecos-=veces
                intentos+=1
                abecedario.remove(letraabc)
                break
            else:
                abecedario.remove(letraabc)
                intentos+=1
                break  
    totalintentos+=intentos 

print(f'Usando un alfabeto ordenado por frecuencia de aparición de letra, el programa necesita {totalintentos} intentos para adivinar las palabras:{palabras}')
                

                
                
         
  

 