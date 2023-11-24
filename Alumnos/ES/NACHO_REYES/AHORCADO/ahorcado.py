import pandas as pd
import time
inicio = time.time()
#df = pd.read_csv('palabras.csv')

#lista = []
#for i in df['palabras']:
#    lista.append(i)
#print(lista)

lista = ['japonesa','aullar','cosquillas','amistad','matrimonio','obligatorio','trenza','aldea','peinado','principal']

letras_espanol = ['e', 'a', 'o', 's', 'r', 'n', 'l', 'd', 'i', 'c', 't', 'u', 'm', 'p', 'b', 'g', 'v', 'y', 'q', 'h', 'f', 'z', 'j', 'ñ' 'x', 'k', 'w']

intentos = 0

for i in lista:
    num = len(i)
    while num > 0:
        for a in letras_espanol:
            intentos += 1
            if a in i:
                conteo = i.count(a)
                num -= conteo
                if num == 0:
                    break

fin = time.time()
print(f' El numero de intentos ha sido de: {intentos}')
print(f' El tiempo de ejecución ha sido de: {fin-inicio}') 