import pandas as pd
import time
import timeit
import sys

tiempo_inicial = time.time()

palabras_csv = pd.read_csv('palabras.csv',
                             dtype= {
                                 'Palabra': str,
                             })

listaLetras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
intentos = 0

def Ahorcado():
    for i, palabras in palabras_csv.iterrows():
        palabraEnLista = list(palabras['Palabra'])
        for letra in listaLetras:
            global intentos
            if len(palabraEnLista) == 0:
                break
            else:
                intentos += 1
                if(letra in palabraEnLista):
                    #palabraEnLista.remove(letra)
                    while letra in palabraEnLista:
                        palabraEnLista.remove(letra)
                        print(palabraEnLista)                   
              
Ahorcado()

tiempo_final = time.time()      
tiempo_ejecucion = tiempo_final - tiempo_inicial

print(f'Número de intentos: {intentos}\n'
      f'Tiempo transcurrido: {tiempo_ejecucion}')