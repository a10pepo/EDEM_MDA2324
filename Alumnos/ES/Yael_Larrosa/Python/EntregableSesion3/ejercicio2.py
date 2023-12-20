#Crea un programa en Python que sea capaz de calcular y mostrar por consola todos los números primos de 1 - 100

i=1
numeros_primos = []

while (i<101):

  lista = list(range(1,i+1)) 
  lista_divisibles = []
  
  #mediante este for esta evaluando para cada numero entre que numeros es divisible
  for elemento in lista: 
    resto = i%elemento
    if (resto == 0):
      lista_divisibles.append(elemento)

  lista_primo=[1,i] #un numero primo es aquel que solo e divisible por el mismo y por la unidad
  
  #en este if se comprueba si los numeros por los que es divisible coincide con la peculiaridad  de los numeros primos
  if (lista_divisibles==lista_primo):
    numeros_primos.append(i) 

  i+=1

print(f'Los numeros primos de 1-100 son: {numeros_primos}')