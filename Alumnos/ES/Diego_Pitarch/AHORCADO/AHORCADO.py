import pandas as pd
import random
import time

df = pd.read_csv('palabras.csv', dtype={"PALABRAS": str})

abecedario = ['E', 'A', 'O', 'S', 'R', 'N', 'I', 'D', 'L', 'C', 'T', 'U', 'M', 'P', 'B', 'G', 'V', 'Y', 'Q', 'H', 'F', 'Z', 'J', 'Ñ', 'X', 'K', 'W']

palabras_disponibles = df['PALABRAS'].tolist()

total_intentos = 0

for palabras in range(len(palabras_disponibles) ): 
    
    palabra_seleccionada = random.choice(palabras_disponibles)
    numero_letras = len(palabra_seleccionada)
    
    palabras_disponibles.remove(palabra_seleccionada) 

    intentos = 0
    
    while numero_letras > 0:
        for letra in abecedario:
            intentos += 1
            if letra in palabra_seleccionada:
                conteo = palabra_seleccionada.count(letra)
                numero_letras -= conteo
                if numero_letras == 0:
                    break
    
    total_intentos += intentos  

    print(f"Palabra: {palabra_seleccionada}, Adivinada en {intentos} intentos.")


print(f"Total de intentos: {total_intentos}") 