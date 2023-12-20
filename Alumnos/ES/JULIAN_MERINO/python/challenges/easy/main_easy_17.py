"""
Reto 17

Partiendo de la siguiente tupla:

tupla = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
Realiza las siguientes operaciones

Encontrar los elementos de 3 a 5
Encontrar los 6 primeros elementos
Muestra la tupla desde el 5 elemento hasta el final
Muestra toda la tupla haciendo uso de [:]
Muestra todos los elementos desde la posición 2 a la 9 de dos en dos
Devuelve la tupla con un salto cada 4 elementos
Usa un step negativo para mostrar la tupla desde la posición 9 a la 2
"""

tuple = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)

#Elements 3 to 5
tuple3_5 = tuple[3:5]
print(f'Elements 3 to 5: {tuple3_5}')

#Elements 3 to 5
tuple_6 = tuple[:6]
print(f'First 6 elements: {tuple_6}')

#Elements 5 until end
tuple5_end = tuple[4:]
print(f'From 5th til end: {tuple5_end}')

#All elements
tuple_all= tuple[:]
print(f'All elements: {tuple_all}')

#Elements 2 to 9, skipping 1
tuple2_9= tuple[2:9:2]
print(f'Elements 2 to 9 skipping 1: {tuple2_9}')

#Elements 2 to 9, skipping 1
tuple_all_each_4 = tuple[::4]
print(f'All elements skipping 4: {tuple_all_each_4}')

#Elements 9 to 2 in reverse
tuple9_2= tuple[9:2:-1]
print(f'Elements 9 to 2 in reverse: {tuple9_2}')