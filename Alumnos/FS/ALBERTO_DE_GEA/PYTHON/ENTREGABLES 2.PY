#EJERCICIO NUMERO 1 - NÚMEROS PRIMOS

listaNumeroPrimo = []
listaNumeroCompuesto = []

def primo(num):
 if num < 2: 
   return False
 for i in range(2, num): 
   if num % i == 0: 
    return False
 return True 

for numero in range (1,101):
  if primo(numero) is True:
    listaNumeroPrimo.append(numero)
    
print('Primos:')
for primos in listaNumeroPrimo:
  print(f'-{primos}')

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



