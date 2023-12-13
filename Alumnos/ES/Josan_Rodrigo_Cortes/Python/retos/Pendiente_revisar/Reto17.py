""" Reto 17
Partiendo de la siguiente tupla:"""

tupla = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)

# Realiza las siguientes operaciones

print('Encontrar los elementos de 3 a 5')
print(tupla[3:5])
print('Encontrar los 6 primeros elementos')
print(tupla[0:6])
print('Muestra la tupla desde el 5 elemento hasta el final')
print(tupla[5:])
print('Muestra toda la tupla haciendo uso de [:]')
print(tupla[::])
print(' Muestra todos los elementos desde la posición 2 a la 9 de dos en dos')
print(tupla[2:9:2])
print('Devuelve la tupla con un salto cada 4 elementos')
print(tupla[::4])
print(tupla[0:len(tupla):4]) #no lo saca bien creo
print(' Usa un step negativo para mostrar la tupla desde la posición 9 a la 2 ')
print(tupla[9:2:-1])
print(tupla)


