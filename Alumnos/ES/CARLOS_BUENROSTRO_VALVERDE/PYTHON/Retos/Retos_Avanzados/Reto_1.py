# Reto 1: Tienda de discos musicales.
from datetime import datetime

discos = [
    {
        "Nombre" : "21st Century Breakdown",
        "Artista" : "Green Day",
        "Año" : "2009",
        "Precio" : 19.99,
        "Género" : "Rock"

    },
    {
        "Nombre" : "Sin Noticias de Holanda",
        "Artista" : "Melendi",
        "Año" : 2003,
        "Precio" : 17.99,
        "Género" : "Pop"
    }
    ,
    {
        "Nombre" : "Summoning",
        "Artista" : "Stronghold",
        "Año" : 1999,
        "Precio" : 18.99,
        "Género" : "Black Metal"
    },
    {
        "Nombre" : "Grey With Breaks",
        "Artista" : "Lowfish",
        "Año" : 2003,
        "Precio" : 12.99,
        "Género" : "Electro"
    }]

def calculo_descuento(precio, descuento):
    genero = discos['genero']
    if genero == "Black Metal" or genero == "Electro":
        return precio * 0.3
    else:
        return 0

print("Discos disponibles:")
for idx, disco in enumerate(discos, start=1):
    print(f"{idx}. {disco['Nombre']} - {disco['Artista']} - Género: {disco['Género']} - Precio: ${disco['Precio']}")

ticket = []
ahorro = 0

while True:
    seleccion = input("Bienvenido al programa. Elija un disco para comprar o pulse 0 para salir.")
    if seleccion == 0:
        break
    try:
        seleccion = int(seleccion)
        if 1 <= seleccion <= len(discos):
            disco_elegido = discos[seleccion -1]
            ticket.append(disco_elegido)
            descuento = calculo_descuento(disco_elegido['Precio']), disco_elegido['Género']
            ahorro =+ descuento
            print(f'Has seleccionado {disco_elegido["Nombre"]} a tu compra')
        else:
            print('Pulsa un botón correcto.')
    except ValueError:
        print('Selecciona un número válido.')

total_ticket = sum(discos['Precio'] for disco in ticket) - ahorro
fecha_compra = datetime.now()

print('--- Ticket de compra ---')
print(f'Fecha de la compra: {fecha_compra}')
print(f'Descuento total de la compra: {descuento}')
print(f'El total de la compra ha sido: {total_ticket}')