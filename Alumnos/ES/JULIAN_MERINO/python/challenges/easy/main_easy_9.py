"""
Reto 9
Escribe un programa que pueda decirte si un año (número entero) es bisiesto o no
"""

#If a year is divisible by 4, it's a leap year
year = int(input('Enter a year (integer): '))
if year % 4 == 0:
    print(f'{year} is a leap year.')
else:
  print(f'{year} is not a leap year.')