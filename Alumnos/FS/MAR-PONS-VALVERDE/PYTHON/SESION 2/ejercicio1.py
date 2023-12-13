# Crea una aplicación de consola que calcule los resultados de una inversión. Debe
#Pedir por consola una cantidad (numérica) de Inversión
#Pedir el % de interés anual
#Pedir el número de años que se va a mantener la inversión
#Finalmente, calcular la cantidad generada en los años especificados por el usuario
#Debería resultar en algo así vía consola:

saludo= ('Hola. Bienvenido al sistema de cálculo de inversiones')
print(saludo)
cantidad_invertir=int(input('¿Cuánto quieres invertir? :'))
print(cantidad_invertir)
interes_anual=int(input('¿Cuál es el interes a invertir :'))
print(interes_anual)
años_inversion=int(input('¿Cuántos años vas a mantener la inversión? :'))
print(años_inversion)  
cantidad_generada=int(200*0.05)
print(cantidad_generada)  
print('En 2 años habrás recibido  10€ de interés')          