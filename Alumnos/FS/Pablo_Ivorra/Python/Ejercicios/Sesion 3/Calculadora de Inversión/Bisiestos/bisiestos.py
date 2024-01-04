#Crea un programa en Python que sea capaz de identificar a partir de una lista de años si un año es bisiesto o no.
#Un año es bisiesto si es divisible entre 4, excepto aquellos divisibles entre 100 pero no entre 400.
#Por ejemplo, 1900 no fue bisiesto, pero sí el 2000.
#El programa debe mostrar por consola el año y si es bisiesto o no.
#Por ejemplo:
#2000 es bisiesto
#1900 no es bisiesto
#1800 no es bisiesto
#1600 es bisiesto


def es_bisiesto(ano):
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        return True
    else:
        return False
    
ano = int(input("Introduce un año: "))

if es_bisiesto(ano):
    print(ano, "es bisiesto")
else:
    print(ano, "no es bisiesto")


