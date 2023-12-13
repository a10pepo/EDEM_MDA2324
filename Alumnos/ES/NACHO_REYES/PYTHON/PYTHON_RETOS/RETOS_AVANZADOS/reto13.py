# RETO 13

from datetime import datetime

str_d1 = str(input('Indica la primera fecha: '))
str_d2 = str(input('Indica la segunda fecha: '))

d1 = datetime.strptime(str_d1, "%Y/%m/%d")
d2 = datetime.strptime(str_d2, "%Y/%m/%d")

delta = d2 - d1
print(f'La diferencia es de {delta.days} dias')