import sys

# Verificar que se pasaron dos argumentos además del nombre del script
if len(sys.argv) == 3:
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        suma = num1 + num2
        print(f"Sum: {suma}")
    except ValueError:
        print("Por favor, introduce dos números.")
else:
    print("Se requieren exactamente dos argumentos.")
