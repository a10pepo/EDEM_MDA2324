primos = []
for numero in range(100):
  if numero > 1: 
    for divisor in range(2, numero):
      if (numero % divisor) == 0:  #si se cumple, no es primo (tiene divisor)
        break
    else:
      primos.append(numero)
      
print(primos)