
import pandas as pd
import random 
import time

print('Hola, Mundo')

df = pd.read_csv('Palabras.csv')
lista_palabras = df['PALABRAS:'].tolist()
abecedario =['e', 'a', 'o', 'i', 's', 'n', 'r', 'l', 'u', 'd', 't', 'c', 'm', 'p', 'b', 'g', 'v', 'y', 'q', 'f', 'h', 'z', 'x', 'j', 'k', 'w', 'ñ']


ruta_txt = 'Diccionario_espanol.txt'
lista_diccionario = []
# Abrir el archivo txt, eliminar espacios en blanco y saltos de línea y agregar a la lista_palabras.
with open(ruta_txt,'r', encoding='utf-8') as archivo:
    for linea in archivo:
        lista_diccionario.append(linea.strip())

total_intentos = 0
tinicial = time.time()


for elemento in lista_palabras:
    numero_letras = len(elemento)
    print(f'la palabra {elemento} tiene {numero_letras} letras')
    aciertos = 0
    intentos = 0
    adivinadas = set()

    while aciertos < numero_letras:
        #hacer una lista de palabras del diccionario solo si el número de letras coincide con el del elemento de la lista_palabras
        # ¡Y! contenga las letras ya adivinadas o no contenga las letras que no se han acertado
        filtro_dicc = [palabra for palabra in lista_diccionario if len(palabra) == numero_letras and all(letra in adivinadas or letra not in elemento for letra in palabra) ]
        print(f"aciertos {aciertos} numero {numero_letras}")
        print(filtro_dicc[0])
        if not filtro_dicc:
            print(f'No hay palabras en el diccionario que cumplan las condiciones. Palabra objetivo: "{elemento}", Letras adivinadas: {adivinadas}')

        frecuencia_letras_dicc = {}
        for palabra_en_filtro in filtro_dicc:
            for letra in palabra_en_filtro:

                if letra not in adivinadas:
                    frecuencia_letras_dicc[letra] = frecuencia_letras_dicc.get(letra, 0) + 1

        abecedario_ordenado = sorted(abecedario, key = lambda letra: frecuencia_letras_dicc.get(letra, 0), reverse = True)
        
        letra = abecedario_ordenado[0]
        print(letra+" elegida")
        #letra = abecedario[i]
        veces = elemento.count(letra)
        if veces == 0:
            print("No acierto")
            print(len(adivinadas))
        else:
            adivinadas.add(letra)
        aciertos += veces
        intentos += 1
        #i += 1

        

    print(intentos)
    total_intentos += intentos 
        
print(total_intentos)

tfinal = time.time()
ttranscurrido = tfinal - tinicial
print(f'Han sido necesarios {total_intentos} para adivinar las palabras en {ttranscurrido} segundos')



'''
import pandas as pd
import random 
import time

print('Hola, Mundo')

df = pd.read_csv('Palabras.csv')
lista_palabras = df['PALABRAS:'].tolist()
abecedario = ['e', 'a', 'o', 'i', 's', 'n', 'r', 'l', 'u', 'd', 't', 'c', 'm', 'p', 'b', 'g', 'v', 'y', 'q', 'f', 'h', 'z', 'x', 'j', 'k', 'w', 'ñ']
print(len(abecedario))

total_intentos = 0

tinicial = time.time()

for elemento in lista_palabras:
    numero_letras = len(elemento)
    print(f'la palabra {elemento} tiene {numero_letras} letras')
    aciertos = 0
    intentos = 0
    i = 0
    while aciertos < numero_letras:
        letra = abecedario[i]
        veces = elemento.count(letra)
        aciertos += veces
        intentos += 1
        i += 1
    print(intentos)
    total_intentos = intentos + total_intentos
        
print(total_intentos)

tfinal = time.time()
ttranscurrido = tfinal - tinicial
print(f'El tiempo transcurrido es de {ttranscurrido} segundos')

'''


