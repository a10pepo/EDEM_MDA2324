"""
Reto 15

Escribe una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
"""
def squares(list):
    sq_list = list.copy()
    for i in range(len(list)):
        sq_list[i] = sq_list[i] ** 2
    print(sq_list)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares(list)