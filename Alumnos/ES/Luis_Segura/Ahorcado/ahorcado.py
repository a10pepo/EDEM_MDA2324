#Bon dia Pedro, el total de este código son 143 pero le pregunté al amigo cómo podría reducir los intentos y me dio una variable lambda,
#que aún no hemos visto pero que creo que primero analiza todas las letras del csv y guarda las más usadas para ir probándolas las primeras
#en vez de seguir el orden de la variable abecedario y creo que no se podían guardar.
#Sea como fuere, ojalá esté bien. Abajo te dejo el anterior que hice que me lo hace en 155 intentos pero ese seguro que está bien.
import pandas as pd
import random
import time

df = pd.read_csv('palabras.csv', dtype={"PALABRAS": str})

abecedario = ["E", "A", "O", "S", "R", "N", "I", "D", "L", "C", "T", "U", "M", "P", "B", "G", "V", "Y", "Q", "H", "F", "Z", "J", "Ñ", "X", "K", "W"]

frecuencia_letras = {letra: 0 for letra in abecedario}
for palabra in df['PALABRAS']:
    for letra in abecedario:
        frecuencia_letras[letra] += palabra.count(letra)

# Aquí creo que utiliza la variable lambda para ordenar las letras conforme al uso que el piensa que tienen
letras_ordenadas = sorted(abecedario, key=lambda letra: frecuencia_letras[letra], reverse=True)

palabras_disponibles = df['PALABRAS'].tolist()
total_intentos = 0

for i in range(10):
    inicio = time.time()
    intentos = 0
    adivinadas = 0

    palabra_seleccionada = random.choice(palabras_disponibles)
    palabras_disponibles.remove(palabra_seleccionada) 
    numero_letras = len(palabra_seleccionada)

    print(f'Palabra a adivinar: {palabra_seleccionada}')

    for letra in letras_ordenadas:
        intentos += 1
        if palabra_seleccionada.count(letra) > 0:
            adivinadas += palabra_seleccionada.count(letra)
        if adivinadas == numero_letras:
            print(f'Se ha adivinado: {palabra_seleccionada}')
            break

    total_intentos += intentos 
    print(f'Intentos totales: {intentos}')

fin = time.time()
minutos, segundos = divmod(fin - inicio, 60)
print('--------------------------')
print(f'Tiempo total: {round(segundos, 2)} segundos')
print(f'Intentos totales: {total_intentos}')

#PALABRAS INDEPENDIENTES, NO SE ACUMULA EL VALOR DE LA LETRA
#Número de intentos
#Tiempo

# A esto de abajo ni caso porque mira si iba perdido ayer que pensaba que tendría que ir generando las formas y tal como en un ahorcado jajajaja
#___________

#     |
#     |
#     |
#     |
#     |
#_____|_____

#      __________
#     |
#     |
#     |
#     |
#     |
#_____|_____


#AQUÍ EL QUE DA 155!!!!
#import pandas as pd
#import random
#import time

#df = pd.read_csv('palabras.csv', dtype={"PALABRAS": str})

#abecedario = ["E", "A", "O", "S", "R", "N", "I", "D", "L", "C", "T", "U", "M", "P", "B", "G", "V", "Y", "Q", "H", "F", "Z", "J", "Ñ", "X", "K", "W"]

#palabras_disponibles = df['PALABRAS'].tolist()
#total_intentos = 0

#for i in range(10):
#    inicio = time.time()
#    intentos = 0
#    adivinadas = 0

#    palabra_seleccionada = random.choice(palabras_disponibles)
#    palabras_disponibles.remove(palabra_seleccionada) 
#    numero_letras = len(palabra_seleccionada)

#    print(f'Palabra: {palabra_seleccionada}')

#    for letra in abecedario:
#        intentos += 1
#        if palabra_seleccionada.count(letra) > 0:
#            adivinadas += palabra_seleccionada.count(letra)
#        if adivinadas == numero_letras:
#            print(f'La palabra adivinada es {palabra_seleccionada}')
#            break

#    total_intentos += intentos 
#    print(f'Total de intentos: {intentos}')

#fin = time.time()
#minutos, segundos = divmod(fin - inicio, 60)
#print('--------------------------')
#print(f'Tiempo total: {round(segundos, 2)} segundos')
#print(f'Total de intentos: {total_intentos}')