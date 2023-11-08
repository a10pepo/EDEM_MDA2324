#Crea una aplicación de consola que calcule los resultados de una inversión. Debe
#Pedir por consola una cantidad (numérica) de Inversión
#Pedir el % de interés anual
#Pedir el número de años que se va a mantener la inversión
#Finalmente, calcular la cantidad generada en los años especificados por el usuario

print(f'Hola, bienvenido al sistema de cálculo de inversiones\n'
      f'¿Cuánto quieres invertir?')
euros = input('')
euros = float(euros)

print("¿Cuál es el interés anual?")
interes = input('')
interes = float(interes)

print("¿Cuántos años vas a mantener la inversion?")
años = input('')
años = float(años)

calculoInteres = euros * (1 + (interes / 100)) ** años - euros

print(f"En {años} años habrás recibido {calculoInteres} euros de interés")