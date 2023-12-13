""" Reto 16
Crea un script que sea capaz de restar dos fechas y muestra el resultado por consola """

from datetime import datetime, timedelta

# fechaInicio=input("Introduce la fecha inicial como yymmdd: ")
# fechaFinal=input("Introduce la fecha final como yymmdd: ")

# f1=timedelta.strptime(fechaInicio,'%d-%m-%Y ')
# f2=timedelta.strptime(fechaFinal,'%d-%m-%Y ')

# diferencia=f2-f1
# print(diferencia)
# dias = (f1 - f2) / timedelta(days=1)
# meses = (f1 - f2) / timedelta(months=1)
# años = (f1 - f2) / timedelta(years=1)
# print(f'La diferencia es de {dias} días, {meses} meses o {años} años. ') 


# Luego, solicita al usuario que ingrese las 3 partes de una fecha por separado, así que llame input() tres veces, convierta los resultados en enteros y cree una fecha:

""" año = (input('Introduzca un año'))
mes = (input('Introduzca un mes'))
dia = (input('Introduzca un día'))
fecha = datetime.date(dia,mes,año)
print(fecha)
 """
# Si no, solicita al usuario que ingrese la fecha en un formato específico , luego convierta ese formato en los tres números de año, mes y día:

datos = input('Introduzca una fecha de forma YYYY-MM-DD')
año, mes, dia = map(int, datos.split('-'))
fecha = datetime.date(año, mes, dia)