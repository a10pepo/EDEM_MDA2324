# import random 

# Random nos permitirá elegir una palabra aleatoria de una lista. Luego, podemos definir una lista de palabras que el programa elegirá al azar.

"""Asignamos variable a través de random choice, que devuelve un valor aleatorio
extraido de la secuencia pasada como argumento."""

# palabra_aleatoria = random.choice(palabras) 

# Asignamos variable para que nos ofresca un guión bajo por cada letra que tenga nuestra palabra aleatoria.

# palabra_oc = "_" *len(palabra_aleatoria)

palabras = ["REMEDIO", "PRONUNCIAR", "MANEJAR", "LEY", "ELEFANTE"]

import string

def listAlphabet():
    return list(string.ascii_uppercase)

alphabet = listAlphabet()

intentos = 0

for palabra in palabras:
    for letter in alphabet:
        if letter in palabra:
            print("letra encontrada")
            intentos = intentos+1
        else:
            print("letra no encontrada")
            intentos = intentos+1

print(intentos)