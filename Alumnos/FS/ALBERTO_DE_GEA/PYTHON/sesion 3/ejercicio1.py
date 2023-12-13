while True:
    print("Bienvendio al sistema de inversiones, ¿Que quieres hacer?")
    print("[1] Calcular una inversión")
    print("[X] Salir")

    opcion = input("Selecciona una opción (1/X): ").upper()

    if opcion == "1":
        inversión = float(input("¿Cuanto quieres invertir?"))
        print(f"Quieres invertir{inversión}€")
        print("¿Cuál es el interes?")
        interes = float(input())
        print(f"El interes es {interes}%")
        print("¿En cuantos años?")
        numero_años = int(input())
        print(f"En {numero_años} años")
        cantidad_generada = inversión * (1 + (interes / 100)) ** numero_años
        print(f"La cantidad generada en {numero_años} años será: {cantidad_generada:.2f}")

    elif opcion == "X":
        print("¡Nos vemos!")
    break  
else:
    print("Opción no válida. Por favor, selecciona 1 o X.")