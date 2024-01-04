# EJERCICIOS SESIÓN 

# Ejercicio 1

opcion_escogida = ''
while True:
    opcion_escogida = input('''Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?
1. Calcular una inversión
X. Salir
''')
    if (opcion_escogida == '1'):
        while True:
            cantidad = int(input('''¿Cuanto quieres invertir?
'''))
            interes = int(input('''¿Cuál es el interés anual (en %)?
'''))
            años = int(input('''¿Cuántos años vas a mantener la inversión?
'''))
            resultado = años * cantidad * (interes/100)
            print(f'''En {años} años habrás recibido {resultado}€ de interés. ¿Qué quieres hacer ahora?
    1. Calcular una nueva inversión
    X. Salir''')
            opcion_escogida2 = input()
            if (opcion_escogida2 == 'X'):
                print('¡Nos vemos!')
                break
            elif(opcion_escogida2 != '1'):
                print('Opción no valida.')   
        break 
    elif (opcion_escogida == 'X'):
        print('¡Nos vemos!')
    break

# Ejercicio 2
def primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

lista = list(range(0,101))
for numero_p in lista:
    if primo(numero_p):
        print(numero_p)
     
# Ejercicio 3
def año_bis(año):
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                return True
            else:
                return False
        return True
    return True

años_ver = [2000, 2004 , 2100, 2200, 2300, 2400]  
for i in años_ver:
    if año_bis(i):
        print(f'{i} es primo')
    else:
        print(f'{i} no es primo')
