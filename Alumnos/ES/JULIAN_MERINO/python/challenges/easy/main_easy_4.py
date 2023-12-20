"""
RETO 4

Escribe un programa que sea capaz de mostrar los elementos de una lista en orden 
inverso al original.
Por ejemplo: teniendo [1,2,3,4,5] el programa debe mostrar por pantalla [5,4,3,2,1]
"""

# Let's create a list using a range
mylist = []

for i in range(39):
  mylist.append(i + 1)

print(mylist)
#and then use the .reverse() method
reversed = mylist.copy()
reversed.reverse()
print(reversed)