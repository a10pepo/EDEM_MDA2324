""" def sumar(a,b):
    total= a+b
    print(f'El resultado de la suma es {total}')

sumar(5,3)

 """
# suma.py
import sys

a= int(sys.argv[1])
b= int(sys.argv[2])


resultado=a+b
print(f'La suma de los dos numeros es igual a {resultado}')