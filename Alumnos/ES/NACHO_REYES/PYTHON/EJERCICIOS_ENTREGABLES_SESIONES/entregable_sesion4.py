# EJERCICIOS SESION 4

# Ejercicio 4.1

def es_bisiesto(i):
  i = int(i)
  if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
    return True
  else:
    return False

años = []
for i in range (10):
  a = input('Introduce un año ')
  años.append(a)

for año in años:
  if es_bisiesto(año):
    print(f"{año} es bisiesto")


# Ejercicio 4.2

def es_primo():
  numero = int(input('Indica el numero que quieres comprobar '))
  if numero <= 1:
      print(f'El numero {numero} no es primo')
      return

  for i in range(2, int(numero ** 0.5) + 1):
      if numero % i == 0:
          print(f'El numero {numero} no es primo')
          break
  else: 
      print(f'El numero {numero} es primo')

es_primo()


# Ejercicio 4.3

import requests

url = 'https://randomuser.me/api'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

print(data)