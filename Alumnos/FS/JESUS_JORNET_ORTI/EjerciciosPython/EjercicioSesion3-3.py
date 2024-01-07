'''Crea un programa en Python que sea capaz de identificar a 
partir de una lista de años si un año es bisiesto o no.'''


for anyo in range(1990,2021):
    if (anyo % 4 == 0 and anyo % 100 != 0) or anyo % 400 == 0:
        print (f"{anyo} es bisiesto")
    else:
        print (f"{anyo} no es bisiesto")