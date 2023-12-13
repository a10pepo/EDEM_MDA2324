"""
Reto 14

Escribe una función que use la función del área del círculo para 
devolver el volumen de un cilindro, obteniendo por parámetro la longitud del mismo.
"""

#We import math library for PI value
import math

radius = float(input(f'Enter the circle radius, in mm: '))
height = float(input(f'Enter the cylinder height, in mm: '))

def circle(radius:float):
    area_c = round(radius**2 * math.pi, 2)
    print(f'The area of the circle is: {area_c:.2f} mm\u00b2')
    return area_c

def cylinder(area_c:float, height):
    area_cyl = round(area_c * height, 2)
    print(f'The volume of the cylinder is: {area_cyl:.2f} mm\u00b3')

cylinder(circle(radius), height)