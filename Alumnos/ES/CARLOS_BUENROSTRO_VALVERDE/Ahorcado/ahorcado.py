import pandas as pd
import time

start = time.time()
print("Iniciamos el juego del ahorcado")
print("+++++++++++++++++++++++++++++++")

# Cargamos las palabras y las almacenamos en una lista
palabras = pd.read_csv('palabras.csv')["PALABRAS"]
lista_palabras = list(palabras)

# Definimos una lista con todas las letras del abecedario ordenadas por probabilidad de aparación
abecedario = ["E", "A", "O", "S", "R", "N", "I", "D", "L", "C", "T", "U", "M", "P", "B", "G", "V", "Y", "Q", "H", "F", "Z", "J", "Ñ", "X", "K", "W"]

# Inicializamos un contador para llevar el cálculo del total de intentos que llevamos en el juego
total_intentos = 1

for palabra in lista_palabras:
    print("+++++++++++++++++++++++++++++++")
    print("Palabra a acertar: ", palabra)
    letras = len(palabra)
    print(palabra, "tiene", len(palabra), "letras")
    # Inicializamos un contador para llevar el cálculo del total de intentos que llevamos en cada palabra
    intento = 0
    while len(palabra) > 0:
        print("Probamos con la letra", abecedario[intento], ".Número intento en esta palabra", intento+1, ".Total intentos en el juego", total_intentos)
        palabra = palabra.replace(abecedario[intento], '')
        intento+=1
        total_intentos+=1

end = time.time()
print("+++++++++++++++++++++++++++++++")
print("Fin del juego del ahorcado. ", "El juego ha durado ", end - start, " segundos")