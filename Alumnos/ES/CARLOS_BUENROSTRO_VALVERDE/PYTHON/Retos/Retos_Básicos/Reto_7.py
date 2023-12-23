# # Reto 7: Escribe un programa que tenga dos variables. Una de ellas representa la contraseña de 
# # un usuario y la otra un texto introducido. El programa debe poder mostrar por
# # pantalla si las dos cadenas de texto son iguales sin tener en cuenta mayus o minus.

user_password = "contraseña"
texto = input("Para cambiar su contraseña, introduzca la antigua: ")

if user_password == texto.lower():
  print("Las contraseñas son iguales.")
else:
  print("Las contraseñas no son iguales.")