#Reto Entregable 3:

opcion_escogida= ''

while(opcion_escogida != 'x'):
    opcion_escogida = input(
'''
Hola, selecciona que deseas realizar:

1. Calcular una inversion:
x. Salir
''')
    
    if (opcion_escogida) == '1':
        amount:int=(input('Cuanto quieres invertir (£))?'))
        interest:int=(input('Cual es el interes anual actual (%))?'))
        years:int=(input('¿Cuántos años vas a mantener la inversión?'))

        total = amount*(1+interest/100)**years
        print(f'la inversión total de {amount} dutante {years} años al {interest}% es igual a {total}')
    else:
        print("Gracias por utilizar nuestro programa")

#numero primos:

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numeros_primos_hasta_100():
    primos = [num for num in range(1, 101) if es_primo(num)] #usamos comprension de listas
    return primos

primos_en_rango = numeros_primos_hasta_100()
print("Números primos de 1 a 100:")
print(primos_en_rango)
