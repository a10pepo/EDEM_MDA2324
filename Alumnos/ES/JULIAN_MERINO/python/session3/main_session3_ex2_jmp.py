#Session 3 exercise 2 - EDEM MDA ES Julián Merino Pérez
#Crea un programa en Python que sea capaz de calcular y mostrar por consola todos los números primos de 1 - 100

#We do this with two nested for loops
for i in range(1,100):
  prime = True
  for j in range(1,100):
    if i % j == 0 and i != j and j != 1:
        prime = False
  if prime == True:
    print(f'{i} is prime.')