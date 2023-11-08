#Crea un programa en Python que sea capaz de calcular y mostrar por consola todos los números primos de 1 - 100

listaPrimos = []

for numero in range (2,101):
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break   
    if (es_primo == True):
        listaPrimos.append(numero)
        
print(f"{listaPrimos}")