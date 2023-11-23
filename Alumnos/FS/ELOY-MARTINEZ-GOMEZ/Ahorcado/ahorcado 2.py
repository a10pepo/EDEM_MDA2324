import pandas as pd
import time
import random

ALPHA = "abcdefghijklmnñopqrstuvwxyz"

def ahorcado_palabra(word_list):
    start = time.time()
    
    for word in word_list:
        success_letters = []
        for letter in ALPHA:
            if letter in word:
                success_letters.append(letter)
        print("Success Letters done.")

        success = False
        counter = 0
        while success == False:
            option = ''.join(random.choice(success_letters) for i in range(len(word)))
            counter += 1
            if option == word:
                success = True

        end = time.time()

        if success == True:
            print(f"Reto conseguido en {end-start}s en {counter} intentos.")
    
def ahorcado(word_list, alpha):
    start = time.time()
    counter= 0
    for word in word_list:
        letter_counting = 0
        for letter in alpha:
            if letter in word:
                letter_counting += word.count(letter)
                if letter_counting == len(word):
                    break
            counter += 1
        if letter_counting == len(word):
            print(f"Palabra encontrada.")
    end = time.time()
    print(f"\nProceso terminado en {round(end-start, 2)}s y {counter} intentos")
    return counter

df_palabras = pd.read_csv("palabras.txt")
lista_palabras = df_palabras["PALABRAS"].to_list()

ahorcado(lista_palabras, "tjoeyrfdlmaincwuxpqbzkvsgñh")