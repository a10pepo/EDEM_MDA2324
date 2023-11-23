import pandas as pd

palabras = pd.read_csv('palabras.csv')["PALABRAS"]
lista_palabras = list(palabras)

for palabra in lista_palabras:
    letras = len(palabra)
    print([palabra , letras])



