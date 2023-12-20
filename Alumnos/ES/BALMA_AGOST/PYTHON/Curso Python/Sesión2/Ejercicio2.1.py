'''Crea una aplicación de consola que calcule los resultados de una inversión. Debe
Pedir por consola una cantidad (numérica) de Inversión
Pedir el % de interés anual
Pedir el número de años que se va a mantener la inversión
Finalmente, calcular la cantidad generada en los años especificados por el usuario
'''
def calcular_inversion():

    inversion = float(input("Hola. Bienvenido al sistema de cálculo de inversiones. ¿Cuánto quieres invertir? "))

    tasa_interes = float(input("¿Cuál es el interés anual?: "))

    años = int(input("¿Cuántos años vas a mantener la inversión?: "))

    cantidad_generada = inversion * (1 + tasa_interes / 100) ** años

    
    print(f"La cantidad generada después de {años} años será: {cantidad_generada: }")

calcular_inversion()

