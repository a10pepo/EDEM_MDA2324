# Reto 13: Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.
import math
def area_triangulo():
    partes = dict()
    partes['Base'] = float(input("Introduzca la base (cm) del triángulo: "))
    partes['Altura'] = float(input("Introduzca la altura (cm) del triángulo: "))
    print((partes['Altura']*partes['Base'])/2)

def area_circulo(radio):
    return(math.pi*(radio**2))