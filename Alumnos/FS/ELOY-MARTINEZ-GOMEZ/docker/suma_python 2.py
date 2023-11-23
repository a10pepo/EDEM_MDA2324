import sys
"""Script que recibe como argumentos x números y los suma, mostrando la formula y el resultado"""

suma = 0
listado_suma = []
for i in range(len(sys.argv)):
    if i != 0: # primer parametro es script.py
        listado_suma.append(sys.argv[i])
        suma += float(sys.argv[i])
    else:
        pass
funcion_suma = ' + '.join(listado_suma)
print(f"El resultado es: {funcion_suma} = {suma}")