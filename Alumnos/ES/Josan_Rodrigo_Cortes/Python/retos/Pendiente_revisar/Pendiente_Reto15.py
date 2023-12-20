""" Reto 15
Escribe una función que reciba una muestra de números en una lista y
devuelva otra lista con sus cuadrados. """

def listaCuadrados(lista=[]):
    nuevaLista=[]
    for i in lista:
        elmentoAlCuadrado=lista[i]*lista[i]
        nuevaLista[i]=elmentoAlCuadrado
    return nuevaLista    

lista1=[1,2,3,4,5,6,7,8,9]

print(listaCuadrados(lista1))

elementos=0
listaNumerosPorConsola=[]
while elementos<6:
    nuevoElemento=(input("Introduce un número para tu lista: "))
    nuevoElemento.append(listaNumerosPorConsola)
    elementos+=1

print(listaCuadrados(listaNumerosPorConsola))