import sys

def sumar_numeros(num1, num2):
    try:
        suma = float(num1) + float(num2)
        print(f"Sum: {int(suma) if suma.is_integer() else suma}")
    except ValueError:
        print("Error: Ambos argumentos deben ser números.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Error: Se requieren exactamente dos números como argumentos.")
        sys.exit(1)

    num1 = sys.argv[1]
    num2 = sys.argv[2]
    sumar_numeros(num1, num2)