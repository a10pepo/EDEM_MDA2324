import sys

def suma_numeros(num1, num2):
        resultado = int(num1) + int(num2)
        print(f"Sum: {resultado}")
        
if len(sys.argv) == 3:
    suma_numeros(sys.argv[1], sys.argv[2])
else:
    print("Error: Por favor, proporcione dos números como parámetros.")