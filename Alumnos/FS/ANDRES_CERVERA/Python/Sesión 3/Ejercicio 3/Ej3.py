#Crea un programa en Python que sea capaz de identificar a partir de una lista de años si un año es bisiesto o no

listaAnyos = [1990, 1991, 1992, 1993,1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002]
listaBisiestos = []

for x in listaAnyos:
    if x % 4 == 0:
        listaBisiestos.append(x)

print(f"{listaBisiestos}")