""" Escribe un programa que pueda decirte si un número (número entero) es primo o no """

numero=int(input("Introduce un número: "))

def esPrimo(numero):

    for i in range(2,numero):

        if numero%i==0:
            return False
        else:
            return True
            print(f"El numero {numero} es primo")

esPrimo(5)

""" def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True """