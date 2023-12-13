import csv
import pandas as pd
import time
palabras_dfr = pd.read_csv("Palabras.csv")

abecedario = ['e', 'a', 'o', 'i', 's', 'n', 'r', 'u', 'l', 'd', 't', 'c', 'm', 'p', 'b', 'g', 'v', 'y', 'q', 'h', 'f', 'j','x', 'z', 'k', 'w']

words_list = palabras_dfr["Palabras"].tolist()

intentos = 0
inicio = time.time()
for letter in words_list:
    letter = letter.lower()
    leng = len(letter)
    for l in abecedario:
        intentos += 1
        if l in letter:
            cont = letter.count(l)
            leng -= cont
            if leng == 0:
                break
fin = time.time()
print(f' El numero de intentos ha sido: {intentos}')
print (f'Hemos tardado... {fin-inicio}')        
