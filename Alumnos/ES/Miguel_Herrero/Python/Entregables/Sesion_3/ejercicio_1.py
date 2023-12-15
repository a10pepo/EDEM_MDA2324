def calcular_inversion():
    while True:
        print("Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?")
        print("[1] Calcular una inversión")
        print("[X] Salir")
        
        opcion = input(">> ").upper()

        if opcion == "1":
            inversion = float(input("¿Cuánto quieres invertir? "))
            
            interes_anual = float(input("¿Cuál es el interés anual? "))
            
            anos = int(input("¿Cuántos años vas a mantener la inversión? "))
            
            cantidad_generada = inversion * (1 + (interes_anual / 100)) ** anos
            interes_generado = cantidad_generada - inversion
            
            print(f"\nEn {anos} años habrás recibido {interes_generado:.2f}€ de interés.")
            
            print("\n¿Qué quieres hacer ahora?")
            print("[1] Calcular una nueva inversión")
            print("[X] Salir")
            
            opcion_nueva = input(">> ").upper()
            
            if opcion_nueva == "X":
                print("\n¡Nos vemos!")
                exit()
        elif opcion == "X":
            print("\n¡Nos vemos!")
            exit()
        else:
            print("\nOpción no válida. Por favor, elige 1 o X.")

if __name__ == "__main__":
    calcular_inversion()
