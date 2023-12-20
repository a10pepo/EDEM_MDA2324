#Crea una función que reciba un rango de números como parámetro y muestre por consola únicamente los valores primos
def calculadora_primos(inicio_rango, final_rango):
  primos = []
  for numero in range(inicio_rango, final_rango + 1):
      if numero > 1:
          for divisor in range(2, numero):  
              if numero % divisor == 0:
                  break
          else:
              primos.append(numero)

  print("Números primos en el rango:", primos)

calculadora_primos(1, 7)

#Crea una función que pueda evaluar si un número (pasado por parámetro) es primo o no
def es_primo(primito):
    if primito > 1:
        for divisor in range(2, primito):
            if primito % divisor == 0:
                print(f'{primito} no es un número primo')
                break
        else:
            print(f'{primito} es un número primo.')

es_primo(8)



#Crea una función que reciba un año y pueda indicarte con True o False si es un año bisiesto o no.
def es_bisiesto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True  
        else:
            return True
    else:
        return False 

resultado = es_bisiesto(2024)
print(resultado)
