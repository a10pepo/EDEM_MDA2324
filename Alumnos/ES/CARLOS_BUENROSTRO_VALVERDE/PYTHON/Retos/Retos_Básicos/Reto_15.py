# Reto 15: Escribe una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
def cuadrados(lista):
    for numero in lista:
        print(numero**2)
lista = [1, 2, 3, 4, 5, 6]

cuadrados(lista)