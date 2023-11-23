import pandas as pd
import time as t

data = pd.read_csv('txt_horcada.txt', header=None, names=['Palabra'])

list_letras= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']



palabras = data['Palabra'].str.strip('"').tolist()

for palabra in data:
    n_adv = 0
    itt = 0
    palabra_len = len(palabra)
    for letra in list_letras:
        itt += 1
        if(palabra.count(letra) > 0):
            n_adv += palabra.count(letra)
        if(n_adv == palabra_len):
            break
print(itt)
init = t.time()
print(init)