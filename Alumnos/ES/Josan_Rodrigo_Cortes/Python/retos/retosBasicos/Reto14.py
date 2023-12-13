""" Escribe una función que use la función del área del círculo para devolver el volumen de un cilindro,
obteniendo por parámetro la longitud del mismo. """


'''Si llamo las funciones desde el reto 13.py en vez de desde funciones.py, me cruza prints.
REVISAR CON ALGUIEN'''

# Área = 2•π•radio•altura [m²]
# areaCirculo=pi*r**2
from funciones import areaCirculo

def areaCilindro(alt,rad):
    a_Cilindro= areaCirculo(rad)*alt
    return a_Cilindro

altura=int(input("Introduce la alrura del cilíndro "))
radio=int(input("Introduce el radio del cilíndro "))

print(f' El área del cilindro es: {areaCilindro(altura,radio)}')



