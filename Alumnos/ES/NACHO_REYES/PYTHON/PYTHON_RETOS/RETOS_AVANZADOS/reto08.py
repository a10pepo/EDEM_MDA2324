# RETO 8

fact = []
num = int(input('Introduzca el numero entero positivo sobre el cual se quiere hacer su factorial: '))
while num < 0:
  num = int(input('El número intorducido no es correcto, introduzca el numero entero positivo sobre el cual se quiere hacer su factorial: '))
for i in range(1,(num + 1)):
  fact.append(i)

def calc_fact():
  res = 1
  for i in fact:
    res = res * i
  return res

print(fact)
print(calc_fact())