# # Reto 5: Programa por consola que pida contraseña. Es admin. 

password = "admin"

print("Introduzca contraseña por favor: ")

while input() != password:
    print("ERROR. Introduzca la contraseña correcta por favor.")
else:
  print("Bienvenido al programa señor ADMIN")