#Ejercicio 1.1
def primo(num):
    es_primo = True
    for i in range(2, int(num ** 0.5) + 1):
         if num % i == 0:
            es_primo = False
            break
    return es_primo
    

resultado = primo(983)
print(resultado)

#Ejercicio 1.3
def bisiesto(año):
    es_bisiesto = False
    if año % 4 == 0:
        es_bisiesto = True
    elif año % 100 == 0 and año % 400 == 0:
        es_bisiesto = True
    return es_bisiesto
        
Años_bisiestos = bisiesto(2024)
print(Años_bisiestos)

