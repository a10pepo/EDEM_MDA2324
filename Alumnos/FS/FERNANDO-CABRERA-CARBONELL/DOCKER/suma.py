import sys

def sumar(a,b):
    return a + b

if len(sys.argv) != 3: # confirmamos que queremos dos número como parámetros y no más, así si ponemos 3, nos avisa que son solo dos
    print("Inserta dos números como parámetros")
else:
    numero_uno = float(sys.argv[1])
    numero_dos = float(sys.argv[2])
    resultado = sumar(numero_uno, numero_dos)
    print(f'Resultado suma: {resultado}')
