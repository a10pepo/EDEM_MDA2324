def calcular_inversion():
    print("Hola. Bienvenido al sistema de cálculo de inversiones.")
    
    # Paso 1
    inversion = float(input("¿Cuánto quieres invertir? "))
    
    # Paso 2
    interes_anual = float(input("¿Cuál es el interés anual? "))
    
    # Paso 3
    anos = int(input("¿Cuántos años vas a mantener la inversión? "))
    
    # Paso 4 - Final
    cantidad_generada = inversion * (1 + (interes_anual / 100)) ** anos
    interes_generado = cantidad_generada - inversion
    
    print(f"\nEn {anos} años habrás recibido {interes_generado:.2f}€ de interés.")
    
if __name__ == "__main__":
    calcular_inversion()
