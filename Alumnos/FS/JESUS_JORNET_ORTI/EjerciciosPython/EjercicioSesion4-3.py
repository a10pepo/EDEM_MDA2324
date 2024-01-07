"""
A partir de las respuestas a los dos últimos ejercicios de la Sesión 3:
3. Crea una función que reciba un año y pueda indicarte con True o False si 
es un año bisiesto o no.
"""

def bisiesto(anyo):
    if (anyo % 4 == 0 and anyo % 100 != 0) or anyo % 400 == 0:
        return True
    else:
        return False
    
anyo = int(input('¿Qué año quieres saber si es bisiesto? '))
if bisiesto(anyo):
    print (f'{anyo} es bisiesto.')
else:
    print (f'{anyo} no es bisiesto.')