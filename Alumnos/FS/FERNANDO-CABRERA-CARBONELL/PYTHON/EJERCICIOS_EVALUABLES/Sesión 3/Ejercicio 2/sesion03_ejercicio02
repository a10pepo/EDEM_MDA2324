def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def mostrar_primos_en_rango(rango_inicio, rango_fin):
    print(f"Los números primos en el rango de {rango_inicio} a {rango_fin} son:")
    for num in range(rango_inicio, rango_fin + 1):
        if es_primo(num):
            print(num, end=" ")

mostrar_primos_en_rango(1, 100)
