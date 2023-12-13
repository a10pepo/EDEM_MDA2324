#Session 4 exercise 1 - EDEM MDA ES Julián Merino Pérez
#A partir de las respuestas a los dos últimos ejercicios de la Sesión 3:

#1. Crea una función que reciba un rango de números como parámetro y muestre por consola únicamente los valores primos
#We define isprime functio
def isprime(n):
  for i in n:
    prime = True
    for j in n:
      if i % j == 0 and i != j and j != 1:
          prime = False
    if prime == True:
      print(f'{i} is prime.')

#And pass a list to the function
list = range(1, 100)
isprime(list)

#2. Crea una función que pueda evaluar si un número (pasado por parámetro) es primo o no

#We modify isprime function with output when it's not a prime number

def isprime_or_not(n):
  for i in n:
    prime = True
    for j in n:
      if i % j == 0 and i != j and j != 1:
          prime = False
    if prime == True:
      print(f'{i} is prime.')
    else:
      print(f'{i} is not prime.')

# And pass the list to the function
isprime_or_not(list)

#3. Crea una función que reciba un año y pueda indicarte con True o False si es un año bisiesto o no.

def lapyear(year):
  if year % 4 == 0:
    return True
  else:
    return False

#We iterate a range of years from a list.
years = range(1990, 2031)
for i in years:
  print(f'{i} is {lapyear(i)}')