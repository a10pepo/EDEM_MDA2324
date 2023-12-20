

numeros_primos = []
numeros_no_primos = []

for i in range(1, 101):
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

print(numeros_primos)