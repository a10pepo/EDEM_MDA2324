def es_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

def ano_bisiesto(año):
    if es_bisiesto(año):
        print(f"{año} es un año bisiesto.")
    else:
        print(f"{año} no es un año bisiesto.")

# Ejemplo de uso de la función
año_evaluado = 2020  # Año 
ano_bisiesto(año_evaluado)
