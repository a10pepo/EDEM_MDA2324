""" Escribe un programa que pregunte al usuario su edad y muestre por pantalla
si es mayor de edad o no. """

edad=0
while edad<18:
    edad=int(input("Introduce tu edad: "))

    if edad<18:
        print("No eres mayor de edad")

    else:
        print("Eres mayor de edad")