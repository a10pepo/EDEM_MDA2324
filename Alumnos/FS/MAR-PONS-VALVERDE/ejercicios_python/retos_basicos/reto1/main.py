nombre: str= 'Mar'
apellidos: str= 'Pons Valverde'
nombre_completo= nombre + '' + apellidos
print(f'> nombre completo: {nombre_completo}')



lista = [1,2,3,4,5,6,7,8]

while (len(lista) > 3):
    lista.pop ()
    print(lista)

def miFuncionConParametros(a,b):
    print(f'¡{a}, {b}!')

miFuncionConParametros('Hola', 'Mundo')    

# Función con muchos parámetros
def miFuncionConMultiplesParametros(*elementos) :
    for elemento in elementos:
        print(f"Elemento: {elemento}")

# llamando la función y pasándole una lista de parámetros
lista: [int] = [1, 2, 3, 4, 5]
miFuncionConMultiplesParametros(lista)

#1. Desde tu cuenta de replit.com crea un nuevo proyecto. En dicho proyecto, dentro del archivo main.py crea variables que representen los siguientes datos de un contacto:

Nombre = "Mar"
Apellidos = "Pons Valverde"
Edad = 32
Email = "marponsvalverde@gmail.com"
Telefono = "627335222"
Casado = True
Con_Hijos = False
Lista_de_amigos = [ "Arantxa", "Victor", "Raul"]
Peliculas_vistas = {
    "pelicula1": "Pretty Woman",
    "pelicula2": "El diario de Noa",
    "Pelicula3": "El rey Leon"
}
# Mostrar todos los datos por consola.
print("datos del contacto")
print(f"Nombre: {Nombre}")
print(f"Apellidos: {Apellidos}")
print(f"Edad: {Edad} anyos")
print(f"Email: {Email}")
print(f"Telefono: {Telefono}")
print("Casado: " + ("Si" if Casado else "No"))
print("Con_Hijos: " + ("Si" if Con_Hijos else "No"))
print(f"Lista_de_amigos", Lista_de_amigos)
print("Peliculas_vistas:")
for clave, valor in Peliculas_vistas.items():
    print(f"{clave}: {valor}")
