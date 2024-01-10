#Crea un programa en Python que sea capaz de calcular y mostrar por consola todos los números primos de 1 - 100
def numero_primo(numero): 
    if numero < 2: 
        return False

    for i in range (2, int(numero ** 0.5) +1):
        if numero % i == 0: 
            return False
    return True

list_primos = []

for num in range (1,100):
    if numero_primo (num):
        list_primos.append (num)
print ("Números primos ")
print(list_primos)
    
    