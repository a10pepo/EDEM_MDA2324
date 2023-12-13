# RETO 12

alturas = []
for i in range (0,8):
  alt = float(input('Introduce la altura: '))
  alturas.append(alt)

alturas = sorted(alturas, reverse = True)
alturas = alturas[:3]

print(f'Las 3 alturas mas altas son: {alturas}')