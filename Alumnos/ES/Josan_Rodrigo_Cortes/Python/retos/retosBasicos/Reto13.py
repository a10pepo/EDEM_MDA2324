""" Escribe una función que calcule el área de un triángulo, recibiendo la altura 
y la base como parámetros y otra función que calcule el área de un círculo
recibiendo el radio del mismo. """

import math


def areaTriangulo(b,a):
    areat=(b*a)/2
    return areat
    
def areaCirculo(r):
    pi=math.pi
    areaCirculo=pi*r**2
    return areaCirculo

radio=int(input("Introduce el radio del círculo para calcular su área"))

print(f' El area del círculo es: {areaCirculo(radio)}')

base=int(input("Introduce la base del triangulo para cálcular su área"))
altura=int(input("Introduce la altura del triangulo para cálcular su área"))

print(f'El área del triangulo es: {areaTriangulo(base,altura)}')