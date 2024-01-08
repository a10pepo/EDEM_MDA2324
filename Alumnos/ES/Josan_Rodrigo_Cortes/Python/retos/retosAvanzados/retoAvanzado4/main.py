""" Reto 4
Escribe un programa que almacene lenguajes de programación en una lista.

El programa deberá preguntar por consola si el usuario conoce o no el lenguaje. El usuario deberá
 responder "sí" o "no" y cualquier otra respuesta no será tenida en cuenta, preguntando de nuevo la
   misma pregunta:

¿Conoces el lenguaje de programación "lenguaje"? (si / no) donde "lenguaje" es cada uno de los lenguajes 
de la lista.

Finalmente, el programa debe mostrar por pantalla la lista de los lenguajes y si el usuario los conoce
 o no. Algo así:

JavaScript: no
TypeScript: sí
Python: sí
Dart: no """

lenguajes=["JavaScript","TypeScript","Python","Dart"]
dictlenguajes={}


    
for lenguaje in lenguajes:
    
    pregunta=input(f"¿Conoces el lenguaje de programación {lenguaje}? (si / no)")

    while pregunta!="si" and pregunta!="no":

        pregunta=input(f"¿Conoces el lenguaje de programación {lenguaje}? (si / no)")

    if pregunta=="si":
        dictlenguajes[lenguaje]="si"
    
    
    elif pregunta=="no":
        dictlenguajes[lenguaje]="no"

    
            

print(dictlenguajes)

    