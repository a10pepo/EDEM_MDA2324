def calculo_inversion():
    print("Hola, vamos a calcular la cantidad generada de intereses en función de la cantidad que quieras invertir")

# Pedimos la cantidad que quieren invertir
cantidad_inversion = float(input("¿Cuánto quieres invertir?"))

# Introducimos el interés anual
interes_anual = float(input("Introduce el interés anual en porcentaje - Recuerda introducir los décimales con un punto y no introducir el símbolo %. Introduce el valor aquí: "))

# Introducir los años
numero_anos = int(input("¿A cuántos años quieres hacer la inversión?"))

cantidad_generada= (cantidad_inversion * (interes_anual/100) * numero_anos)

# Resultado final
print(f"En {numero_anos} años habrás recibido {cantidad_generada} € de intereses")