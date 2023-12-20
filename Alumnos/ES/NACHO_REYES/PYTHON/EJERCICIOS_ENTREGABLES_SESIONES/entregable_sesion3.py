# EJERCICIOS SESION 3

# Ejercicio 3.1

while True:
    print('Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?')
    print('''
    [1] Calcular una inversión
    [X] Salir
    ''')
    eleccion = input('')

    if eleccion == '1':
        while True:
            cant = int(input('¿Cuánto quieres invertir? '))
            porcentaje = (int(input('¿Cuál es el interés anual en porcentaje? '))) / 100
            años = int(input('¿Cuántos años vas a mantener la inversión? '))
            print(f'En {años} años, habrás recibido {cant * porcentaje * años}€ de interés')

            print('¿Qué quieres hacer ahora?')
            print('''
            [1] Calcular una nueva inversión
            [X] Salir
            ''')
            opcion = input('')
            if opcion.lower() == 'x':
                print('¡Nos vemos!')
                break
            elif opcion != '1':
                print("Opción no válida. Por favor, elige '1' para calcular una nueva inversión o 'X' para salir.")
        break
    elif eleccion.lower() == 'x':
        print('¡Nos vemos!')
        break
    else:
        print("Opción no válida. Por favor, elige '1' para calcular una inversión o 'X' para salir.")


# Ejercicio 3.2
  
def es_primo(numero):
    if numero <= 1:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True

for i in range(1, 101):
    if es_primo(i):
        print(f"{i} es primo")


# Ejercicio 3.3

def es_bisiesto(i):
  i = int(i)
  if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
    return True
  else:
    return False

años = ['2010', '2011', '2012', '2013', '2014']

for año in años:
  if es_bisiesto(año):
    print(f"{año} es bisiesto")