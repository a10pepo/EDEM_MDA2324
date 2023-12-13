import pandas as pd

print('Hola mundo')

df = pd.read_csv('palabras.csv')
lista_palabras=df['PALABRAS'].tolist()
print(f'la lista de palabras es: {lista_palabras}')

abecedario= ['e','a','o','i','s','n','r','l','u','d','t','c','m','p','b','g','v','y','q','h','f','z','j','x','k','w','ñ']

intentos_totales=0

for palabra in lista_palabras:
    cantidad_letras=len(palabra)
    aciertos=0
    intentos=0
    i=0
    while aciertos<cantidad_letras:
        letra = abecedario[i]
        veces=palabra.count(letra)
        aciertos= aciertos + veces
        intentos +=1
        i+=1
    intentos_totales=intentos_totales+intentos
    print(f'La palabra {palabra} ha supuesto {intentos} intentos')
print(f'El número de intentos totales es: {intentos_totales}')

