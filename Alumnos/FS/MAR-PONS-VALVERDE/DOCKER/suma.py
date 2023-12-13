#Construir un script en python que acepte dos números como parámetros e imprima el resultado de la suma

import sys #

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Por favor, proporciona dos números como argumentos.")
    else:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        suma = num1 + num2
        print(f"La suma de {num1} y {num2} es: {suma}")

