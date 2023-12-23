
# Primer apartado del ejercicio
print("Hola. Este programa le ayuda a calcular los números primos de un rango.")

inicio_rango = int(input("Por favor, indique el valor inicial del rango: "))

final_rango_a = int(input("Por favor, indique el valor final del rango: "))

# Le añadimos 1 ya que el rango de cierre se indica siempre con un número más
final_rango_b:int = final_rango_a + 1

numeros_primos = []
numeros_no_primos = []

for i in range(inicio_rango, final_rango_b):
    if i < 2:
        numeros_primos.append(i)
    elif i == 2:
        numeros_primos.append(i)
    else:
        es_primo = True
        for y in range(2, int(i**0.5) + 1):
            if i % y == 0:
                es_primo = False
                break
        if es_primo:
            numeros_primos.append(i)
        else:
            numeros_no_primos.append(i)

print("Los valores primos de este listado son:")
print(numeros_primos)

# Segundo apartado del ejercicio
print("Ahora, si desea calcular si un número en concreto es primo o no, por favor indíquelo a continuación")

dime_si_primo = int(input("Número: "))

if dime_si_primo < 2:
    print("Lo siento, me temo que tu número no es primo")
else:
    es_primo = True
    for y in range(2, int(dime_si_primo**0.5) + 1):
        if dime_si_primo % y == 0:
            es_primo = False
            break

    if es_primo:
        print("Efectivamente, su número es primo")
    else:
        print("Lo siento, me temo que tu número no es primo")

# Tercer apartado del ejercicio
print("A continuación, si me indicas un año (en formato YYYY) puedo decirte si es bisiesto o no")

valor_entrada = int(input("¿Qué año debería calcular? "))

if (valor_entrada % 400 == 0) and (valor_entrada % 100 == 0):
    print(f"{valor_entrada} es año bisiesto")
    # Si no es divisible entre 100 (siglo) pero sí entre 4, es bisiesto
elif (valor_entrada % 4 == 0) and (valor_entrada % 100 != 0):
    print(f"{valor_entrada} es año bisiesto")
else:
    # Si no lo es, entonces no es bisiesto
    print(f"{valor_entrada} no es año bisiesto")