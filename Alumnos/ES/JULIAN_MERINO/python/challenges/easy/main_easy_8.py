"""
Reto 8

#Escribe un programa que pueda decirte si un número (número entero) es primo o no
"""

#This is pretty different from what I've done in Session 4 exercises (this looks more
#efficient).

#I've found a piece a function on Wikipedia that checks
#whether an integer is prime. Accepts an integer and returns a boolean.
#I need to import the module isqrt from the library math:
from math import isqrt

def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit+1, 6):
      if n % i == 0 or n % (i+2) == 0:
        return False
    return True
#Use int() to cast the input to an integer. Otherwise, the funcion fails.
a = int(input('Input an integer to check its primality: '))
if is_prime(a) == True:
  print(f'{a} is a prime number.')
else:
  print(f'{a} is not a prime number.')