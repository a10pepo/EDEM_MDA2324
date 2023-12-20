"""
Reto 7

Escribe un programa que contenga dos variables. Una de ellas representa la contraseña 
de un usuario y la otra un texto introducido. El programa debe poder mostrar por pantalla 
si las dos cadenas de texto son iguales sin tener en cuenta mayúsculas y minúsculas.
"""
#We ask to enter the password and a string via keyboard.
#We pass the method .lower() to make both strings lowercase. We could also do .upper()
password = input("Enter the password: ")
string = input("Enter a string: ")
if password.lower() == string.lower():
  print('Password and string match.')
else:
  print("Password and string don't match.")