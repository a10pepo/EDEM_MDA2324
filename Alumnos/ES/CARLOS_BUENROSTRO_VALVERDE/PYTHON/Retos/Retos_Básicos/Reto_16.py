# Reto 16: Crea un script que sea capaz de restar dos fechas y muestra el resultado por consola
from datetime import datetime
nacimiento = datetime(1995, 2, 9, 15, 0, 0)
diferencia = datetime.now() - nacimiento
print(diferencia)