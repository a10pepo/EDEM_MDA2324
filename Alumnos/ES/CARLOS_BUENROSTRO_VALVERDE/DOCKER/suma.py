import sys

print('Bienvenido al programa de suma. por favor, introduzca dos argumentos (números enteros) para poder realizar la suma de los mismos.')

numero1 = int(sys.argv[1])
numero2 = int(sys.argv[2])

suma = numero1 + numero2

print(f'La suma de {numero1} + {numero2} es: {suma}')