""" Sesión 2
Ejercicio
Crea una aplicación de consola que calcule los resultados de una inversión. Debe
Pedir por consola una cantidad (numérica) de Inversión
Pedir el % de interés anual
Pedir el número de años que se va a mantener la inversión
Finalmente, calcular la cantidad generada en los años especificados por el usuario
Debería resultar en algo así vía consola:

Paso 1
> Hola. Bienvenido al sistema de cálculo de inversiones.
> ¿Cuánto quieres invertir?
> (EL usuario escribe aquí la cantidad)
Paso 2
> ¿Cuál es el interés anual?
> (EL usuario escribe aquí el interés anual)
Paso 3
> ¿Cuántos años vas a mantener la inversión?
> (EL usuario escribe aquí el nº de años)
Paso 4 - Final
> En [N] años habrás recibido [X]€ de interés
> (Donde [N] debes sustituirlo por el número de años y [X] por la cantidad generada)
 """

print("> Hola. Bienvenido al sistema de cálculo de inversiones")

def retornoInversion():
    cantidad=int(input("¿Cuánto quieres invertir?"))
    interes=int(input("¿Que interes aplicas a la inversion?"))
    años=int(input("¿Durante cuanto años?"))
    retorno=cantidad*(interes/100)*años
    print(f"En {años} años, con un interes del {interes}, recibiras {retorno} €")

retornoInversion()
