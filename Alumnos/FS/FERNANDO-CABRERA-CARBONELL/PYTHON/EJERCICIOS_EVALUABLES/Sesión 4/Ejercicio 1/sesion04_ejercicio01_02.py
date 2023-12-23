def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero_pasado_parametro = 7  # Determinar si el numero pasado como parámetro es primo
if es_primo(numero_pasado_parametro):
    print(f"{numero_pasado_parametro} es un número primo.")
else:
    print(f"{numero_pasado_parametro} no es un número primo.")
