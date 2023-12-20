# RETO 4

lista_lenguajes = ['JavaScript', 'TypeScript', 'R', 'Python', 'Dart']
respuestas =[]

for i in lista_lenguajes:
  c = str(input(f'Conoces el lenguaje de programacion {i}? '))
  while c.lower() not in ['si', 'no']:
    c = str(input(f'Esa respuesta no es válida, conoces el lenguaje de programacion {i}? '))
  respuestas.append(f'{i} : {c.lower()}')

print('Los lenugajes de programación que conoce son:')
for c in respuestas:
  print(c)