# RETO 15

numeros = [10,20,(1,3),30,50,69,(10,20),40]
cantidad = 0

for i in numeros:
  x = isinstance(i, tuple)
  if x == True:
    cantidad += 1
print(f' La variable cantidad tiene ahora el valor de: {cantidad}')