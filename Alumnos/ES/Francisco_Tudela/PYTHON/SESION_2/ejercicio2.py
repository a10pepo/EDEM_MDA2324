print(' Hola. Bienvenido al sistema de cálculo de inversiones.')
inversion = float(input('Indique la cantidad de € a invertir'))
interes = float(input('Indique el interes anual aplicado a la inversión'))
tiempo = int(input('Cuanto tiempo se va a mantener la inversion?'))


euros_generados = inversion * (1+(interes/100))**tiempo
print(f'En {tiempo} años habra generado {euros_generados}')
