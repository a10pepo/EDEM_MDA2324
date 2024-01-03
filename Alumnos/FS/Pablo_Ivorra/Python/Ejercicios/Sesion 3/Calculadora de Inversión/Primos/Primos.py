#Crea un programa en Python que sea capaz de calcular y mostrar por consola todos los números primos de 1 - 100
def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
for numero in range(1, 101):
    if es_primo(numero):
        print(numero, "es un número primo")
    else:
        print(numero, "no es un número primo")