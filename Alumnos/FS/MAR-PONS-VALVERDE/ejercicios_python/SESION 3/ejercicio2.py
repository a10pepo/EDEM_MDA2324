# Crea un programa en Python que sea capaz de calcular y mostrar por consola todos los números primos de 1 - 100

# Función para verificar si un número es primo
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

# Iterar a través de los números del 1 al 100
print("Números primos en el rango de 1 a 100:")
for num in range(1, 101):
    if es_primo(num):
        print(num, end=" ")
