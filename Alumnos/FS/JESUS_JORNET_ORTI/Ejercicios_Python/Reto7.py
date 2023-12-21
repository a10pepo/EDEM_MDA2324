"""Escribe un programa que contenga dos variables. 
Una de ellas representa la contraseña de un usuario 
y la otra un texto introducido. El programa debe poder 
mostrar por pantalla si las dos cadenas de texto son 
iguales sin tener en cuenta mayúsculas y minúsculas."""

usuario = "User"
password = "uSeR"
upper_str_usuario = usuario.upper()
upper_str_password = password.upper()

if upper_str_usuario == upper_str_password:
        print ("Son iguales")
else:
        print ("No son iguales")
