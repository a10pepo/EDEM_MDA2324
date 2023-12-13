'''
A la aplicación de la calculadora de inversión, deberás añadirle una opción para salir de la consola.

Debería quedar algo parecido a lo siguiente:

> Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?
> [1] Calcular una inversión
> [X] Salir
> (Aquí el usuario deberá escribir 1 o X. Ningún otro valor será considerado como válido. 
Saliendo el mismo mensaje si introduce algo distinto a 1 o X)
En caso de escribir 1 --> Se deberá proceder al sistema de Cálculo de inversión. 
En todas las pantallas posteriores, se debe mostrar la opción de [X] Salir

> En [N] años habrás recibido [X]€ de interés. ¿Qué quieres hacer ahora?
> [1] Calcular una nueva inversión
> [X] Salir
En caso de escribir X --> La aplicación debe mostrar un mensaje de despedida y cerrarse:

> ¡Nos vemos!
> (aplicación cerrada con un exit())
'''


# VERSIÓN 'LÓGICA':
print('Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quiere hacer?')

opcion_escogida = ''

while opcion_escogida != 'X':
    opcion_escogida = input('''
    1. Calcular una nueva inversión.
    X. Salir
    ''')
    
    if opcion_escogida == '1':
        inversion_inicial = input('¿Cuánto quiere invertir? ')
        interes_anual = input('¿Cuál es el interés anual? (%) ')
        anos_inversion = input('¿Cuántos años va a mantener la inversión? ')
        resultado_inversion: float = float(inversion_inicial) * (float(interes_anual)/100) *int(anos_inversion)
        print(f'En {anos_inversion} años habrá recibido {resultado_inversion:.2f}€ de interés. ¿Qué quiere hacer?')
        opcion_escogida

    if opcion_escogida == 'X':
        print('¡Nos vemos!')
        exit()

    else:
        opcion_escogida




# VERSIÓN CON SALIDA EN TODAS LAS PANTALLAS:

def salir():
        print('¡Nos vemos!')
        exit()


print('Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quiere hacer?')

opcion_escogida = ''
opcion_escogida1 = ''
opcion_escogida2 = ''
opcion_escogida3 = ''
opcion_escogida4 = ''

while opcion_escogida != 'X':
    opcion_escogida = input('''
    1. Calcular una nueva inversión.
    X. Salir
    ''')

    if opcion_escogida == '1':
        print('Su elección ha sido guardada. ¿Qué quiere hacer?')
        opcion_escogida1 = input('''
        1. Seleccionar cantidad a invertir.
        X. Salir
        ''')

        if opcion_escogida1 == '1':
            inversion_inicial = input('¿Cuánto quiere invertir? ')
            print('Su elección ha sido guardada. ¿Qué quiere hacer?')
            opcion_escogida2 = input('''
            1. Seleccionar interés anual. 
            X. Salir
            ''')

            if opcion_escogida2 == '1':
                interes_anual = input('¿Cuál es el interés anual? (%) ')
                print('Su elección ha sido guardada. ¿Qué quiere hacer?')
                opcion_escogida3 = input('''
                1. Seleccionar la duración de la inversión.
                X. Salir
                ''')

                if opcion_escogida3 == '1': 
                    anios_inversion = input('¿Cuántos años va a mantener la inversión? ')
                    print('Su elección ha sido guardada. ¿Qué quiere hacer?')
                    opcion_escogida4 = input('''
                    1. Calcular el interés recibido al final de la inversión.
                    X. Salir
                    ''')

                    if opcion_escogida4 == '1':
                        resultado_inversion: float = float(inversion_inicial) * (float(interes_anual)/100) *int(anios_inversion)
                        print(f'En {anios_inversion} años habrá recibido {resultado_inversion:.2f}€ de interés. ¿Qué quiere hacer ahora?')
                        opcion_escogida 
                    else:
                        salir()
                
                else:
                    salir()
            
            else:
                salir()   

        else:
            salir() 
    
    elif opcion_escogida == 'X':
        salir()
    else:
        opcion_escogida

 










