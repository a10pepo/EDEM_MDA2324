# Reto 18: Crea una función que sea capaz de eliminar un caracter concreto de una cadena de texto. La función debe tener la siguiente firma:
def eliminar(str, n):
    principio = str[: n]
    final = str [n + 1 :]
    return principio + final

def solucion():
    print(eliminar('Madrid', 0))
    print(eliminar('Madrid', 2))
    print(eliminar('Madrid', 5))