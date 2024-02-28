""" Reto 8
Escribe una función que reciba un número entero positivo y devuelva su factorial. """

def factorial(numero):
    factnum=1
    for i in range (numero,1,-1):
        
        factnum*=i
    return factnum


print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))