"""Escribe un programa que pueda decirte si un año 
(número entero) es bisiesto o no"""

anyo = int(input ("Qué año quieres saber si es bisiesto o no? "))

if (anyo % 4 == 0 and anyo % 100 != 0) or anyo % 400 == 0:
    print ("Es bisiesto")
else:
    print ("No es bisiesto")
    