def es_primo():
    numero = int(input('Introduce un número entero: '))

    if numero <= 1:
        print('El número no es primo')
        return

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            print('El número no es primo')
            break
    else:
        print('El número es primo')

es_primo()
