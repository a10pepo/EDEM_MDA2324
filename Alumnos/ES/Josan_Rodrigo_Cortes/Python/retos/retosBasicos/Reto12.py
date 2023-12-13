""" Escribe un programa que almacene en una lista (Array) todos los nombres de los
alumnos del curso Programación para 
No Programadores y los muestre en por pantalla. """

alumnos=[]

while (len(alumnos)<10):
    
    nombre=input("Introduce el nombre")
    alumnos.append(nombre)

print(alumnos)
