#Reto entregable 2:
#Crea una aplicación de consola que calcule los resultados de una inversión. Debe
#Pedir por consola una cantidad (numérica) de Inversión
#Pedir el % de interés anual
#Pedir el número de años que se va a mantener la inversión
#Finalmente, calcular la cantidad generada en los años especificados por el usuario

print('Hola. Bienvenido al sistema de cálculo de inversiones.')
amount:int=(input('Cuanto quieres invertir (£))?'))
interest:int=(input('Cual es el interes anual actual (%))?'))
years:int=(input('¿Cuántos años vas a mantener la inversión?'))

total = amount*(1+interest/100)**years
print(f'la inversión total de {amount} dutante {years} años al {interest}% es igual a {total}')
