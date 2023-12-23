# EJERCICIO ENTREGABLE SESION 3
# 3.1

print("Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?")
print("[1] Calcular una inversión")
print("[X] Salir")

seleccion = input("Seleccione la opción deseada: ")

while True:
    if seleccion == "1":
        print("Hola. Bienvenido al sistema de cálculo de inversiones. ¿Cuánto quieres invertir?")
        inversion = int(input())
        print(f'Vas a invertir {inversion} euros.')

        print("¿Cual es el interés anual de la inversión?")
        interes = int(float(input()))/100
        print(f'El interés anual de la inversión será de un {interes}%.')

        print("¿A cuántos años es la inversión?")
        años_inversion = int(input())
        print(f"Se invertirán {inversion} euros a un interés del {interes}% anual durante {años_inversion} años.")
        print(f"Esto generará unos intereses de {(inversion * interes) * años_inversion} euros en los {años_inversion} años de duración de la inversión.")
        break
    elif seleccion == "x":
        exit("Muchas gracias por su visita. Nos vemos cuando nos necesite.")
    elif seleccion != 1 or "x":
        print("Por favor, introduzca el valor correcto o pulse [X] para salir del programa. Muchas gracias por su atención.")
        break

# 3.2 Crea un programa en Python que sea capaz de calcular y mostrar por consola todos los números primos de 1 - 100
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def numeros_primos_rango(rango_inicio, rango_fin):
    lista_primos = []
    for numero in range(rango_inicio, rango_fin + 1):
        if es_primo(numero):
            lista_primos.append(numero)
    return lista_primos

primos_en_rango = numeros_primos_rango(1, 100)
print("Los números primos en el rango de 1 a 100 son los siguientes:")
print(primos_en_rango)

# 3.3 Crea un programa en Python que sea capaz de identificar a partir de una lista de años si un año es bisiesto o no.

def leap_year():
    year: int = int(input("Intruduzca el año: "))
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(f'El {year} es bisiesto')
    else:
        print(f'El {year} no es bisiesto. Pruebe con otra fecha.')

leap_year()