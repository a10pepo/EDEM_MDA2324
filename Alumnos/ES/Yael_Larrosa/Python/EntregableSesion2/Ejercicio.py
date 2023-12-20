'''
Crea una aplicación de consola que calcule los resultados de una inversión. Debe
Pedir por consola una cantidad (numérica) de Inversión
Pedir el % de interés anual
Pedir el número de años que se va a mantener la inversión
Finalmente, calcular la cantidad generada en los años especificados por el usuario
'''

print(f'Hola. Buenvenido al sistema de cálculo de inversiones.\n ¿Cuánto quieres invertir?')
cantidad_inversion= float(input(f'(El usuario escribe aquí la cantidad)'))

print('¿Cuál es el interés anual?')
interes_anual = float(input(f'((El usuario escribe aquí el interés anual)'))

print('¿Cuántos años va a mantener la inversión?')
tiempo_inversion = int(input(f'(El usuario escribe aquí el nº de años)'))

cantidad_recibida =round(cantidad_inversion*(interes_anual/100)*tiempo_inversion,2) 

print(f'En {tiempo_inversion} años habrás recibido {cantidad_recibida} € de interés')
