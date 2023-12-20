def calcular_inversion():
    inversion = float(input("Hola. Bienvenido al sistema de cálculo de inversiones. ¿Cuánto quieres invertir? "))
    tasa_interes = float(input("¿Cuál es el interés anual?: "))
    años = int(input("¿Cuántos años vas a mantener la inversión?: "))
    cantidad_generada = inversion * (1 + tasa_interes / 100) ** años
    print(f"La cantidad generada después de {años} años será: {cantidad_generada: }")

opcion = ''

while opcion.upper() != 'X':
        opcion = input(
        
        ''' Hola, escoge una opción:
            1. Calcular inversión
            X. Salir '''
        )
        
        if opcion.upper() == '1':
                calcular_inversion()
        elif opcion.upper() == 'X':
                print("¡Nos vemos!")
                exit()
        else:
                print("Opción no válida. Por favor, elige 1 para calcular una inversión o X para salir.")
