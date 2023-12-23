def calcular_valor_futuro(cantidad_inicial, tasa_interes, tiempo):
    # Calcula el valor futuro de una inversión.
    tasa_decimal = tasa_interes / 100.0
    valor_futuro = cantidad_inicial * (1 + tasa_decimal) ** tiempo
    return valor_futuro

def main():
    # Pedir la cantidad de inversión
    cantidad_inicial = float(input("¿Cuánto quieres invertir? "))

    # Pedir el % de interés anual
    tasa_interes = float(input("¿Cuál es el interés anual? "))

    # Pedir el número de años
    tiempo = int(input("¿Cuántos años vas a mantener la inversión? "))

    # Calculamos el valor futuro
    resultado = calcular_valor_futuro(cantidad_inicial, tasa_interes, tiempo)

    # Redondeamos el resultado a dos decimales
    resultado_redondeado = round(resultado, 2)

    # Se muestra el resultado final
    print("En {} años habrás recibido {:.2f}€ de interés".format(tiempo, resultado_redondeado))

if __name__ == "__main__":
    main()