# RETO 29

lista_num = []
for i in range(7):
  num = int(input('Introduce un número: '))
  while type(num) != int:
    num = int(input('No has introducido un número, introduce un nuevo número porfavor: '))
  lista_num.append(num)

lista_num2 = sorted(lista_num, reverse = True)
new_list = lista_num2.copy()
new_list.pop(6)
new_list.sort()
print(f'El segundo valor mas pequeño de la lista: {lista_num} es: {new_list[:1]}')