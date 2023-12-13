import pandas as pd

#leer archivo csv
df =pd.read_csv('palabras.csv')

#Crear lista[] 
lista=[]
for element in df['palabras']:
    lista.append(element)
print(lista)

#adivinar palabra

letras_abc =('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
intentos = 0

for i in lista:
    letras=len(i)
    while letras > 0:
        for a in letras_abc:
            intentos+=1
            if a in i:
                conteo = i.count(a)
                letras-=conteo
                if letras == 0:
                    break
                

print(f'el numero de intentos  fue {intentos}')
