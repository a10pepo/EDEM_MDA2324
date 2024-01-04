'''Crea un programa en Python que sea capaz de identificar a partir de una lista de años si un año es bisiesto o no'''
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