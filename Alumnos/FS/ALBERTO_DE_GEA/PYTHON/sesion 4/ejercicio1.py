#EJERCICIO 1.1
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

#EJERCICIO 1.2
numero = 10
if primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")


#EJERCICIO 1.3
def bisiesto(num):
  if num % 4 == 0:
   if num % 100 != 0:
    return True
  return False

anio = 2024
if bisiesto(anio):
    print(f"{anio} es bisiesto.")
else:
    print(f"{anio} no es bisiesto.")