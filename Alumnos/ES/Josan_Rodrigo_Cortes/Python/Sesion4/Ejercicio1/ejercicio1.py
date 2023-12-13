""" Ejercicio 1
A partir de las respuestas a los dos últimos ejercicios de la Sesión 3:"""
# 1.Crea una función que reciba un rango de números como parámetro y muestre por consola 
# únicamente los valores primos

def esPrimo(numero):
    if numero == 0 or numero == 1 or numero == 4:
        return False
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True
            
def mostrar_primos_en_rango(inicio, fin):
    numeros_primos = []
    for n in range(inicio, fin + 1):
        if esPrimo(n):
            numeros_primos.append(n)
    print(numeros_primos)

numerosPrimos = []
mostrar_primos_en_rango(100,150)


# 2.Crea una función que pueda evaluar si un número (pasado por parámetro) es primo o no
esPrimo(3)

# Crea una función que reciba un año y pueda indicarte con True o False si es un año bisiesto o no.

def anyoBisiesto(anyo):

    if anyo%4!=0:
        print(f"El año {anyo} no es bisiesto")

    elif anyo%100==0 and anyo%400!=0:
        print(f"El año {anyo} no es bisiesto")

    else:
        print(f"El año {anyo} es bisiesto")

        
    
queanyo=int(input("Introduce el año: "))
anyoBisiesto(queanyo)