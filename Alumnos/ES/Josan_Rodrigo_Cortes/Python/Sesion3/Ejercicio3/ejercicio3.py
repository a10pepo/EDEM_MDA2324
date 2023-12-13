""" Ejercicio 3
Crea un programa en Python que sea capaz de identificar a partir de una lista de años si 
un año es bisiesto o no. """
# Al igual que para el numero primo, he copiado la función, no encontraba por mi mismo como expresar la 
# lógica del problema.

def anyoBisiesto(anyo):

    if anyo%4!=0:
        print(f"El año {anyo} no es bisiesto")

    elif anyo%100==0 and anyo%400!=0:
        print(f"El año {anyo} no es bisiesto")

    else:
        print(f"El año {anyo} es bisiesto")

        
    
queanyo=int(input("Introduce el año: "))
for i in range(queanyo-10,queanyo+10):
    anyoBisiesto(i)

