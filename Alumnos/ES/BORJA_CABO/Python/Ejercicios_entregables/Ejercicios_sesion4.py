# EJERCICIOS SESIÓN 4

# Ejercicio 1.1
def primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


def mp(primer_num, ultimo_num):
    for i in range(primer_num,  ultimo_num):
        if primo(i):
            print(i)

primer_num = int(input('Introduce el númerpo donde quieres que empiece el rango: '))
ultimo_num = int(input('Introduce el númerpo donde quieres que termine el rango: '))
mp(primer_num,ultimo_num)

# Ejercicio 1.2
def primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero_ver = int(input('Introduce un número: '))
if primo(numero_ver):
    print('Es primo')
else: 
    print('No es primo')

# Ejercicio 1.3
def año_bis(año):
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                return True
            else:
                return False
        return True
    return True

año_ver = int(input('Introduce un año: '))
if año_bis(año_ver):
    print(True)
else:
    print(False)

# Ejercicio 3
import requests
url = 'https://randomuser.me/api'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
    nombre = data['results'][0]['name']['first']
    apellido = data['results'][0]['name']['last']
    print(f'Su nombre es: {nombre}')
    print(f'Su apellido es: {apellido}')
else:
    print('Ha ocurrido un error al obtener los datos del usuario')