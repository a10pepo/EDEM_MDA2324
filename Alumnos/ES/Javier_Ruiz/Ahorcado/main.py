import pandas as pd
import time
import unidecode
from collections import Counter

# Lee el CSV

df = pd.read_csv('palabras.csv')

# Extrae la columna "Palabras" como una lista y las pongo en minuscula porque sino da problemas

palabras_lista = df['PALABRAS'].tolist()
palabras_lista = [palabra.lower() for palabra in palabras_lista] 

# Diccionario de palabras sacado de https://github.com/JorgeDuenasLerin/diccionario-espanol-txt

palabrastodas = "0_palabras_todas_no_conjugaciones.txt"
rae_palabras = []

# Limpiando el diccionario para poder usarlo

with open(palabrastodas, 'r', encoding='utf-8') as archivo:
    for linea in archivo:
        # Eliminar los caracteres de nueva línea al final de cada línea
        palabra = linea.strip()
        # Quito tildes y diacríticos usando unidecode
        palabra_sin_tildes = unidecode.unidecode(palabra)
        # Convertir a minúsculas
        palabra_minuscula = palabra_sin_tildes.lower()
        # Eliminar caracteres no deseados (por ejemplo, '-')
        palabra_limpia = ''.join(caracter for caracter in palabra_minuscula if caracter.isalnum() or caracter.isspace())
        # Agregar las palabras limpias a la lista
        rae_palabras.append(palabra_limpia)

# AHORCADO

total_intentos = 0
iniciocrono = time.time()

while palabras_lista:
    palabra_seleccionada = palabras_lista[0]
    palabras_lista.remove(palabra_seleccionada)

    print(f'Palabra: {palabra_seleccionada}')

    numero_letras = len(palabra_seleccionada)

    rae_palabras_f1 = [palabra for palabra in rae_palabras if len(palabra) == numero_letras]   # filtro 1: palabras que contengan el mismo numero de letras
    f1 = ''.join(rae_palabras_f1)
    frecuencia_letras1 = Counter(f1)
    letras_ordenadas = sorted(frecuencia_letras1.items(), key=lambda x: x[1], reverse=True)

    # Creo la primera lista de letras a elegir en base a el orden de uso en filtro 1
    primer_set = [letra for letra, frecuencia in letras_ordenadas]

    #print(primer_set)
    
    intentos_realizados = 0
    nletras_correctas = 0
    letras_correctas_lista = []
    letras_incorrectas_lista = []
    indice = 0  

    while indice < len(primer_set):        # Bucle while para controlar el índice (disclaimer: esto lo he tenido que hacer porque iterar la lista primer_set directamente, ha sido imposible)

        letra = primer_set[indice]                          # Siempre elige la primera letra
        intentos_realizados += 1

        if palabra_seleccionada.count(letra) > 0:
            nletras_correctas += palabra_seleccionada.count(letra)
            letras_correctas_lista.append(letra)
            rae_palabras_f1 = [palabra for palabra in rae_palabras_f1 if all(letra in palabra for letra in letras_correctas_lista)]        # filtro 2.1: en base a las palabras que contienen la letra adivinada
            #print(f'Letras correctas {letras_correctas_lista}')

        if palabra_seleccionada.count(letra) == 0:
            letras_incorrectas_lista.append(letra)
            rae_palabras_f1 = [palabra for palabra in rae_palabras_f1 if letra not in palabra]                                              # filtro 2.2: en base a las palabras que no contienen la letra fallada
            #print(f'Letras incorrectas : {letras_incorrectas_lista}')

        # Actualiza primer_set de letras eligibles
        primer_set = [letra for letra, frecuencia in sorted(Counter(''.join(rae_palabras_f1)).items(), key=lambda x: x[1], reverse=True)]      #Ordena la lista de letras en base a la frecuencia de uso a partir de los filtros 2
        primer_set = [letra for letra in primer_set if letra not in letras_correctas_lista]                                                    # Elimina de posibles letras las que ya ha adivinado previamente
        #print(primer_set)


        if nletras_correctas == numero_letras:
            break


    print(f'Numero de intentos : {intentos_realizados}')
    total_intentos += intentos_realizados

fincrono = time.time()
tiempo_transcurrido = fincrono - iniciocrono


print(f'Total de intentos: {total_intentos}')
print(f'Tiempo transcurrido: {round(tiempo_transcurrido, 2)} segundos')
