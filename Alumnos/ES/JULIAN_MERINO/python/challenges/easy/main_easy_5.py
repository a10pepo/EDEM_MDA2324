"""
RETO 5

Escribe un programa que sea capaz de pedirle a un usuario por consola** que introduzca 
una contraseña y mientras que ésta no sea "admin", el programa seguirá pidiéndola
Si la contraseña es errónea, deberá sacarle un mensaje de error y volver a pedirle la 
contraseña hasta que la introduzca bien. Si el usuario introduce "admin" correctamente, 
el programa le deberá mostrar un mensaje "Bienvenido al programa señor ADMIN" y luego 
terminar.
NOTA: Para pedir por pantalla y guardarlo en una variable llamada password debes hacer 
uso de password:str = input('Introduce una contraseña')
"""


password:str = input('Enter password: ')
# Use a while loop. Couldn't use a do while because in case of wrong answer, 
# it would just prompt the same message over and over. Would work but wouldn't
# be as nice.
while password != 'admin':
  password:str = input ('Wrong password. Enter again: ')

print('Welcome to the program, ADMIN.')