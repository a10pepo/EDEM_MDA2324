#EJERCICIO SESIÓN 1

name = "Martin"

print (f'¡Hola, {name}!')

#EJERCICIO SESIÓN 2

cantidad_input = float(input("Hola. Bienvenido al sistema de cálculo de inversiones. ¿Cuánto quieres invertir?\n"))
interes_input = float(input("¿Cuál es el interés anual?\n"))
anos_input = int(input("¿Cuántos años vas a mantener la inversión?\n"))

print(f"En {anos_input} años habrás recibido {cantidad_input * (interes_input/100) * anos_input}€ de interés")

#EJERCICIO SESIÓN 3

inversion = (input("Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?\n"))

if inversion == "1":
    cantidad_input = float(input("Hola. ¿Cuánto quieres invertir?\n"))
    interes_input = float(input("¿Cuál es el interés anual?\n"))
    anos_input = int(input("¿Cuántos años vas a mantener la inversión?\n"))

    print (f"En {anos_input} años habrás recibido {(cantidad_input * interes_input / 100) * anos_input}€ de interés")

elif inversion == "X":
    
    print ("¡Nos vemos!")
    exit()
   
else: 
    print ("Este mensaje no es válido. Introduce 1 para calcular la inversión o X para salir")

#CALCULADORA DE NUMEROS PRIMOS

list_primos = []

number = int(input("Escribe el número límite: "))

cont = 0

for i in range(2, number + 1):
    for j in range(2 , int(i/2) + 1):
        if i % j == 0:
            cont += 1
    
    if cont == 0:
        list_primos.append(i)
    cont = 0

print(list_primos)

#CALCULADORA AÑOS BISIESTOS

anos_bisiesto = []

cont = 0

anyo = int(input("Escribe el año aquí: "))

for i in range(1800, anyo +1):
    if i % 4 == 0:
        if i % 100 == 0:
            print("No es bisiesto")
            
        elif i % 100 and i % 400 == 0:
            anos_bisiesto.append(i)
        else:
            anos_bisiesto.append(i)

print(anos_bisiesto)