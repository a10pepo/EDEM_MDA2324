def es_bisiesto():
  año = int(input('Introduce un año: '))
  if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f'El año seleccionado: {año} fue bisiesto o lo será...')
  else:
    print(f'El año seleccionado: {año} no fue bisiesto o no lo será...')

es_bisiesto()