# Escribe un programa que contenga dos variables. Una de ellas representa la contraseña de un usuario y la otra un texto introducido.  
# El programa debe poder mostrar por pantalla si las dos cadenas de texto son iguales sin tener en cuenta mayúsculas y minúsculas.

contraseña = "Mar953"
texto_introducido = input("Introduce tu texto: ")

if texto_introducido.upper() == contraseña.upper():
    print(" Las contraseñas son iguales (ingnorando mayúsculas y minúsculas).")

else: 
    print("Las contraseñas no son iguales (ingnorando mayúsculas y minúsculas).")    

#TAMBIEN SE PUEDE PONER CON LOWER