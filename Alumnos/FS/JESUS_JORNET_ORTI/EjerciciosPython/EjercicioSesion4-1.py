"""
A partir de las respuestas a los dos últimos ejercicios de la Sesión 3:
1. Crea una función que reciba un rango de números como parámetro y muestre 
por consola únicamente los valores primos
"""
print ('Vamos a ver qué números son primos')

numero1 = int(input('¿Por qué número quieres empezar? '))
numero2 = int(input('¿Hasta qué número quieres que comprobemos? '))


for numero in range(numero1, numero2):
    if numero < 2:
        False
    elif numero == 2:
        print(f"{numero} es primo")
    else:
        es_primo = True
        for i in range(2, numero):
            if numero % i == 0:
                es_primo = False
                break
        if es_primo:
            print(f"{numero} es primo")
        else:
            False
