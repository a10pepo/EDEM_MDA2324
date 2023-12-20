# RETO 6

palabra = str(input('Indique la palabra que quiere comprobar: '))
girada = palabra[::-1]

if palabra == girada:
  print(f'La palabra {palabra} es un palíndormo porque: {palabra} = {girada}')
else:
  print(f'La palabra {palabra} no es un palíndormo porque: {palabra} != {girada}')