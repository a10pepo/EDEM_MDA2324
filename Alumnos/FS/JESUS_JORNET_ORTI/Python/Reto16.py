"""Crea un script que sea capaz de restar dos fechas y 
muestra el resultado por consola"""

import datetime

fecha1 = datetime.datetime (2023, 4, 17)
fecha2 = datetime.datetime (2023, 3, 17)
fecha3 = fecha1 - fecha2

print (fecha3)