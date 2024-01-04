# # Reto 2: Escribe un programa capaz de mostrar todos los números impares desde un número 
# # de inicio y otro final.
def numeros_impares(inicio, final):
    for numero in range(inicio, final + 1):
        if numero % 2 != 0:
            print(numero)
inicio = int(input("Introduzca el primer número: "))
final = int(input("Introduzca el número final: "))

numeros_impares(inicio, final)