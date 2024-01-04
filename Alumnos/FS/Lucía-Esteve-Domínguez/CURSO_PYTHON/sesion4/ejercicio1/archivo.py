'''A partir de las respuestas a los dos últimos ejercicios de la Sesión 3:
Crea una función que reciba un rango de números como parámetro y muestre por consola únicamente los valores primos
Crea una función que pueda evaluar si un número (pasado por parámetro) es primo o no
Crea una función que reciba un año y pueda indicarte con True o False si es un año bisiesto o no '''

def mostrar_primos(rango_inicio, rango_fin):
    for numero in range (rango_inicio, rango_fin +1):
        if numero > 1 and all(numero % i != 0 for i in range(2, int(numero ** 0.5)+1)):
            print (numero, end='')



def año_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else: 
        return False
    
lista_años = [1900, 1991, 1992, 1992, 1994, 1995, 1996, 1997, 1998, 1999, 2000,2001,2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]

for año in lista_años:
    if año_bisiesto: 
        print (f"{año} es un año bisisesto")
    else:
        print (f"{año} es un año bisisesto")
