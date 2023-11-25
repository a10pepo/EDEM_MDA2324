import pandas as pd
import random
import time

df = pd.read_csv('palabras.csv', dtype={"palabras": str})

lista_letras = ['e', 'a', 'o', 'i', 's', 'r', 'n', 'l', 'u', 'd', 't', 'c', 'm', 'p', 'b', 'g', 'v', 'y', 'q', 'h', 'f', 'z', 'j', 'x', 'k', 'w']

palabras_disponibles = df['palabras'].tolist()
total_intentos = 0

def estrategia_adivinanza(palabra_seleccionada, lista_letras):
    intentos = 0
    letras_adivinadas = set()

    while letras_adivinadas != set(palabra_seleccionada):
        intentos += 1

        for letra in lista_letras:
            if letra in palabra_seleccionada and letra not in letras_adivinadas:
                letras_adivinadas.add(letra)
                break

    return intentos

for i in range(10):
    inicio = time.time()

    palabra_seleccionada = random.choice(palabras_disponibles)
    palabras_disponibles.remove(palabra_seleccionada) 
    
    print(f'Palabra a adivinar: {palabra_seleccionada}')

    intentos = estrategia_adivinanza(palabra_seleccionada, lista_letras)

    print(f'La palabra adivinada es {palabra_seleccionada}')
    print(f'Total de intentos de la palabra: {intentos}')
    print('---------------------')

    total_intentos += intentos 

fin = time.time()
minutos, segundos = divmod(fin - inicio, 60)
print(f'Tiempo total: {round(segundos, 5)} segundos')
print(f'Total de intentos: {total_intentos}')
