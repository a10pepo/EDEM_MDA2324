# Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
#teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]

inicio = int(input("ingresa el numero de inicio: "))
final = int(input("ingresa el numero final: "))
if inicio % 2==0:
    inicio +=1

print("Numeros impares en el rango:")
for numero in range(inicio, final + 1, 2):
    print(numero)

    

