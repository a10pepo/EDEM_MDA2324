import pandas as pd

df = pd.read_csv('Palabras.csv')
lista_palabras = df['Palabras:'].str.lower().tolist()

abecedario = ['e', 'a', 'o', 'i', 's', 'n', 'r', 'l', 'u', 'd', 't', 'c', 'm', 'p', 'b', 'g', 'v', 'y', 'q', 'f', 'h', 'z', 'x', 'j', 'k', 'w', 'ñ']

total_intentos = 0

for palabra in lista_palabras:
    numero_letrasdepalabra = len(palabra)
    print(f'La palabra {palabra} tiene {numero_letrasdepalabra} letras')

    numero_intentos = 0
    letras_encontradaporpalabra = 0

    for letra in abecedario:
        letras_enpalabra = palabra.count(letra)
        letras_encontradaporpalabra += letras_enpalabra
        numero_intentos += 1
        
        if letras_encontradaporpalabra == numero_letrasdepalabra:
            break

    total_intentos += numero_intentos
    print(f" Has encontrado todas las letras en {numero_intentos} intentos para esta palabra.")

print(f"Total de intentos para todas las palabras: {total_intentos}")



