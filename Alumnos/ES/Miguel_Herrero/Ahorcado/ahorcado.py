import pandas as pd
import time
import random

# Definimos y guardamos el tiempo inicial antes de hacer cualquier operación
tiempo_inicial = time.time()

# Leemos el archivo CSV con las palabras
palabras_csv = pd.read_csv('palabras.csv', dtype= {'palabras': str,})

# Definimos la lista de todas las letras, la lista de palabras tanto a adivinar como las adivinadas, y el contador de intentos
todas_letras = ['e', 'a', 'o', 'i', 's', 'n', 'r', 'l', 'u', 'd', 't', 'c', 'm', 'p', 'b', 'g', 'v', 'y', 'q', 'h', 'f', 'j', 'ñ', 'x', 'z', 'k', 'w']
lista_palabras = palabras_csv['palabras'].tolist()
palabras_adivinadas = []
intentos = 0

# Función para resolver el ahorcado
for i in range(10):
    letras_acertadas = 0
    palabra_seleccionada = random.choice(lista_palabras)
    lista_palabras.remove(palabra_seleccionada)
    numero_letras = len(palabra_seleccionada)
    for letra in todas_letras:
        intentos += 1
        if palabra_seleccionada.count(letra) > 0:
            letras_acertadas += palabra_seleccionada.count(letra)
        if letras_acertadas == numero_letras:
            palabras_adivinadas.append(palabra_seleccionada)
            break

# Finalizamos el contador del tiempo y calculamos el tiempo transcurrido
tiempo_final = time.time()      
tiempo_transcurrido = tiempo_final - tiempo_inicial

# Imprimimos los resultados del número de intentos y del tiempo transcurrido
palabras_adivinadas_str = ', '.join(palabras_adivinadas)
print(f'Las palabras a adivinar eran: {palabras_adivinadas_str}\n'
    f'Número de intentos: {intentos}\n'
    f'Tiempo transcurrido: {tiempo_transcurrido}')
