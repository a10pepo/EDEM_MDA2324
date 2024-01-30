"""Crea un programa en Python que sea capaz de calcular y
 mostrar por consola todos los números primos de 1 - 100"""


for numero in range(1, 101):
    if numero < 2:
        print(f"{numero} no es primo")
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
            print(f"{numero} no es primo")
