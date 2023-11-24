import pandas as pd
import random
import time

df = pd.read_csv('palabras.csv', dtype={"palabras": str})

#lista_letras = ['a', 'e', 'i', 'o', 'u', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
lista_letras = ['e', 'a', 'o', 'i', 's', 'r', 'n', 'l', 'u', 'd', 't', 'c', 'm', 'p', 'b', 'g', 'v', 'y', 'q', 'h', 'f', 'z', 'j', 'x', 'k', 'w']

palabras_disponibles = df['palabras'].tolist()
total_intentos = 0

for i in range(10):
    inicio = time.time()
    intentos = 0
    adivinadas = 0

    palabra_seleccionada = random.choice(palabras_disponibles)
    palabras_disponibles.remove(palabra_seleccionada) 
    numero_letras = len(palabra_seleccionada)
    
    print(f'Palabra a adivinar: {palabra_seleccionada}')

    for letra in lista_letras:
        intentos += 1
        if palabra_seleccionada.count(letra) > 0:
            adivinadas += palabra_seleccionada.count(letra)
        if adivinadas == numero_letras:
            print(f'La palabra adivinada es {palabra_seleccionada}')
            break

    total_intentos += intentos 
    print(f'Total de intentos de la palabra: {intentos}')
    print('---------------------')

fin = time.time()
minutos, segundos = divmod(fin - inicio, 60)
print(f'Tiempo total: {round(segundos, 2)} segundos') #esto lo ha fet mi colegon GPT
print(f'Total de intentos: {total_intentos}')