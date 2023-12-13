import random


abecedario2 = ["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
abecedario = ['e', 'a', 'o', 's', 'r', 'n', 'l', 'd', 'i', 'c', 't', 'u', 'm', 'p', 'b', 'g', 'v', 'y', 'q', 'h', 'f', 'z', 'j', 'ñ' 'x', 'k', 'w']



with open("palabras.csv", "r") as archivo:
    lista = archivo.read().splitlines()

intento= 0


for palabra in lista:
    longitud = len(palabra)
    while longitud > 0:
        for a in abecedario:
            intento += 1
            if a in palabra:
                conteo = palabra.count(a)
                longitud -= conteo
                if longitud == 0:
                    break

 
print(f'ha tomado {intento} intentos resolver el ahorcado')







