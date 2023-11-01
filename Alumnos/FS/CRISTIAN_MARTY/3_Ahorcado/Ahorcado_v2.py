import pandas as pd
import time

path = './test_ahoracado.csv'
data = pd.read_csv(path)

lista = data.values.flatten().tolist()
diccionario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
diccionario_upgrade = ['E', 'A', 'O', 'I', 'S', 'N', 'R', 'L', 'U', 'T', 'C', 'D', 'P', 'M', 'H', 'B', 'G', 'V', 'Y', 'Q', 'F', 'J', 'X', 'Z', 'W', 'K']



def ahorcado():
    inicio_tiempo = int(time.time() * 1000)
    intentos = 0
    for palabra in lista:
        letras_adivinadas = 0
        letras_ya_adivinadas = []  
        letra_anterior = None
        for letra in diccionario_upgrade:
            intentos += 1
            if letra in palabra and letra != letra_anterior and letra not in letras_ya_adivinadas:              
                letras_adivinadas += palabra.count(letra)
                letras_ya_adivinadas.append(letra)  
                letra_anterior = letra
                if letras_adivinadas == len(palabra):
                    break
                
    
    fin_tiempo = int(time.time() * 1000)  
    tiempo_total = fin_tiempo - inicio_tiempo 

    print(f"Intentos totales: {intentos}")
    print(f"Tiempo total de ejecución: {tiempo_total} milisegundos")


ahorcado()
