import pandas as pd
import time as t

init = t.time()
ahorcado_df = pd.read_csv('palabras.csv', header=None, names=['Palabra'])

palabras = ahorcado_df['Palabra'].str.strip('"').tolist()

intentos = 0
tiempo = 0.0

vocales = ['A', 'E', 'I', 'O', 'U']
cons_comun = ['S', 'R', 'N', 'D', 'L', 'C', 'T', 'M', 'P', 'B', 'G']
cons_no_comun = ['V', 'Y', 'Q', 'H', 'F', 'Z', 'J', 'Ñ', 'X', 'K', 'W']

letras1 = ['E', 'A', 'O', 'I', 'N', 'S', 'R', 'L']
letras2 = ['U', 'T', 'C', 'D', 'P', 'M', 'Y', 'V']
letras3 = ['Q', 'G', 'B', 'H', 'F', 'Z', 'J']
letras4 = ['Ñ', 'X', 'K', 'W']

letras_espanol = ['E', 'A', 'O', 'I', 'N', 'S', 'R', 'L', 'U', 'T', 'C', 'D', 'P', 'M', 'Y', 'V', 'Q', 'G', 'B', 'H', 'F', 'Z', 'J', 'Ñ', 'X', 'K', 'W']


## OPTIMIZAR
# importar diccionario español.
# cuando tengas alrededor del 50% de la palabra buscar palabras en el diccionario que tengan la coincidencia al 100%.
# IMPORTANTE. Excluir las palbras cuyas letras han sido descartadas.
# lo haré en ahorcado4

def ahorcado(palabra:str,intentos:int)->int: 
   # acierto = False
    voc = False
    cons1 = False
    adivino = 0
    adivinar = len(palabra)
    while(adivino != adivinar):
        if(voc == False):
            for vocal in vocales:
                intentos += 1
                adivino += palabra.count(vocal)
                if(adivino == adivinar):
                    break
                if(vocal == 'U'):
                    voc = True
        elif(cons1 == False):
            for conso in cons_comun:
                intentos += 1
                adivino += palabra.count(conso)
                if(adivino == adivinar):
                    break
                if(conso == 'G'):
                    voc = True
        else:
            for conso in cons_no_comun:
                intentos += 1
                adivino += palabra.count(conso)
                if(adivino == adivinar):
                    break
    return(intentos)


def ahorcado2(palabra:str,intentos:int)->int: 
   # acierto = False
    let1 = False
    let2 = False
    let3 = False
    adivino = 0
    adivinar = len(palabra)
    while(adivino != adivinar):
        if(let1 == False):
            for vocal in letras1:
                intentos += 1
                adivino += palabra.count(vocal)
                if(adivino == adivinar):
                    break
                if(vocal == 'L'):
                    let1 = True
        elif(let2 == False):
            for conso in letras2:
                intentos += 1
                adivino += palabra.count(conso)
                if(adivino == adivinar):
                    break
                if(conso == 'V'):
                    let2 = True
        elif(let3 == False):
            for conso in letras3:
                intentos += 1
                adivino += palabra.count(conso)
                if(adivino == adivinar):
                    break
                if(conso == 'J'):
                    let3 = True
        else:
            for conso in letras4:
                intentos += 1
                adivino += palabra.count(conso)
                if(adivino == adivinar):
                    break
    return(intentos)


def ahorcado3(palabra:str,intentos:int)->int: 
    adivino = 0
    adivinar = len(palabra)
    while(adivino != adivinar):
        for letra in letras_espanol:
            intentos += 1
            adivino += palabra.count(letra)
            if(adivino == adivinar):
                break
    return(intentos)


def ahorcado4(palabra:str,intentos:int)->int: 
    adivino = 0
    adivinar = len(palabra)
    letras_mal = []
    for letra in letras_espanol:
        intentos += 1
        if(palabra.count(letra) > 0):
            adivino += palabra.count(letra)
        else:
            letras_mal.append(letra)
        if(adivino == adivinar):
            break
    return(intentos)

'''
p = 'PRONUNCIAR'
intentos = 0
print(f'- {ahorcado(p, intentos)}')

init = t.time()
print(ahorcado(p, intentos))
fin = t.time()
tiempo = fin-init
print(f'{tiempo}')

intentos = 0
init = t.time()
print(ahorcado2(p, intentos))
fin = t.time()
tiempo = fin-init
print(f'{tiempo}')         
            
intentos = 0
init = t.time()
print(ahorcado3(p, intentos))
fin = t.time()
tiempo = fin-init
print(f'{tiempo}')     

intentos = 0
init = t.time()
print(ahorcado4(p, intentos))
fin = t.time()
tiempo = fin-init
print(f'{tiempo}')  
'''
intentos = 0
ir = 0
init = t.time()
for palabra in palabras:
    g = ahorcado4(palabra, 0)
    ir += g

fin = t.time()
tiempo = fin-init
print(f'{ir} intentos en {tiempo}t')




