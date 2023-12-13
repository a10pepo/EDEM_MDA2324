import sys

if len(sys.argv) == 3:
    print("Por favor, proporciona dos números como argumentos.")
else:
    try:
        primer_numero = float(sys.argv[1])
        segundo_numero = float(sys.argv[2])
        suma = primer_numero + segundo_numero
        print(f"La suma es: {suma}")
    except ValueError:
        print("Por favor, asegúrate de ingresar números válidos como argumentos.")
