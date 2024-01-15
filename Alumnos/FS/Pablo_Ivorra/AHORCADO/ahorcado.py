import pandas as pd
import time
import random

ALPHA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def adivina_palabra(lista_palabras):
    inicio = time.time()
    
    for palabra in lista_palabras:
        letras_adivinadas = []
        
        for letra in ALPHA:
            if letra in palabra:
                letras_adivinadas.append(letra)
        
        print("Letras adivinadas encontradas.")
        
        exito = False
        intentos = 0
        
        while not exito:
            opcion = ''.join(random.choice(letras_adivinadas) for _ in range(len(palabra)))
            intentos += 1
            if opcion == palabra:
                exito = True

        fin = time.time()

        if exito:
            print(f"¡Adiviné la palabra en {fin-inicio:.2f}s y en {intentos} intentos.")
    
def busca_palabra(lista_palabras, letras):
    inicio = time.time()
    intentos = 0
    
    for palabra in lista_palabras:
        conteo_letras = 0
        for letra in letras:
            if letra in palabra:
                conteo_letras += palabra.count(letra)
                if conteo_letras == len(palabra):
                    break
            intentos += 1
        if conteo_letras == len(palabra):
            print(f"Palabra encontrada: {palabra}")
    
    fin = time.time()
    print(f"\nProceso completado en {fin-inicio:.2f}s y {intentos} intentos")

# Llamada a la función adivina_palabra con una lista de palabras
lista_de_palabras = ["hola", "mundo", "python"]
adivina_palabra(lista_de_palabras)

# Llamada a la función busca_palabra con una lista de palabras y letras
lista_de_palabras = ["hola", "mundo", "python"]
letras = ["o", "l", "a"]
busca_palabra(lista_de_palabras, letras)

# Dibujo ASCII del muñeco escapando de la horca
print("   O")
print("  /|\\")
print("  / \\")
print("Gracias por salvarme al ejecutar este código.")




