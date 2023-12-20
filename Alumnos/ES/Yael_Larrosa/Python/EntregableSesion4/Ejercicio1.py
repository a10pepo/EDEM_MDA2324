#Crea una función que reciba un rango de números como parámetro y muestre por consola únicamente los valores primos

def primo (lista):

  lista_final=[]

  for numero in lista:
    lista_numero=list(range(1,numero+1))
    lista_comprobacion=[]
    lista_primo=[1,numero]
    
    for elemento in lista_numero:
      resto=numero%elemento
      if (resto==0):
        lista_comprobacion.append(elemento)

    if(lista_comprobacion==lista_primo):
      lista_final.append(numero)

  return(lista_final)

#comprobación de que funciona:
prueba=[3,7,9,11,23,15,16,17,80]
    
resultado_lista= primo(prueba)
print(f'de la lista {prueba} los numeros primos son los siguientes: {resultado_lista}')

#Crea una función que pueda evaluar si un número (pasado por parámetro) es primo o no

def identificacion_primo(numero):
  lista_numero=list(range(1,numero+1))
  lista_comprobacion=[]
  lista_primo=[1,numero]

  for elemento in lista_numero:
    resto=numero%elemento
    if (resto==0):
      lista_comprobacion.append(elemento)

  if(lista_comprobacion==lista_primo):
    print(f'El numero {numero} es un número primo')
  else:
    print(f'El numero {numero} no es un número primo')

#comprobacion de que funciona:
identificacion_primo(7)


  
               
#Crea una función que reciba un año y pueda indicarte con True o False si es un año bisiesto o no.

def identificacion_bisiesto (año):
  return (((año%100==0)&(año%400!=0))|(año%400==0)|(año%4==0))

#comrpobación de que funciona:
resultado= identificacion_bisiesto(2010)
if (resultado==False):
  print('no es un año bisiesto')
else:
  print('si es un año bisiesto')

