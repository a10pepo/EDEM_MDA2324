# Importamos el módulo sys para obtener los argumentos
import sys

# Obtenemos los argumentos de la línea de comandos
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

# Calculamos la suma
suma = num1 + num2

# Imprimimos el resultado
print(f"El resultado de sumar {num1} y {num2} es: {suma}")

