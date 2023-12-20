"""RETO1
Desde tu cuenta de replit.com crea un nuevo proyecto. En dicho proyecto, 
dentro del archivo main.py crea variables que representen los siguientes datos 
de un contacto:
Una vez hayas creado todas las variables, muéstralas por consola haciendo uso 
de la función print().
"""

name = 'Julián'
surnames = 'Merino Pérez'
age = 38
email = 'jmerino@edem.es'
phone = '+34 677 400 882'
married = False #If married, then True.
children = False #If have children, then True.
friends = [
    'Juan', 'Ana', 'Jose', 'María', 'Pedro', 'Manuel', 'Lucía', 'Marta', 'Sofía']
movies = {1: 'The Matrix', 2: 'Big Fish', 3: 'Star Wars', 4: 'Skyfall'}
print(f'Name: {name}\nSurnames: {surnames}\nAge: {age}\nEmail: {email}\nPhone: {phone}\nMarried: {married}\nChildren: {children}')
i = 0
for i in range(len(friends)):
  print(friends[i])