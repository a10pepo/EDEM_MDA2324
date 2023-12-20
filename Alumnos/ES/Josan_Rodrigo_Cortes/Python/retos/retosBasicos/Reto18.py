""" Reto 18
Crea una función que sea capaz de eliminar un caracter concreto de una cadena de texto. 
La función debe tener la siguiente firma:

def eliminar(str, n):
    # TODO: Esto debes completarlo
    # Pista, haz uso de [start:end:step]

# De modo que:
print(eliminar('Madrid', 0)) #adrid
print(eliminar('Madrid', 3)) #Madid
print(eliminar('Madrid', 5)) #Madri """

def eliminar(palabra,caracter):
    nuevoCarcter=palabra.replace(caracter," ") 
    return nuevoCarcter 

print(eliminar("Josan","J"))
print(eliminar("Josan","o"))
print(eliminar("Josan","s"))
print(eliminar("Josan","a"))
print(eliminar("Josan","n"))
