# Reto 11: Escribe un programa que pida al usuario los siguientes datos por consola:
def crear_peli():
    pelicula = dict()
    pelicula['Título'] = input("Introduzca el nombre de la película: ")
    pelicula['Director'] = input("Introduzca el nombre del director: ")
    pelicula['Año'] = int(input("Introduzca el año de la película: "))
    pelicula['País'] = input("Introduzca el país de la película: ")

crear_peli()
print('pelicula')