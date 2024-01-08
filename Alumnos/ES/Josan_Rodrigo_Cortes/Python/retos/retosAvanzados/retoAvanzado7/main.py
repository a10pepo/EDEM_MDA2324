""" Reto 7
Escribe un programa que pida 5 precios al usuario y los almacene en una lista de precios.
 Al finalizar, deberá mostrar por consola la media de los precios introducidos. """


listaprecios=[]
for i in range(5):
    precio=int(input("Introduce el precio: "))
    listaprecios.append(precio)

media=sum(listaprecios)/len(listaprecios)
print(media)


