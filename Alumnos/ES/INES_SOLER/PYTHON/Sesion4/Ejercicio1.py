'''
A partir de las respuestas a los dos últimos ejercicios de la Sesión 3:
a) Crea una función que reciba un rango de números como parámetro y muestre por consola únicamente los valores primos
b) Crea una función que pueda evaluar si un número (pasado por parámetro) es primo o no
c) Crea una función que reciba un año y pueda indicarte con True o False si es un año bisiesto o no.
'''

# Ejercicio 1.a)

lista_nprimos = []

def lista_primos(num_inicial: int, num_final: int):

    for i in range(num_inicial, num_final):
        for num in range(2, i):
            if (i % num) == 0:
                break
        else:
            lista_nprimos.append(i)
    print(f'Los números primos son: {lista_nprimos}')

lista_primos(2,100)


# Ejercicio 1.b)

def num_primo(numero: int):
    for i in range(2, numero):
        if (numero % i) == 0:
            print(f'El número {numero} NO es un número primo.')
            break
    else:
        print(f'El número {numero} SÍ es un número primo.')

num_primo(25)


# Ejercicio 1.c)

def es_bisiesto(anio):
    if anio % 4 == 0:
        print(True)
    else:
        print(False)

es_bisiesto(2008)


