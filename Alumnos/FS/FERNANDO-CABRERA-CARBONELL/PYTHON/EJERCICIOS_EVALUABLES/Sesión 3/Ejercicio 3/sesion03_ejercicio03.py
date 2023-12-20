def es_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

# Lista de años a verificar
lista_años = [2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]

# Verificar si los años en la lista son bisiestos
for año in lista_años:
    if es_bisiesto(año):
        print(f"{año} es un año bisiesto.")
    else:
        print(f"{año} no es un año bisiesto.")
