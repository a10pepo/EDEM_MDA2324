'''
Crea una aplicación de consola que calcule los resultados de una inversión. Debe
1.Pedir por consola una cantidad (numérica) de Inversión
2.Pedir el % de interés anual
3.Pedir el número de años que se va a mantener la inversión
4.Finalmente, calcular la cantidad generada en los años especificados por el usuario
'''

print('Hola. Bienvenido al sistema de cálculo de inversiones.')

inversion_inicial = input('¿Cuánto quieres invertir? ')
interes_anual = input('¿Cuál es el interés anual? (%) ')
anos_inversion = input('¿Cuántos años vas a mantener la inversión? ')
resultado_inversion: float = float(inversion_inicial) * (float(interes_anual)/100) *int(anos_inversion)

print(f'En {anos_inversion} años habrás recibido {resultado_inversion:.2f}€ de interés')






