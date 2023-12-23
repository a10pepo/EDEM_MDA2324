# Reto 8: Escribe un programa que pueda decirte si un número (numero entero) es primo o no.
def es_primo(num):
  for n in range(2, num):
      if num % n == 0:
          print("No es primo", n, "es divisor")
          return False
  print("Es primo")
  return True