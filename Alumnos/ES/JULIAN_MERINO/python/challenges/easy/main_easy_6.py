"""
Reto 6

Escribe un programa que pregunte al usuario 
su edad y muestre por pantalla si es mayor de edad o no.
"""
# We can use an if else loop for this
age = int(input('Enter your age: '))
if age >= 18:
  print('Of legal age.')
else:
  print('Under 18.')