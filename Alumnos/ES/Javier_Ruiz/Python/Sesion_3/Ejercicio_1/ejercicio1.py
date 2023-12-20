def calcular_inversion():
    while True:
        print("Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?")
        print("[1] Calcular una inversión")
        print("[X] Salir")

        opcion = input("> ")

        if opcion == "X":
            print("¡Nos vemos!")
            print("(aplicación cerrada con un exit())")
            exit()

        elif opcion == "1":
            # Paso 1
            inversion = float(input("¿Cuánto quieres invertir? (€) "))
            
            # Paso 2
            interes_anual = float(input("¿Cuál es el interés anual? (%) "))
            
            # Paso 3
            anos_inversion = int(input("¿Cuántos años vas a mantener la inversión? "))
            
            # Paso 4 - Final
            cantidad_generada = inversion * (1 + interes_anual / 100) ** anos_inversion
            interes_generado = cantidad_generada - inversion
            
            print(f"En {anos_inversion} años habrás recibido {interes_generado:.2f}€ de interés.")
            
            # Opción para realizar otra inversión o salir
            print("¿Qué quieres hacer ahora?")
            print("[1] Calcular una nueva inversión")
            print("[X] Salir")
            
            opcion_nueva = input("> ")
            
            if opcion_nueva == "X":
                print("¡Nos vemos!")
                print("(aplicación cerrada con un exit())")
                exit()
        else:
            print("Opción no válida. Por favor, elige 1 o X.")

calcular_inversion()
