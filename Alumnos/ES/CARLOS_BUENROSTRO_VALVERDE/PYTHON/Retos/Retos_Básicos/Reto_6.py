# # Reto 6: Escribe un programa que pregunte al usuario su edad y muestre por pantalla si
# # es mayor de edad o no.

print("Bienvenido al programa. Introduzca su edad, por favor")

edad = int(input())

if edad >= 18:
  print("Eres mayor de edad. Puedes acceder al programa.")
else:
  print("Lo siento, no puedes acceder al siguiente programa.")