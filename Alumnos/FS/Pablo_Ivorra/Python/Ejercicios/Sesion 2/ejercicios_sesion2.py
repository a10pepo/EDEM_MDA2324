#Crea una aplicación de consola que calcule los resultados de una inversión. Debe
#1.Pedir por consola una cantidad (numérica) de Inversión
#2.Pedir el % de interés anual
#3.Pedir el número de años que se va a mantener la inversión
#4.Finalmente, calcular la cantidad generada en los años especificados por el usuario

print("Bienvenido al sistema de cálculo de inversiones.")

while True:
    try:
        dinero = float(input("¿Cuánto dinero tienes para invertir (€)? "))
        break
    except ValueError:
        print("Por favor, introduce un número válido.")

while True:
    try:
        interes = float(input("¿Cuál es el interés anual? \nEscríbelo en decimal, ej 5% = 0.05: "))
        break
    except ValueError:
        print("Por favor, introduce un número en formato decimal válido.")

while True:
    try:
        ano = int(input("¿Cuántos años quieres mantener la inversión? "))
        break
    except ValueError:
        print("Por favor, introduce un número entero válido.")

profit = dinero * interes * ano

print(f"En {ano} años tendrás {profit}€ de interés.")
