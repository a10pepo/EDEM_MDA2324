# Reto 9: Escribe un programa que pueda decirte si un año (número entero) es bisiesto o no

def leap_year():
    year: int = int(input("Intruduzca el año: "))
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(f'El {year} es bisiesto')
    else:
        print(f'El {year} no es bisiesto. Pruebe con otra fecha.')

leap_year()