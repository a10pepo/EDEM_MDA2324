# EJERCICIO SESION 2

print('Hola. Bienvenido al sistema de cálculo de inversiones.')
cant = int(input('¿Cuánto quieres invertir? '))
porcentaje = (int(input('¿Cual es el interés anual en porcentaje? '))) / 100
años = int(input('¿Cuántos años vas a mantener la inversión? '))
print(f'En {años} años, habrás recibido {cant * porcentaje * años}€ de interés')