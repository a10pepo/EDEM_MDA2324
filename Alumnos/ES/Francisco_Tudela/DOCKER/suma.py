import sys

def sumatorio(a, b):
    try:
        num1 = int(a)
        num2 = int(b)
        resultado = num1 + num2
        return resultado
    except ValueError:
        return "Error: Por favor, proporciona dos números válidos."

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Proporciona dos números para sumar.")
        sys.exit(1)

    num1 = sys.argv[1]
    num2 = sys.argv[2]

    resultado = sumatorio(num1, num2)

    print(f"El resultado de la suma de {num1} y {num2} es: {resultado}")

