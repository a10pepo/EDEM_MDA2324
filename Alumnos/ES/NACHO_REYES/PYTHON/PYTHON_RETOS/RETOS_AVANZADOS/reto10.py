# RETO 10

a = int(input('Introduce un numero '))
b = int(input('Introduce un numero '))

def maximo_comun_divisor(a, b):
    c = 0
    while b != 0:
        c = b
        b = a % b
        a = c
    return a

def minimo_comun_multiplo(a,b):
  res = (a * b) / maximo_comun_divisor(a,b)
  return res

print(f' El maximo comun divisor de {a} y {b} es: {maximo_comun_divisor(a,b)}')
print(f' El minimo comun multiplo de {a} y {b} es: {minimo_comun_multiplo(a,b)}')