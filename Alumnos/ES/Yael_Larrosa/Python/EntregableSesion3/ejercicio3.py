#Crea un programa en Python que sea capaz de identificar a partir de una lista de años si un año es bisiesto o no.

lista_años = [896,2008,6,8,2012,1978,1654,1234,1567,2659,2002]
lista_bisiestos=[]

for elemento in lista_años :
  if (((elemento%100==0)&(elemento%400!=0))|(elemento%400==0)|(elemento%4==0)):
    lista_bisiestos.append(elemento)


print(f'Los años bisiestos de la lista son: {lista_bisiestos}')