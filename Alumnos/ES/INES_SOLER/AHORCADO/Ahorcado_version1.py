
import pandas as pd
import time

print('Hola, Mundo')

df = pd.read_csv('Palabras.csv')
lista_palabras = df['PALABRAS:'].tolist()
abecedario= ['e','a','o','i','s','n','r','l','u','d','t','c','m','p','b','g','v','y','q','h','f','z','j','x','k','w','ñ']


total_intentos = 0
tinicial = time.time()

for elemento in lista_palabras:
    numero_letras = len(elemento)
    print(f'la palabra {elemento} tiene {numero_letras} letras')
    aciertos: int = 0
    intentos: int = 0
    i: int = 0
    while aciertos<numero_letras:
        letra = abecedario[i]
        veces=elemento.count(letra) 
        aciertos= aciertos + veces
        intentos +=1
        i+=1
    print(f'Número de intentos: {intentos}')
    total_intentos = total_intentos + intentos

print(f'Número total de intentos: {total_intentos}')

tfinal = time.time()
ttranscurrido = tfinal - tinicial
print(f'El tiempo transcurrido es de {ttranscurrido} segundos')

