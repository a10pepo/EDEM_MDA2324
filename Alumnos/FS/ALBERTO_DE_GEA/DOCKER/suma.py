import sys

if len(sys.argv) != 3:
    print("Uso: python sumar.py <numero1> <numero2>")
    sys.exit(1)

try:
    numero1 = float(sys.argv[1])
    numero2 = float(sys.argv[2])
except ValueError:
    print("Los argumentos deben ser números válidos.")
    sys.exit(1)

resultado = numero1 + numero2
print(f"La suma de {numero1} y {numero2} es: {resultado}")
