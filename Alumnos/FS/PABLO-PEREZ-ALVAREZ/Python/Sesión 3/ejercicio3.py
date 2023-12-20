
# Lista de años de ejemplo
lista = [2000, 2001, 2002, 2003, 2004, 2005]

# La fórmula que quiero usar para calcular si cada año es bisiesto o no
for i in lista:
    # Si es divisible entre 100 (siglo) y entre 400, es bisiesto
    if (i % 400 == 0) and (i % 100 == 0):
        print(f"{i} es año bisiesto")
    # Si no es divisible entre 100 (siglo) pero sí entre 4, es bisiesto
    elif (i % 4 == 0) and (i % 100 != 0):
        print(f"{i} es año bisiesto")
    else:
    # Si no lo es, entonces no es bisiesto
        print(f"{i} no es año bisiesto")