def primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5)+1):
        if numero % i == 0:
            return False
    return True

print("Números primos en el rango de 1 a 100: ")
for numero in range(1, 101):
    if primo(numero):
        print(numero)