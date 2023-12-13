""" Ejercicio 3
Crea un programa en Python que sea capaz de calcular y mostrar por consola todos los números 
primos de 1 - 100
 """
# En este ejercicio he tenido que copiar la función por que no sabía de que forma expresarla.


def primos(numero):
    if numero == 0 or numero == 1 or numero == 4:
        return False
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True
            

numerosPrimos = []

for n in range(1, 100):
    esPrimo = primos(n)
    if esPrimo:
        numerosPrimos.append(n)

print(numerosPrimos)
