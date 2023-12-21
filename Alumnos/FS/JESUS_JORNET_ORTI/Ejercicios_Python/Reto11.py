"""Escribe un programa que pida al usuario los siguientes datos por consola:

Título de la película
Director
Año
País
E introduzca esos valores en una variable GLOBAL llamada "pelicula" """

titulo = str(input("¿Cómo se llama la película?"))
director = str (input("¿Quién la dirigió?"))
anyo = int (input("¿De qué año es?"))
pais = str (input("¿Y de qué país?"))

pelicula = {
            'titulo' : titulo ,
            'director' : director ,
            'año' : anyo ,
            'pais' : pais
               }

print (pelicula)