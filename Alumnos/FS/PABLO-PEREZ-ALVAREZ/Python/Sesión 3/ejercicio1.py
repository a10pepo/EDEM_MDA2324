def calcular_valor_futuro(cantidad_inicial, tasa_interes, tiempo):
    
    tasa_decimal = tasa_interes / 100.0
    valor_futuro = cantidad_inicial * (1 + tasa_decimal) ** tiempo
    return valor_futuro

def main():
    while True:
        print("\nHola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?")
        print("[1] Calcular una inversión")
        print("[X] Salir")

        opcion = input().upper()

        if opcion == "1":
            # Pedir la cantidad de inversión
            cantidad_inicial = float(input("Ingrese la cantidad de inversión: "))

            # Pedir el % de interés anual
            tasa_interes = float(input("Ingrese la tasa de interés anual (%): "))

            # Pedir el número de años
            tiempo = int(input("Ingrese el número de años que se va a mantener la inversión: "))

            # Calcular el valor futuro
            resultado = calcular_valor_futuro(cantidad_inicial, tasa_interes, tiempo)

            # Redondear el resultado a dos decimales
            resultado_redondeado = round(resultado, 2)

            # Mostrar el resultado y opciones posteriores
            print("En {} años habrás recibido {:.2f}€ de interés.".format(tiempo, resultado_redondeado))
            print("¿Qué quieres hacer ahora?")
            print("[1] Calcular una nueva inversión")
            print("[X] Salir")
        elif opcion == "X":
            print("¡Nos vemos!")
            exit()
        else:
            print("Opción no válida. Por favor, ingrese 1 para calcular una inversión o X para salir.")

if __name__ == "__main__":
    main()