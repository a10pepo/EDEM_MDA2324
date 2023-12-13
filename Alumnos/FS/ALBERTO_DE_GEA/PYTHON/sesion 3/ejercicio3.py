#EJERCICIO NUMERO 2 - año bisiesto

listaAnyoBisiesto = []
listaAnyoNormal = []

def bisiesto(num):
  if num % 4 == 0:
   if num % 100 != 0:
    return True
  return False

for numero in range (2000,2110):
  if bisiesto(numero) is True:
    listaAnyoBisiesto.append(numero)
    
print('Bisiesto:')
for bisiesto in listaAnyoBisiesto:
  print(f'-{bisiesto}')
