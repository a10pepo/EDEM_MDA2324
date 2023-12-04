import pandas as pd

palabras = pd.read_csv('palabras.csv')["PALABRAS"]
lista_palabras = list(palabras)
abecedario = ["E", "A", "O", "S", "R", "N", "I", "D", "L", "C", "T", "U", "M", "P", "B", "G", "V", "Y", "Q", "H", "F", "Z", "J", "Ñ", "X", "K", "W"]

for palabra in lista_palabras:
    letras = len(palabra)
    print([palabra , letras])