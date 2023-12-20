""" Reto 9
Escribe un programa que pueda decirte si un año (número entero) es bisiesto o no """


# print("AÑO BISIESTO??")
# anyo=int(input("Introduce el año a comprobar: "))
def anyoBisiesto(anyo):

    if anyo%4!=0:
        print(f"El año {anyo} no es bisiesto")

    elif anyo%4==0 and anyo%100!=0:
        print(f"El año {anyo} no es bisiesto")

    elif anyo%4==0 and anyo%100!=0 and anyo%400!=0:
        print(f"El año {anyo} no es bisiesto")

    elif anyo%4==0 and anyo%100!=0 and anyo%400==0:
        print(f"El año {anyo} es bisiesto")

anyyo=int(input("Introduce el año"))
for i in range(anyyo-20,anyyo+20):
    anyoBisiesto(i)

