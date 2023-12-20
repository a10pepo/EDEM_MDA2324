# Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
# Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]

n_in = 1
n_fi = 5
lista = list(range(n_in,n_fi+1))

results = []
for i in lista:
    if i % 2 != 0:
        results = i
        print(results)