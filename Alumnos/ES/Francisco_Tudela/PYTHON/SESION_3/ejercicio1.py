
while True:
    print("""Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?
    [1] Calcular una inversión
    [X] Salir""")
    opcion_elegida = input('Indique 1 o X')
    if opcion_elegida == '1':
        print(' Hola. Bienvenido al sistema de cálculo de inversiones.')
        inversion = float(input('Indique la cantidad de € a invertir'))
        interes = float(input('Indique el interes anual aplicado a la inversión'))
        tiempo = int(input('Cuanto tiempo se va a mantener la inversion?'))

        euros_generados = inversion * (1+(interes/100))**tiempo
        print(f'En {tiempo} años habra generado {euros_generados}')
        print('Que desea hacer ahora?')
    elif opcion_elegida.upper() == 'X':
        print('Saliendo del programa')
        exit()
    else:
        print('Indique una opción valida')