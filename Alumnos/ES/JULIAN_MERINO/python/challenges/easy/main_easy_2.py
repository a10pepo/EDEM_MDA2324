"""
RETO 2

Escribe un programa capaz de mostrar todos los números impares desde un número de 
inicio y otro final.
Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]
"""
initial_num = -5
final_num = 11
# Iterate through the range, bearing in mind that the first element is i = 0
for i in range((1 + final_num) - initial_num):
  # Condition: if % is not 0, then the number is an odd one and is printed:
  if (initial_num + i) % 2 != 0:
    print(initial_num + i)
    