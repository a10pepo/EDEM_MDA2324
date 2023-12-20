"""
RETO11

Escribe un programa que pida al usuario los siguientes datos por consola:
Título de la película/Director/Año/País
E introduzca esos valores en una variable GLOBAL, llamada "pelicula"
"""

#We initialise variable film as a dictionary
film = dict()
#And start entering key: value entries
def film_details():
    film['title']:str = input("Enter the movie's title: ")
    film['director']:str = input("Enter the movie's director: ")
    film['year']:int = input("Enter the movie's release year: ")
    film['country']:str = input("Enter the movie's country: ")
    print(f'Title: {film["title"]}')
    print(f'Director: {film["director"]}')
    print(f'Year: {film["year"]}')
    print(f'Country: {film["country"]}')

film_details()