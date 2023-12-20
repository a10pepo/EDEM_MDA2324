'''
Crea un programa en Python que sea capaz de calcular y mostrar por consola todos los números primos de 1 - 100
'''
lista_nprimos = []
num1_100: int = range(1,101)

for i in num1_100:
    for num in range(2, i):
        if (i % num) == 0:
            break
    else:
        lista_nprimos.append(i)

print(f'Los números primos son: {lista_nprimos}')
