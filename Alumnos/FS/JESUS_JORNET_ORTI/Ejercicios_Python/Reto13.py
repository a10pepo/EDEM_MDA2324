"""Escribe una función que calcule el área de un triángulo, 
recibiendo la altura y la base como parámetros y otra función 
que calcule el área de un círculo recibiendo el radio del mismo."""

base = float(input("¿Cuál es la base del triángulo en centímetros? "))
altura = float (input("¿Y su altura? "))

area = (base*altura)/2

print (f"el area es de {area} cm^2")