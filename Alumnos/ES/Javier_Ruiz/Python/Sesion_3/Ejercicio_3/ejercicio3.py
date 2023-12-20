# Identificar si un año es bisiesto o no.
lista_anos = list(range(2000,2050))
anos_bisiestos = []

for ano in lista_anos:
    # Paso 1: Si el año es divisible por 4.
    if ano % 4 == 0:
        # Paso 2: Si el año es divisible por 100.
        if ano % 100 == 0:
            # Paso 3: Si el año es divisible por 400
            if ano % 400 == 0:
                anos_bisiestos.append(ano)  # Paso 4: El año es un año bisiesto.
        else:
            anos_bisiestos.append(ano)  # Si es divisible entre 4 y no entre 100, es un ano bisiesto.

print(anos_bisiestos)
