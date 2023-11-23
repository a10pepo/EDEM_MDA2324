import pandas as pd
import time as t
import collections as c
import unicodedata as u


ahorcado_df = pd.read_csv('palabras.csv', header=None, names=['Palabra'])
dic_esp_df = pd.read_csv('dic_esp.csv', header=None, names=['Pal'])
palabras = ahorcado_df['Palabra'].str.strip('"').tolist()
dic = dic_esp_df['Pal'].str.strip('"').tolist()
diccionario = palabras_sin_acentos = [u.normalize('NFKD', palabra).encode('ASCII', 'ignore').decode('ASCII') for palabra in dic]

letras_espanol = ['E', 'A', 'O', 'I', 'N', 'S', 'R', 'L', 'U', 'T', 'C', 'D', 'P', 'M', 'Y', 'V', 'Q', 'G', 'B', 'H', 'F', 'Z', 'J', 'Ñ', 'X', 'K', 'W']

# devuelve una lista con todas las posibles palabras
def listado_palabra(lista:list, letras_bien:list, letras_mal:list) -> list:
    posibles_palabras = []
    aciertos = 0
   
    for i, letra_ok in enumerate(letras_bien):   # todas las palabras que coiciden las letras
        if(letra_ok != '_'):
            for pal_dic in lista:
                if(pal_dic.count(letra_ok) > 0 and pal_dic.index(letra_ok) == i):
                    posibles_palabras.append(pal_dic)
            letras_bien[i] = '_'
            aciertos += 1    
    
    if(aciertos == 0):  # Si no esta la palabra la lsita es la misma que antes, borrando las letras que no están
        posibles_palabras = lista
    
    borrar = []
    for i, letra_no_ok in enumerate(letras_mal):    # borra las palabras que tienen letras que no están en la palabra
        for i, pal_dic in enumerate(posibles_palabras):
            if(pal_dic.count(letra_no_ok) > 0):
                borrar.append(pal_dic)
    for palabra in borrar:
        posibles_palabras.remove(palabra)

    return(posibles_palabras)



def letra_comun(listado:list, excluir:list) -> str:

    letras = "".join(listado)   # junta todas las letras en un array y selecciona la mas comun
    letras_sin_aciertos = ""
    for letra in letras:        # borra las letras que ya aparecen para no repetirlas
        if letra not in excluir:
            letras_sin_aciertos += letra

    cuenta_letras = c.Counter(letras_sin_aciertos)
    letra = cuenta_letras.most_common(1)[0][0]
    return(letra)


def ahorcado4(palabra:str, intentos:int)->int: 
    adivino = 0
    adivinar = len(palabra)
    letras_mal = []
    letras_bien = []
    excluir = []
    posibles_palabras = []
    
    for asterisco in range(0, len(palabra)):    # descubre la longitud de la palabra y prepara para posicion de las letras
        letras_bien.append('_')
    
    for palabra_dic in diccionario:     # filtra las palabras que tienen el mismo tamaño que la que hay que advinar
        if len(palabra_dic) == len(palabra):
            posibles_palabras.append(palabra_dic)

    for j in letras_espanol:    # adivina las palabras
        intentos += 1
        posibles_palabras = listado_palabra(posibles_palabras, letras_bien, letras_mal)
        letra = letra_comun(posibles_palabras, excluir)
        if(palabra.count(letra) > 0):
            adivino += palabra.count(letra)
            excluir.append(letra)
            for i, acierto in enumerate(letras_bien):
                if letra == palabra[i]:
                    letras_bien[i] = letra   
        else:
            letras_mal.append(letra)
        if(adivino == adivinar):
            break

    return(intentos)

intentos = 0
ir = 0
init = t.time()
for palabra in palabras:
    g = ahorcado4(palabra, 0)
    ir += g

fin = t.time()
tiempo = fin-init
print(f'{ir} intentos en {tiempo}t')