"""
Reto 1

Una tienda vende Discos de música (unos muñecos muy graciosos). Con la idea de vender un stock almacenado 
durante meses, se decide que discos de género "Black Metal" y "Electro" tienen un descuento del 30%.

Cada disco (usa un diccionario para esto) tendrá:

Nombre
Artista
Año
Precio
Género (solo pueden ser de los siguientes):
    Pop
    Electro
    Reggaeton
    Rock
    Metal
    Death Metal
    Black Metal

Escribe un programa que, disponiendo de una lista de discos disponibles en la tienda el usuario pueda 
elegir el disco a comprar.

Al acabar la compra (pulsando la tecla 0) se deberá mostrar el ticket de compra indicando la fecha de compra 
(puedes coger la fecha actual a través de datetime), el dinero que se ahorra el usuario y el coste final 
de la compra.
"""
from datetime import datetime

#We initialise variables discs as dict() and pass key: values
disc01 = dict()
disc01["title"] = "El Viaje de Copperpot"
disc01["artist"] = "La Oreja de Van Gogh"
disc01["year"] = 2000
disc01["cost"] = 15.95
disc01["genre"] = "Pop"
#print(disc01)

disc02 = dict()
disc02["title"] = "Slipknot"
disc02["artist"] = "Slipknot"
disc02["year"] = "1999"
disc02["cost"] = 21.50
disc02["genre"] = "Black Metal"
#print(disc02)

disc03 = dict()
disc03["title"] = "Idealism"
disc03["artist"] = "Digitalism"
disc03["year"] = 2007
disc03["cost"] = 19.95
disc03["genre"] = "Electro"
#print(disc03)

disc04 = dict()
disc04["title"] = "La Noche"
disc04["artist"] = "Arde Bogotá"
disc04["year"] = 2021
disc04["cost"] = 9.95
disc04["genre"] = "Rock"
#print(disc04)

#We declare disc_list and enter values:
disc_list = []
disc_list.append(disc01)
disc_list.append(disc02)
disc_list.append(disc03)
disc_list.append(disc04)
#print(disc_list)

def disc_purchase(disc_list):
    a = True
    while a == True:
        print(f'Hello. Choose the disc you want to buy: \n')
        for i in range(len(disc_list)):
            print(f'{i + 1}: {disc_list[i]["title"]}')
        print('Press X to exit:')
        choice = input()
        if choice.lower() == 'x':
            a = False
            return print('Goodbye!')
        elif int(choice) == 1:
            print(f' Title: {disc_list[0]["title"]}')
            print(f' Artist: {disc_list[0]["artist"]}')
            print(f' Year: {disc_list[0]["year"]}')
            print(f' Price: {disc_list[0]["cost"]}€')
            print(f' Genre: {disc_list[0]["genre"]}')
            buy = input(f'Press 0 to buy or any key to return: ')
            if buy == '0':
                if disc_list[0]["genre"] == "Electro" or disc_list[0]["genre"] == "Black Metal":
                    print(f'Price: {disc_list[0]["cost"]}€')
                    print(f' 30% discount: {0.3 * disc_list[0]["cost"]}€')
                    print(f'Total: {disc_list[0]["cost"] - (0.3 * disc_list[0]["cost"])}€')
                    print(f' Date: {datetime.now()}')
                    print('Thank you!')
                    a = False
                else:
                    print(f'Total: {disc_list[0]["cost"]}€')
                    print(f' Date: {datetime.now()}')
                    print('Thank you!')
                    a = False
                    break

        elif int(choice) == 2:
            print(f' Title: {disc_list[1]["title"]}')
            print(f' Artist: {disc_list[1]["artist"]}')
            print(f' Year: {disc_list[1]["year"]}')
            print(f' Price: {disc_list[1]["cost"]}€')
            print(f' Genre: {disc_list[1]["genre"]}')
            buy = input(f'Press 0 to buy or any key to return: ')
            if buy == '0':
                if disc_list[1]["genre"] == "Electro" or disc_list[1]["genre"] == "Black Metal":
                    print(f'Price: {disc_list[1]["cost"]}€')
                    print(f' 30% discount: {0.3 * disc_list[1]["cost"]}€')
                    print(f'Total: {disc_list[1]["cost"] - (0.3 * disc_list[1]["cost"])}€')
                    print(f' Date: {datetime.now()}')
                    print('Thank you!')
                    a = False
                else:
                    print(f'Total: {disc_list[1]["cost"]}€')
                    print(f' Date: {datetime.now()}')
                    print('Thank you!')
                    a = False
                    break

        elif int(choice) == 3:
            print(f' Title: {disc_list[2]["title"]}')
            print(f' Artist: {disc_list[2]["artist"]}')
            print(f' Year: {disc_list[2]["year"]}')
            print(f' Price: {disc_list[2]["cost"]}€')
            print(f' Genre: {disc_list[2]["genre"]}')
            buy = input(f'Press 0 to buy or any key to return: ')
            if buy == '0':
                if disc_list[2]["genre"] == "Electro" or disc_list[2]["genre"] == "Black Metal":
                    print(f'Price: {disc_list[2]["cost"]}€')
                    print(f' 30% discount: {0.3 * disc_list[2]["cost"]}€')
                    print(f'Total: {disc_list[2]["cost"] - (0.3 * disc_list[2]["cost"])}€')
                    print(f' Date: {datetime.now()}')
                    print('Thank you!')
                    a = False
                else:
                    print(f'Total: {disc_list[2]["cost"]}€')
                    print(f' Date: {datetime.now()}')
                    print('Thank you!')
                    a = False
                    break

        elif int(choice) == 4:
            print(f' Title: {disc_list[3]["title"]}')
            print(f' Artist: {disc_list[3]["artist"]}')
            print(f' Year: {disc_list[3]["year"]}')
            print(f' Price: {disc_list[3]["cost"]}€')
            print(f' Genre: {disc_list[3]["genre"]}')
            buy = input(f'Press 0 to buy or any key to return: ')
            if buy == '0':
                if disc_list[3]["genre"] == "Electro" or disc_list[3]["genre"] == "Black Metal":
                    print(f'Price: {disc_list[3]["cost"]}€')
                    print(f' 30% discount: {0.3 * disc_list[3]["cost"]}€')
                    print(f'Total: {disc_list[3]["cost"] - (0.3 * disc_list[3]["cost"])}€')
                    print(f' Date: {datetime.now()}')
                    print('Thank you!')
                    a = False
                else:
                    print(f'Total: {disc_list[3]["cost"]}€')
                    print(f' Date: {datetime.now()}')
                    print('Thank you!')
                    a = False
                    break

disc_purchase(disc_list)