for elemento in range(2, 101):
    es_primo = True
    for i in range(2, int(elemento**0.5) + 1):
        if elemento % i == 0:
            es_primo = False
            break  

    if es_primo == True:
        print(elemento)
