'''
Crea un programa en Python que sea capaz de identificar a partir de una lista de años si un año es bisiesto o no.
'''

lista_anios = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000]
bisiestos = []
no_bisiestos = []

for element in lista_anios:
    if (element%4) == 0:
        bisiestos.append(element)
    else:
        no_bisiestos.append(element)

print(f'De la lista de años, los bisiestos son: {bisiestos}. Los años {no_bisiestos} NO son bisiestos.')