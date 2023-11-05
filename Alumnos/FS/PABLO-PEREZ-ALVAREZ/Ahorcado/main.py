
import pandas as pd

rows = []
lista_letras = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
lista_vocales = ['a', 'e', 'i', 'o', 'u']

rows = pd.read_csv("palabras.csv")

intentos = 0

for i,palabra in rows.iterrows():
    print(palabra["Nombres"])
    for letra, vocal in zip(lista_letras, lista_vocales):
        if letra in palabra["Nombres"]:
            print(letra)
            intentos+=1
        elif vocal in palabra["Nombres"]:
            print(vocal)
            intentos+=1
        else:
            intentos+=1
print(intentos)


