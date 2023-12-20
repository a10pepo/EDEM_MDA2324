import sys

def suma(no1, no2):
    print('El resultado de sumar', no1, 'y', no2, 'es:', no1 + no2)

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
suma(num1, num2)