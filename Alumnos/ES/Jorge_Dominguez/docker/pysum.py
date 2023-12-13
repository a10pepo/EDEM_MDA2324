import sys

if len(sys.argv) != 3:
    print("introduce 2 numeros")
    sys.exit(1)

try:
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
except ValueError:
    print('error')

suma_total = n1 + n2

print(f'la suma de {n1} y {n2} es igual a {suma_total}')