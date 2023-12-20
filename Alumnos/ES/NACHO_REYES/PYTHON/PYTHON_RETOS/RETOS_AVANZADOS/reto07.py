# RETO 7

precios = []

for i in range(0,5):
  p = float(input('Indique el precio que quiere intorducir: '))
  precios.append(p)

def mean():
  return sum(precios) / len(precios)

print(mean())
