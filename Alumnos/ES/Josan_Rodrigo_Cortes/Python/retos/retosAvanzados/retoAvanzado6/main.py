""" Reto 6
Escribe un programa que pida al usuario una palabra por consola y devuelva si se trata de un palíndormo**

** Palíndromo: Palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a
 izquierda """

palabra=input("Introduce la palabra")
listapalabra=[]
for letra in palabra:
    listapalabra.append(letra)

listapalabraInvertida=listapalabra[::-1]


if listapalabra==listapalabraInvertida:
    print(f'La palabra {palabra} es un palindromo')
else:
    print(f'La palabra {palabra} es no un palindromo')    