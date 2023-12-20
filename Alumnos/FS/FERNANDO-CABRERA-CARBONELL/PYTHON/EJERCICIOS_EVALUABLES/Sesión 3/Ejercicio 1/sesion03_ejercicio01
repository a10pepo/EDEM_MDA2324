def calcular_inversion():
    print("Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?")
    opcion = ""

    while opcion.upper() != "X":
        print("[1] Calcular una inversión")
        print("[X] Salir")
        opcion = input("Introduce tu elección: ")

        if opcion == "1":
            print("Hola, vamos a calcular la cantidad generada de intereses en función de la cantidad que quieras invertir")

            cantidad_inversion = float(input("¿Cuánto quieres invertir? "))
            interes_anual = float(input("Introduce el interés anual en porcentaje - Recuerda introducir los décimales con un punto y no introducir el símbolo %. Introduce el valor aquí: "))
            numero_anos = int(input("¿A cuántos años quieres hacer la inversión? "))

            cantidad_generada = cantidad_inversion * (interes_anual / 100) * numero_anos

            print(f"En {numero_anos} años habrás recibido {cantidad_generada} € de intereses.")
            opcion = input("¿Qué quieres hacer ahora?\n[1] Calcular una nueva inversión\n[X] Salir\n")
        elif opcion.upper() == "X":
            print("¡Gracias, adiós!")
        else:
            print("Opción inválida. Por favor, elige una opción válida: [1] o [X]")

        # Llamar a la función para calcular la inversión
calcular_inversion()
