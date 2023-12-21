"""Escribe un programa que pueda decirte si un número 
(número entero) es primo o no"""

numero = int(input("¿Qué número quieres saber si es primo? "))


if numero < 2:
    print("No es primo")
elif numero == 2:
    print("Es primo")
else:
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print("Es primo")
    else:
        print("No es primo")
