#A la aplicación de la calculadora de inversión, deberás añadirle una opción para salir de la consola.

def calculoInversion () :
      
      print(f'Hola, bienvenido al sistema de cálculo de inversiones\n'
      f'¿Cuánto quieres invertir?')
      euros = input('')
      euros = float(euros)

      print('¿Cuál es el interés anual?')
      interes = input('')
      interes = float(interes)

      print('¿Cuántos años vas a mantener la inversion?')
      años = input('')
      años = float(años)

      calculoInteres = euros * (1 + (interes / 100)) ** años - euros

      print(f'En {años} años habrás recibido {calculoInteres} euros de interés. ¿Qué quieres hacer ahora?\n'
            f'[1] Calcular una nueva inversión\n'
            f'[X] Salir')
      
      solicitarCaracter()
      
def salir():
      print(f'¡Nos vemos!')
      exit()
      
def solicitarCaracter ():

      caracter = input('')

      if (caracter == '1'):
            calculoInversion()

      elif (caracter == 'X'):
            salir()           

      else :
            solicitarCaracter()

print(f'Hola, bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?\n'
      f'[1] Calcular una nueva inversión\n'
      f'[X] Salir')

solicitarCaracter()