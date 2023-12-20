""" Ejercicio 2
A la aplicación de la calculadora de inversión, deberás añadirle una opción para salir de la consola.
Debería quedar algo parecido a lo siguiente

> Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?
> [1] Calcular una inversión
> [X] Salir
> (Aquí el usuario deberá escribir 1 o X. Ningón otro valor será considerado como válido. Saliendo el mismo mensaje si introduce algo distinto a 1 o X)
En caso de escribir 1 --> Se deberá proceder al sistema de Cálculo de inversión. En todas las pantallas posteriores, se debe mostrar la opción de [X] Salir

> En [N] años habrás recibido [X]€ de interés. ¿Qué quieres hacer ahora?
> [1] Calcular una nueva inversión
> [X] Salir
En caso de escribir X --> La aplicación debe mostrar un mensaje de despedida y cerrarse: """



def retornoInversion():
    cantidad=int(input("¿Cuánto quieres invertir?"))
    interes=int(input("¿Que interes aplicas a la inversion?"))
    años=int(input("¿Durante cuanto años?"))
    retorno=cantidad*(interes/100)*años
    print(f"En {años} años, con un interes del {interes}%, recibiras {retorno} €")

opcion=" "

while opcion!= "X":
    print("> Hola. Bienvenido al sistema de cálculo de inversiones")
    opcion=input("""
¿Qué quieres hacer?
> [1] Calcular una inversión
> [X] Salir
""")

    if opcion=="1":
        retornoInversion()
        opcion=input("""¿Qué quieres hacer ahora?
> [1] Calcular otra inversión
> [X] Salir
""")
    else:
        opcion=input("""
Lo siento, parametro introducido fuera del rango de elección.                     
¿Qué quieres hacer?
> [1] Calcular una inversión
> [X] Salir
""")
        
print("Programa finalizado. ¡Nos vemos!")