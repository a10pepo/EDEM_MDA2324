""" Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso**.** """

#Sería una forma de hacerlo pero no es la correcta.
""" for i in range (1,101):
    print(101-i) """
# Para el caso de contar hacia atrás, el indice mayor tiene que ser el primero
for i in range(100,0,-1): 
    print(i)

