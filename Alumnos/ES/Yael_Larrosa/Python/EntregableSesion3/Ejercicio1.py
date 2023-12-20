#A la aplicación de la calculadora de inversión, deberás añadirle una opción para salir de la consola.

opcion_escogida = ' '

print('Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?\n')


while(opcion_escogida != 'X'):
  print('[1] Calcular una inversión\n[X] Salir')
  opcion_escogida = input('(Aquí el usuario deberá escribir 1 o X) ')
  
  if (opcion_escogida == '1'):
    print(f'Hola. Buenvenido al sistema de cálculo de inversiones.\n ¿Cuánto quieres invertir?')    
    cantidad_inversion= float(input(f'(El usuario escribe aquí la cantidad)'))    
    print('¿Cuál es el interés anual?')
    interes_anual = float(input(f'((El usuario escribe aquí el interés anual)'))    
    print('¿Cuántos años va a mantener la inversión?')
    tiempo_inversion = int(input(f'(El usuario escribe aquí el nº de años)'))    
    cantidad_recibida =round(cantidad_inversion*(interes_anual/100)*tiempo_inversion,2)  
    print(f'En {tiempo_inversion} años habrás recibido {cantidad_recibida} € de interés.¿Qué quieres hacer ahora?')

  elif(opcion_escogida == 'X'): #repasar
    print('¡Nos vemos!')
    exit("aplicación cerrada con un exit()")

  else: 
    print('Has introducido mal el codigo, introduce un 1 o X')
