""" 
Reto 11
Escribe un programa que pida al usuario los siguientes datos por consola:

Título de la película
Director
Año
País
E introduzca esos valores en una variable GLOBAL llamada "pelicula" """

titulo=input("Introduce el titulo ")
director=input("Introduce el director ")
anyo=input("Introduce el año ")
pais=input("Introduce el país ")

pelicula={}
pelicula["Titulo"]=titulo
pelicula["Director"]=director
pelicula["Año"]=anyo
pelicula["Pais"]=pais

print(pelicula)

