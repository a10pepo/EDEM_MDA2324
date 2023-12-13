# Abecedario en el orden normal
import csv

palabras = []

with open('palabras.csv') as csvfile:
    words = csv.reader(csvfile, delimiter=',')
    for row in words:
        for word in row:
            palabras.append(word.lower())


totalintentos=0

for palabra in palabras:
    abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","y","z"]
    
    huecos=len(palabra)
    intentos=0
    while huecos>0:
        """     alabradescompuesta=[]
        for letras in palabra:
            palabradescompuesta.append(letras)
        palabradescompuesta.sort()
        palabraordenada="".join(palabradescompuesta) 
        """
       
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

print(f'Usando un alfabeto en su orden normal, el programa necesita {totalintentos} intentos para adivinar las palabras:{palabras}')
  
                

                
                
         
  

 