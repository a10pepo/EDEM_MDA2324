#Calculadora de Inversión (Clase anterior)

print("Bienvenido al sistema de cálculo de inversiones.")
dinero = float(input("Cuanto dinero tienes para invertir (€)? "))
interes = float(input("Cual es el interés anual? \nEscribelo en decimal, ej 5% = 0.05. "))
ano = int(input("Cuantos años quieres mantener la inversión? "))
profit = dinero*interes*ano

print(f"En {ano} años tendrás {profit}€ de interés")

#Calculadora de Inversión 2.0 (Opción Salir)

def calcular_inversion():
    print("Bienvenido al sistema de cálculo de inversiones.")
    dinero = float(input("Cuanto dinero tienes para invertir (€)? "))
    interes = float(input("Cual es el interés anual? \nEscribelo en decimal, ej 5% = 0.05. "))
    ano = int(input("Cuantos años quieres mantener la inversión? "))
    profit = dinero * interes * ano
    print(f"En {ano} años habrás recibido {profit}€ de interés. ¿Qué quieres hacer ahora?")
    mostrar_menu()

def mostrar_menu():
    while True:
        print("Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?")
        print("[1] Calcular una inversión")
        print("[X] Salir")
        opcion = input("Elige una opción: ").upper()

        if opcion == '1':
            calcular_inversion()
        elif opcion == 'X':
            print("¡Hasta la vista baby!")
            exit()
        else:
            print("Espabila, introduce 1 o X para proceder.")

# Inicia el programa mostrando el menú principal.
mostrar_menu()



