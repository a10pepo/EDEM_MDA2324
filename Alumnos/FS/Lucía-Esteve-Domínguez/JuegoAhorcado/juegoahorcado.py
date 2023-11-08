import pandas as pd

nombre="Hola Mundo"
print(nombre)
#JUEGO AHORCADO
letras="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
intentos=0
palabras=pd.read_csv("juegoahorcado.txt")
print(palabras)
for i,palabra in palabras.iterrows():
    for letra in letras:
        if letra in palabra["Palabras"]:
            print(True)
            intentos=intentos+1
        else:
            print(False)
            intentos=intentos+1
print(intentos)
