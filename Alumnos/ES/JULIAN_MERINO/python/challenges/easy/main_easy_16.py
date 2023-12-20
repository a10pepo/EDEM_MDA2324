"""
Reto 16

Crea un script que sea capaz de restar dos fechas y muestra el resultado por consola
"""

#For this, we need the function date from datetime library:
from datetime import date
#date works with yyyy/mm/dd (note: remove leading zeroes from month and day)

#Let's do a function for this
def subt_dates():
    date1 = date(2023, 12, 8)
    date2 = date(2023, 12, 7)
    return date1 - date2

print(subt_dates())