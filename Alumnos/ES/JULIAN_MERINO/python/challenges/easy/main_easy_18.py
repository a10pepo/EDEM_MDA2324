"""
Reto 18

Crea una función que sea capaz de eliminar un caracter concreto de una cadena de texto. 
La función debe tener la siguiente firma:

def eliminar(str, n):
    # TODO: Esto debes completarlo
    # Pista, haz uso de [start:end:step]

# De modo que:
print(eliminar('Madrid', 0)) #adrid
print(eliminar('Madrid', 3)) #Madid
print(eliminar('Madrid', 5)) #Madri
"""

def delete(str, n):
    return str[:n] + str[n + 1:]

print(delete('La Almunia de Doña Godina', 0))
print(delete('La Almunia de Doña Godina', 14))
print(delete('La Almunia de Doña Godina', 99))