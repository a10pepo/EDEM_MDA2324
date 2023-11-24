# Como no puedo sumar sustantivos, voy a ver las veces que aparece repetida una palabra en el texto

import requests
import json
import time
#import matplotlib.pyplot as plt
#import numpy as np
# no entiendo porque no me deja importar matplotlib ni nunpy

url = "https://api.chucknorris.io/jokes/random"

numeroFrases=0

while numeroFrases<=3:

    time.sleep(1)
    respuesta = requests.get(url)
    datos=respuesta.json()
    fraseChuck:str =datos["value"]  
    numeroFrases+=1
    f = open("ChuckCasa.txt", "a")
    f.write( str(numeroFrases) +" " + fraseChuck + "\n")
    f.close()
    
f = open("ChuckCasa.txt")

listapalabras=[]

for line in f:

    listafrases=line.split() #Separa las frases y Me devuelve una lista donde cada elemento es una frase

    for palabra in listafrases:

        listapalabras.append(palabra) #itera las frases y me devuelve una lista donde cada elemento es una palabra.

#quito los respetidos transformando la lista en un set

listapalabrasnorepetidas=set(listapalabras)
#creo un diccionario vacío
diccionariopalabras={}

for i in listapalabrasnorepetidas:
    diccionariopalabras[i]=0 #creo un diccionario de palabras de la lista no repetidas con valor 0 cada una.
    # Y las añado al diccionario 
# ahora hay que contar las veces que una palabra aparece dentro de la lista de palabras


for i in listapalabras: # En este bucle cuento las veces que aparece una palabra en las frases,
    for j in listapalabrasnorepetidas: #sumando uno cada vez que aparece una palabra

        if i ==j:
            diccionariopalabras[j]+=1
      

print(diccionariopalabras)

#Tambien se podría hacer de mayor a menor
#probado-->parece que FUNCIONA!!
#tambien pordría contar la longitud de casa palabra
#Revisar este artículo:https://es.stackoverflow.com/questions/410757/diccionarios-anidados-a-partir-de-listas-en-python

#PODRIA CREAR UN BUCLE QUE AÑADIERA UN ELEMENTO A UNA LISTA SI TIENE LEN 1,2,3,ETC... Y 
#CREAR UNA LISTA POR LA LONGITUD DE LA STRING, CON UN BUCLE. 
#debugg los bucles para ver si funcionan los códigos
