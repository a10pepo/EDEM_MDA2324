# Reto 4: Escribe un programa que almacene lenguajes de programación en una lista.
# El programa deberá preguntar por consola si el usuario conoce o no el lenguaje. El usuario deberá responder "sí" o "no" y cualquier otra respuesta no será tenida en cuenta, preguntando de nuevo la misma pregunta:
# ¿Conoces el lenguaje de programación "lenguaje"? (si / no) donde "lenguaje" es cada uno de los lenguajes de la lista.
# Finalmente, el programa debe mostrar por pantalla la lista de los lenguajes y si el usuario los conoce o no. Algo así:

# JavaScript: no
# TypeScript: sí
# Python: sí
# Dart: no

lista_lenguajes = ["JavaScript", "TypeScript", "Python", "Dart"]
respuestas = []
print("Bienvenido al curso de programación. Por favor, indique los lenguajes que conozca.")

for l in lista_lenguajes:
    respuesta = input(f'¿Conoces el lenguaje {l}? ')
    while respuesta not in ['si', "no"]:
        respuesta = input(f'Esa respuesta no es correcta. Introduzca un valor válido. ¿Conoces el lenguaje {l}?')
    respuestas.append(f'{l} : {respuesta}')
    

print("Los leguajes de programación que el alumno conoce son los siguientes:")
for respuesta in respuestas:
    print(respuesta)
