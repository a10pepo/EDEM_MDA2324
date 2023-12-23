# Crea una aplicación de consola que calcule los resultados de una inversión. Debe
# Pedir por consola una cantidad (numérica) de Inversión
# Pedir el % de interés anual
# Pedir el número de años que se va a mantener la inversión
# Finalmente, calcular la cantidad generada en los años especificados por el usuario

print("Hola. Bienvenido al sistema de cálculo de inversiones. ¿Cuánto quieres invertir?")
inversion = int(input())
print(f'Vas a invertir {inversion} euros.')

print("¿Cual es el interés anual de la inversión?")
interes = int(float(input()))/100
print(f'El interés anual de la inversión será de un {interes}%.')

print("¿A cuántos años es la inversión?")
años_inversion = int(input())
print(f"Se invertirán {inversion} euros a un interés del {interes}% anual durante {años_inversion} años.")
print(f"Esto generará unos intereses de {(inversion * interes) * años_inversion} euros en los {años_inversion} años de duración de la inversión.")