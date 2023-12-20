# RETO 1

from datetime import datetime

discos = [
    {
        "Nombre": "Disco1",
        "Artista": "Artista1",
        "Año": 2022,
        "Precio": 20,
        "Género": "Electro"
    },
    {
        "Nombre": "Disco2",
        "Artista": "Artista2",
        "Año": 2020,
        "Precio": 25,
        "Género": "Black Metal"
    },
    {
        "Nombre": "Disco3",
        "Artista": "Artista3",
        "Año": 2021,
        "Precio": 18,
        "Género": "Pop"
    }
    
]

def calcular_descuento(precio, genero):
    if genero == "Black Metal" or genero == "Electro":
        return 0.3 * precio
    else:
        return 0

print("Discos disponibles:")
for idx, disco in enumerate(discos, start=1):
    print(f"{idx}. {disco['Nombre']} - {disco['Artista']} - Género: {disco['Género']} - Precio: ${disco['Precio']}")

compra = []
ahorro_total = 0

while True:
    opcion = input("Elige un disco para comprar (o introduce 0 para salir): ")
    if opcion == '0':
        break
    try:
        opcion = int(opcion)
        if 1 <= opcion <= len(discos):
            disco_elegido = discos[opcion - 1]
            compra.append(disco_elegido)
            descuento = calcular_descuento(disco_elegido['Precio'], disco_elegido['Género'])
            ahorro_total += descuento
            print(f"Has agregado '{disco_elegido['Nombre']}' a tu compra.")
        else:
            print("Por favor, introduce un número válido.")
    except ValueError:
        print("Por favor, introduce un número.")

coste_total = sum(disco['Precio'] for disco in compra) - ahorro_total
fecha_compra = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("\n--- Ticket de compra ---")
print(f"Fecha de compra: {fecha_compra}")
print(f"Dinero ahorrado: ${ahorro_total:.2f}")
print(f"Coste final de la compra: ${coste_total:.2f}")
