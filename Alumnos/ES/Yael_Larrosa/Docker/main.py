#importar la librería sys
import sys

#establecer los valores que van a ser sumados --> el sys.argv[] sirve para que en la linea de comandos sepa interpretar valor1 y valor 2
valor1 = float(sys.argv[2])
valor2 = float(sys.argv[1])

#sumar los valores
resultado = valor1 + valor2

#imprimir el resultado
print(f'La suma de los numeros {valor1} y {valor2} es:  {resultado}')