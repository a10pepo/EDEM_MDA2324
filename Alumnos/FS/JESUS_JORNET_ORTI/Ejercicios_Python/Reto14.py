"""Escribe una función que use la función del área del círculo 
para devolver el volumen de un cilindro, obteniendo por parámetro 
la longitud del mismo."""

import math

radio = float (input("¿Cuál es el radio del cilindro en centímetros? "))
altura = float (input("¿Y su altura?"))

volumen = (radio**2) * math.pi * altura

print (f"El volumen del cilindro es de {volumen:.2f}cm^3")