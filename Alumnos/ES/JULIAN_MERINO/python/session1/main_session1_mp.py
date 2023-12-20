# This is a comment, it's useful to explain what the code does.

# Print Hola mundo in python.
print("Hola mundo")

# Declaring and assigning a value to a variable.
nombre = "Julián"

# Concatenate texts
print("Hola" + " " + nombre)

# Formatting texts
print(f"Hola {nombre}")

# Typping variables - text (str)
apellidos: str = "Merino Pérez"

# Concatenate text and assign a new variable - Full name
nombre_completo = f"{nombre} {apellidos}"
print("Hola " + nombre_completo)

# Declare integer numbers variables (INT)
edad: int = 38
print(f"{nombre_completo} tiene {edad} años")

# Declare float number variable (float)
altura: float = 1.77

# Operations - additions
print(f"{nombre} ha cumplido años y ahora tiene {edad + 1} años")

# Operations - increments
edad_nueva = edad + 1
# We could also do edad +=1

# Operations - Multiply * (updating existing value)
edad = edad * 2
# It could also be edad *= 2
print(f"El doble de la edad es {edad}")

# Operations - Powers ** (exponents)
edad **= 2
print(f"La potencia cuadrada de la edad es {edad} años")

# Operations - divisions /
# Watch out - not recommended using INT for divisions, because the division may not have rest = 0 and decimals may be missed. Better using float.
altura = altura / 2

# Operations - Obtaining the rest of a division %
resto_edad = edad % 2

# Declaring and assigning a CONSTANT: use capital letters
NUMERO_PI = 3.1416

# Assigning and declaring  BOOLEANS: True / False
tiene_hijos = True
casado = False

# Lists with []- A shopping list!

lista_compra = ["Patatas", "Leche", "Filetes"]
# Three elements in the list, type str.
# Each element has a POSITION in the list.
# Positions start from 0.
print(lista_compra[0])
print(lista_compra[1])
print(lista_compra[2])

# Show (print) lista_compra in console: use *
print(*lista_compra)

# To append elements to a list
lista_compra.append("Queso")
print(*lista_compra)

# Ways of checking a list: ranges with brackets - watch out, the range is open, 
# which means that the last element is not included!
print(lista_compra[0:2])

# If the range is not defined after the semicolon, it will show the entire list:
print(lista_compra[0:])

# We can also show elements each x elements: [0: :x]
# Each 2 elements:
print(lista_compra[0: :2])

# Reverse the list
print(lista_compra[::-1])

# If you use .reverse() method, it will change the original list and reverse it:
lista_compra.reverse()
print(lista_compra)

# You can also create a copy of the list:
copy_lista_compra = lista_compra.copy()
print(copy_lista_compra)

#This is not copying a list, but creating a new variable that points to another:
copy2_lista_compra = lista_compra
lista_compra.append("Vino")
print(copy2_lista_compra)

# Deleting the last position of the list: .pop()
lista_compra.pop()
print(lista_compra)
# Delete the x position of the list: .pop(x)
lista_compra.pop(0) # to delete the 1st position
print(lista_compra)

# It's also useful to remove by value:
lista_compra.remove("Filetes")
print(lista_compra)
# If there's more than one entry with the same value, will remove only the first one.

# To remove all the elements: .clear()
lista_compra.clear()
print(lista_compra)

# Insert an element in a list: .insert(position, "value")
lista_compra = ['Agua', 'Coca-Cola', 'Cerveza']
lista_compra.insert(2, 'Sprite')
print(lista_compra)

# To update an entry in a list: 
lista_compra[2] = 'Fanta'
print(lista_compra)

# Copy a list, but modifying Fanta with Sprite
lista_compra2 = lista_compra.copy()
lista_compra2[2] = 'Sprite'
print(lista_compra2)

# Dictionary structures:
# Dictionaries are collections of key-value pairs.
# Each key is unique, and each value can be any type.
# Keys are separated by colons :
# Values are separated by commas ,
# Each key-value pair is separated by commas ,