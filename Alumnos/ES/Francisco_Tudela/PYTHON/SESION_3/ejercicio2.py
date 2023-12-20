def primos():
    lista = list(range(2,101))
    primos_lista = []
    for num in lista:
        es_primo = True
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            primos_lista.append(num)
    return primos_lista

resultado = primos()
print(resultado)

