

choice = ''
# La variable count perimitirá modificar el mensaje de entrada del programa 
# en función de si ya ha sido utilizada la calculadora o no.
count = 0
# Bienvenida al sistema e interfaz.
print('Bienvenido al sistema de cálculo de inversiones.')
# Con método lower() para aceptar también la x mayúscula.
while (choice != 'x'):

    if (count == 0):
        print('¿Qué desea hacer?')
    else:
        print('¿Qué desea hacer ahora?')

    choice = input('''
          [1] Calcular una inversión.
          [X] Salir del programa.
''').lower()
    
    if (choice == '1'):
        # Un input para establecer cantidad a invertir.
        initial_capital = float(input('¿Cuánto desea invertir? '))

        # Otro input para el interés anual y periodo.
        interest_rate = float(input('¿A qué interés anual (%) está invirtiendo? '))
        period = float(input('¿Y por cuántos años va a mantener esta inversión? '))

        # Hacer el cálculo con interés compuesto:
        final_capital = initial_capital * (1 + interest_rate/100) ** period
        net_return = round(final_capital - initial_capital,2)
        # Devolver resultado por terminal:
        print(f'En {period} años habrás recibido {net_return}€ de interés.')

    elif (choice == 'x'):
        print('¡Nos vemos pronto!')
        break

    else:
        print('Opción no válida, escoja de nuevo:')

    count += 1

