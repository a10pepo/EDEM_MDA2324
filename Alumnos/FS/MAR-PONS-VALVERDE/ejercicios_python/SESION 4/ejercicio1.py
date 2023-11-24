# A partir de las respuestas a los dos últimos ejercicios de la Sesión 3:
# Crea una función que reciba un rango de números como parámetro y muestre por consola únicamente los valores primos
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def mostrar_primos_en_rango(inicio, fin):
    for num in range(inicio, fin + 1):
        if es_primo(num):
            print(num)

# Ejemplo de uso:
inicio = 1
fin = 100
mostrar_primos_en_rango(inicio, fin)


# Crea una función que pueda evaluar si un número (pasado por parámetro) es primo o no

def es_primo(numero):
    if numero  <=1:
        return False
    for i in range (2,numero):
        if numero % i== 0:
            return False
    return True

numero=20
if es_primo(numero):
    print(f'{numero} es un número primo.')    
else:
    print(f'{numero} no es un número primo.')    


# Crea una función que reciba un año y pueda indicarte con True o False si es un año bisiesto o no.
def es_bisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else: 
        return False

año=2004
if es_bisiesto(año):
    print(f'{año} es bisiesto.')
else: 
    print(f'{año} no es bisiesto.')
