lista = [1, 2, 3, 4, 5]
  
results = []
def cuadrados():
  for i in lista:
    results.append(i ** 2)
  print(f' Los cuadrados calculados de la lista {lista} son: {results}')

cuadrados()