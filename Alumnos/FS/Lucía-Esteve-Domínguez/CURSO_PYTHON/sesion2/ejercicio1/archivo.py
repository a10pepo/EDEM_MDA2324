'''Crea una aplicación de consola que calcule los resultados de una inversión. 
Debe pedir por consola: 
1. cantidad (numérica) de Inversión
2. el % de interés anual
3. el número de años que se va a mantener la inversión
4. calcular la cantidad generada en los años especificados por el usuario'''

saludo = "Hola. Bienvenido al sistema de cálculo de inversión" 
print (saludo)
cantidad_inversion = float (input ("¿cuánto quieres invertir?\n"))
interes_anual = float (input ("¿Cuál es el interés anual?\n"))
duracion_inversion = int (input ("¿Cuántos años vas a mentener la inversión?\n"))
interes_generado = float (cantidad_inversion * (interes_anual/100) * duracion_inversion)
print (f" Has invertido {cantidad_inversion} con un interés anual de {interes_anual}% durante {duracion_inversion} y has generado {interes_generado} de interés")

