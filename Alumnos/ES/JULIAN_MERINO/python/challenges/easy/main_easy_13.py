"""
Reto 13

Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros
y otra función que calcule el área de un círculo recibiendo el radio del mismo.
"""
#We import math library for PI value
import math

base = float(input(f'Enter the triangle base, in mm: '))
height = float(input(f'Enter the triangle height, in mm: '))
radius = float(input(f'Enter the circle radius, in mm: '))

def triangle(base:float, height:float):
    area_t = round(base * height / 2, 2)
    print(f'The area of the triangle is: {area_t:.2f} mm\u00b2')

triangle(base, height)

def circle(radius:float):
    area_c = round(radius**2 * math.pi, 2)
    print(f'The area of the circle is: {area_c:.2f} mm\u00b2')

circle(radius)