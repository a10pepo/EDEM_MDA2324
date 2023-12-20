# Crea una función que reciba un rango de números como parámetro y muestre por consola únicamente los valores primos
def primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def mostrar_primos_en_rango(a,b):
    print(f"Números primos en el rango de {a} a {b}:")
    for numero in range(a, b + 1):
        if primo(numero):
            print(numero)

a = 100
b = 340
mostrar_primos_en_rango(a,b)

# Crea una función que pueda evaluar si un número (pasado por parámetro) es primo o no

numero_evaluado = 23

if primo(numero_evaluado):
    print (f"El número {numero_evaluado} es primo.")
else:
    print (f"El número {numero_evaluado} no es primo.")

# Crea una función que reciba un año y pueda indicarte con True o False si es un año bisiesto o no.

def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

año_a_verificar = int(input("Ingrese un año para verificar si es bisiesto: "))
resultado = es_bisiesto(año_a_verificar)
print(f"¿{año_a_verificar} es un año bisiesto? {resultado}")