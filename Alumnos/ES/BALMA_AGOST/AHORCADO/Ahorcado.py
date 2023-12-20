import csv
import pandas as pd
import random
import time

abecedario = ["E", "A", "O", "S", "R", "N", "I", "D", "L", "C", "T", "U", "M", "P", "B", "G", "V", "Y", "Q", "H", "F", "Z", "J", "Ñ", "X", "K", "W"]

palabras = pd.read_csv("palabras.csv", dtype={"Palabras_ahorcado": str})
palabras_disponibles = palabras["Palabras_ahorcado"].tolist()

print(palabras)

def jugar_ahorcado(palabras_disponibles):
    intentos_totales = 0
    inicio_juego = time.time()

    for _ in range(10):
        intentos = 0
        adivinadas = 0

        palabra_seleccionada = random.choice(palabras_disponibles)
        palabras_disponibles.remove(palabra_seleccionada) 
        numero_letras = len(palabra_seleccionada)

        print(f"Palabra: {palabra_seleccionada}")

        for letra in abecedario:
            intentos += 1
            if palabra_seleccionada.count(letra) > 0:
                adivinadas += palabra_seleccionada.count(letra)
            if adivinadas == numero_letras:
                print(f"La palabra adivinada es {palabra_seleccionada}")
                break

        intentos_totales += intentos 
        print(f"Total de intentos: {intentos}")

    fin_juego = time.time()
    minutos, segundos = divmod(fin_juego - inicio_juego, 60)
    print("-                                  -")
    print(f"Tiempo total: {round(segundos, 2)} segundos")
    print(f"Número total de intentos: {intentos_totales}")

palabras = pd.read_csv("palabras.csv", dtype={"Palabras_ahorcado": str})
palabras_disponibles = palabras["Palabras_ahorcado"].tolist()

jugar_ahorcado(palabras_disponibles)