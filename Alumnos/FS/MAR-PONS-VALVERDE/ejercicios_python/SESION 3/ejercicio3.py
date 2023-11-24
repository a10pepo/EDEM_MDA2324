# Crea un programa en Python que sea capaz de identificar a partir de una lista de años si un año es bisiesto o no.
# Solicitar al usuario el año inicial y el año final
inicio = int(input("Ingrese el año inicial: "))
final = int(input("Ingrese el año final: "))

# Iterar a través de los años en el rango proporcionado
print("Años bisiestos en el rango de", inicio, "a", final, ":")
for year in range(inicio, final + 1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year)
