#A la aplicación de la calculadora de inversión, deberás añadirle una opción para salir de la consola.

def inversion(cant, inter, anos):
    total = cant * (1 + inter / 100) ** anos
    print(f'La inversión total de {cant} durante {anos} años al {inter}% de interés es igual a {total:.2f}')

def menu():
    print("Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?")
    print("[1] Calcular una inversión")
    print("[X] Salir")

while True:
    menu()
    
    opcion = input("Ingresa tu elección (1/X): ")
    
    if opcion.upper() == 'X':
        print("Saliendo del programa.")
        break
    elif opcion == '1':
        cant = int(input('¿Qué cantidad deseas invertir?: '))
        inter = float(input('Dime el interés anual: '))
        anos = int(input('¿Cuántos años?: '))
        inversion(cant, inter, anos)
    else:
        print("Opción no válida. Por favor, ingresa 1 para calcular una inversión o X para salir.")


#Crea un programa en Python que sea capaz de calcular y mostrar por consola todos los números primos de 1 - 100     
        
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def mostrar_primos(inicio, fin):
    print(f'Números primos de {inicio} a {fin}:')
    for numero in range(inicio, fin + 1):
        if es_primo(numero):
            print(numero, end=' ')

inicio = 1
fin = 100

mostrar_primos(inicio, fin)

#Crea un programa en Python que sea capaz de identificar a partir de una lista de años si un año es bisiesto o no.

def bisiesto(anyo):
    return (anyo % 4 == 0 and anyo % 100 != 0) or (anyo % 400 == 0)

def identificar_bisiestos(lista_anios):
    for anyo in lista_anios:
        if bisiesto(anyo):
            print(f"{anyo} es un año bisiesto.")
        else:
            print(f"{anyo} no es un año bisiesto.")

lista_anyos = [2000, 2001, 2005, 2008, 2010, 2012, 2016, 2019, 2023]

identificar_bisiestos(lista_anyos)


