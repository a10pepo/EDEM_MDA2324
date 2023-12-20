# RETO 27

lista_paises = []
for i in range (5):
  pais = str(input('Introduce un país a la lista: '))
  lista_paises.append(pais)
  
lista_paises = set(lista_paises)
lista_paises = sorted(lista_paises)
lista_paises = ', '.join(lista_paises)
print(f'La lista de paises ordenados alfabéticamente, sin ninguna repetición y separados por comas es: {lista_paises}')