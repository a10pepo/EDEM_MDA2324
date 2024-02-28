""" Reto 5
Escribe un programa que realice lo mismo que el programa del reto 4, pero que elimine de la lista
 aquellos lenguajes que el usuario conoce y únicamente muestre aquellos que no conoce. """

lenguajes=["JavaScript","TypeScript","Python","Dart"]
nuevoslenguajes=[]    
for lenguaje in lenguajes:
    
    pregunta=input(f"¿Conoces el lenguaje de programación {lenguaje}? (si / no)")

    while pregunta!="si" and pregunta!="no":

        pregunta=input(f"¿Conoces el lenguaje de programación {lenguaje}? (si / no)")

    if pregunta=="no":
        nuevoslenguajes.append(lenguaje)
    

print(f'Los lenguajes que te quedan por aprender son: {nuevoslenguajes}')