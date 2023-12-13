# 1.Creamos la imagen pysum --> docker build -t pysum .

import sys

a = int(sys.argv[1])
b = int(sys.argv[2]) #recibe como parámetro la línea de comandos de docker

def suma(a,b):
    suma = a + b
    print(f"La suma es: {suma}")

suma (a,b)

# 2.Ejecutamos el script --> docker run pysum 3 4