# Obtener chistes de la API de Chuck Norris

import requests

url = 'https://api.chucknorris.io/jokes/random'

# Número de chistes
numero_de_chistes = 100

# Crear el archivo TXT
archivo = open('/Users/User/Documents/GitHub/EDEM_MDA2324/Alumnos/ES/Javier_Ruiz/Chuck/results/chistes.txt', 'w')

# Obtener las bromas
for i in range(numero_de_chistes):

    # Obtener una broma aleatoria
    data = requests.get(url)

    # Obtener el texto de la broma
    joke_text = data.json()['value']

    # Escribir la broma en el archivo TXT
    archivo.write(joke_text + '\n')

# Cerrar el archivo TXT
archivo.close()
