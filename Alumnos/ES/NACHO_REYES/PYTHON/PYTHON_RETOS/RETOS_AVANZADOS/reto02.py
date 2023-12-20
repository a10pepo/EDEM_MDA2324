# RETO 2
carrito = []

def calcular_coste_total(carrito):
    return sum(item['Precio'] for item in carrito)

while True:
    nombre_articulo = input("Introduce el nombre del artículo: ")
    precio_articulo = float(input("Introduce el precio del artículo: "))

    articulo = {
        "Nombre": nombre_articulo,
        "Precio": precio_articulo
    }

    carrito.append(articulo)

    respuesta = input("¿Introducir otro elemento al carrito? (Si / No): ")
    if respuesta.lower() != 'si':
        break

print("\n--- Lista de la compra ---")
for idx, item in enumerate(carrito, start=1):
    print(f"{idx}. {item['Nombre']} - Precio: ${item['Precio']:.2f}")

coste_total = calcular_coste_total(carrito)
print(f"\nCoste total de la compra: ${coste_total:.2f}")
