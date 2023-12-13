# Los años bisiestos son aquellos cuyas dos últimas cifras 
# son divisibles por 4 (2012/ 4= 503), exceptuando los múltiplos de 100,
# donde a su vez también se exceptúan aquellos divisibles por 400 (1600, 2000, 2400...) 
# que sí serán bisiestos



def es_bisiesto(rango):
    bisiestos = []
    for year in rango:

        if (year % 100 == 0):
            if (year % 400 == 0):
                bisiestos.append(year)

        elif (year % 4 == 0):
            bisiestos.append(year)

    return bisiestos


first = int(input('Bienvenido, introduce a partir de qué año quieres calcular si son bisiestos:  '))
second = int(input('y hasta qué año? '))

choice = range(first,second)

bisiestos_rango = es_bisiesto(choice)


print(f'Los años bisiestos comprendidos en esos años son: {bisiestos_rango}')