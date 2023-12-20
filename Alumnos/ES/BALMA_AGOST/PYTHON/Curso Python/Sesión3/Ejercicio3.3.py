lista_años = [1765,1798,1823,1976,1997,2000,2002,2012,2018,2021,2023]

# a) divisible entre 4 b) divisible entre 100 c) divisible entre 400 ----> Bisiesto si (a y no (b) o c)
    
def es_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

for año in lista_años:
    if es_bisiesto(año):
        print(f"{año} es un año bisiesto.")
    else:   
        print(f"{año} no es un año bisiesto.")