# 1 Script para jugar al Ahorcado
# 2 Contar Intentos
# 3 Contar Tiempo

# PRIMERA ITERACION MAS PRACITCO

# 1 GIT 
# 2 DOCKER

# # REQ 
# 1 NO ESPACIOS
# 2 LETRAS
# 3 ESPACIOS
# 4 NO ACENTOS
# 5 MAYUSCULAS
# 6 INTENTAR TIEMPO 25 SEG

import pandas as pd
import time

abecedario = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'u', 'c', 'm', 'f', 'w', 'y', 'g', 'p', 'b', 'v', 'k', 'x', 'j', 'q', 'z', 'ñ']

palabras = pd.read_csv("palabras.txt")
inicio = time.time()

def ahorcado(palabras):
    intento = 0
    for i,palabra in palabras.iterrows():
        cuentaletras = 0
        for letra in abecedario:
            if letra in palabra["PALABRAS"]:
                cuentaletras += palabra["PALABRAS"].count(letra)
                if cuentaletras == len(palabra["PALABRAS"]):
                    break                
            intento += 1
        if cuentaletras == len(palabra["PALABRAS"]):
            print(intento)

end = time.time()

print(round(end-inicio,10))
ahorcado(palabras)