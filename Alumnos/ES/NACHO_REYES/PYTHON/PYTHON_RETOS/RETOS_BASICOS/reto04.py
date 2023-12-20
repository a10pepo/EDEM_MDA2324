#Escribe un programa que sea capaz de mostrar los elementos de una lista en orden inverso al original.
ini = 1
fin = 20
lista = list(range(ini, fin+1))

list_rev = lista
list_rev.reverse()
print(list_rev)