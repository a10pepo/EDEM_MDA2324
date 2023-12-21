"""Escribe una función que reciba una muestra de números 
en una lista y devuelva otra lista con sus cuadrados."""

lista = [9,3,4,6,7]
lista_cuad = []

for numero in lista:
    cuadrado = (numero ** 2)
    lista_cuad.append(cuadrado)

print (lista_cuad)