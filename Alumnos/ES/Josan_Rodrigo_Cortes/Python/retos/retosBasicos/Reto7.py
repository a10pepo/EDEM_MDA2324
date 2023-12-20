""" Escribe un programa que contenga dos variables. Una de ellas representa la contraseña de un usuario
y la otra un texto introducido. El programa debe poder mostrar por pantalla si las dos cadenas de
texto son iguales sin tener en cuenta mayúsculas y minúsculas. """



contrasenya=input("Introduce la contraseña")
texto=input("Introduce el texto")
sinMcontrasenya=contrasenya.lower()
sinMtexto=texto.lower()

if sinMcontrasenya==sinMtexto:
    print("Son iguales")
else:
    print("Son distintas")