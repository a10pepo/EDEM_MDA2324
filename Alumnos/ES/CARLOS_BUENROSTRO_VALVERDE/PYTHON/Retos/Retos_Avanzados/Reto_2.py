# Reto 2: El programa debe preguntar el artículo y su precio y añadirlo a una variable (diccionario u objeto literal), hasta que el usuario decida terminar ("Introducir otro elemento al carrito (Si / No)".
# Una vez el usuario decida no introducir más elementos al carrito, debe mostrar por pantalla la lista de la compra y el coste total.
carrito = []

def calculo_coste_total():
    return sum(item['Precio'] for item in carrito)

while True:
    nombre = input("Introduzca el nombre del artículo: ")
    precio = float(input("Introduzca el precio del artículo: "))

    articulo = {
        "Nombre" : nombre,
        "Precio" : precio
    }

    carrito.append(articulo)

    respuesta = input("¿Desea introducir algún otro artículo? Sí/No: ")
    if respuesta == "si":
        print("Producto añadido correctamente")
    else:
        break
print("*************** TICKET DE LA COMPRA ***************")
for id, item in enumerate(carrito, start = 1):
            print(f"{id}.{item['Nombre']} | Precio: {item['Precio']}")

coste_total = calculo_coste_total
print('***************************************************')
print(f'El precio total de la cesta es: {calculo_coste_total()}')