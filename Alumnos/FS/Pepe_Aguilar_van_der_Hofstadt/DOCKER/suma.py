import sys

if len(sys.argv) == 3:      # CONTROLA EL NUMERO DE ARGUMENTOS PASADOS POR CONSOLA
    try:                    # CONTROLA QUE SE HAYAN INTODUCIDO NÚMEROS
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        suma = num1 + num2
        print(f'La suma da {suma}')
    except:
        print("ERROR: NO HAS INTRODUCIDO NUMEROS")
    
else:
    print("ERROR: NUMERO DE ARGUMENTOS INCORRECTO")