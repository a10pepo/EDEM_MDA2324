# RETO 16

miLista = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
new_list = []

for i in miLista:
  if i != ():
    new_list.append(i)

miLista = new_list
print(miLista)

miLista = [i for i in miLista if i != ()]
print(miLista)
