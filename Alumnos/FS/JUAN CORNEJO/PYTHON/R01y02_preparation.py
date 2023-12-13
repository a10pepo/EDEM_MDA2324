#CLASS CREATION:
class disc:
    def __init__(self,Name,Reference,Artist,Year,Price,Type):
        self.Name:str = Name
        self.Reference:str = Reference
        self.Artist:str = Artist
        self.Year:int = Year
        self.Price:float = Price
        self.Type:str = Type   

#LISTS CREATION:
Type_list = ["Pop", "Electro","Reggaeton","Rock","Metal","Death Metal","Black Metal"]
Customer_trolley = []
Discs_available = [
    disc("Thriller","001", "Michael Jackson", 1982, 15.99, "Pop"),
    disc("Random Access Memories","002", "Daft Punk", 2013, 12.99, "Electro"),
    disc("Vibras","003", "J Balvin", 2018, 10.99, "Reggaeton"),
    disc("Master of Puppets","004", "Metallica", 1986, 14.99, "Metal"),
    disc("Dark Side of the Moon", "005", "Pink Floyd", 1973, 18.99, "Rock"),
    disc("Abbey Road", "006", "The Beatles", 1969, 16.99, "Rock"),
    disc("Thriller", "007", "Michael Jackson", 1982, 15.99, "Pop"),
    disc("Back in Black", "008", "AC/DC", 1980, 13.99, "Rock"),
    disc("Master of Puppets", "009", "Metallica", 1986, 14.99, "Metal"),
    disc("Random Access Memories", "010", "Daft Punk", 2013, 12.99, "Electro"),
    disc("Vibras", "011", "J Balvin", 2018, 10.99, "Reggaeton"),
    disc("The Wall", "012", "Pink Floyd", 1979, 17.99, "Rock"),
    disc("In Utero", "013", "Nirvana", 1993, 12.99, "Rock"),
    disc("Born to Die", "014", "Lana Del Rey", 2012, 11.99, "Pop"),
    disc("Paranoid", "015", "Black Sabbath", 1970, 13.99, "Metal"),
    disc("Rumors", "016", "Fleetwood Mac", 1977, 14.99, "Rock"),
    disc("Random Album Title", "017", "Deadmau5", 2008, 12.49, "Electro"),
    disc("Soy Peor", "018", "Bad Bunny", 2017, 9.99, "Reggaeton"),
    disc("Homogenic", "019", "Björk", 1997, 13.49, "Electro"),
    disc("Malibu", "020", "Anderson .Paak", 2016, 11.99, "Pop"),
    disc("Blackwater Park", "021", "Opeth", 2001, 15.99, "Metal"),
    disc("Electric Ladyland", "022", "Jimi Hendrix", 1968, 16.99, "Rock"),
    disc("En Vivo Desde la Habana", "023", "Silvio Rodríguez", 2013, 9.99, "Reggaeton"),
    disc("Abbath", "024", "Abbath", 2016, 14.49, "Black Metal"),]

#FUNCTIONS DEFINITION

def show_discs_stock ():
    while True:
        if not Discs_available:
            print ("\nTHERE ARE NO DISCS AVAILABLE FOR PURCHASE")
        else:
            print("\nDISCOS DISPONIBLES:")
            print("-" * 85)
            print("{:<7} {:<30} {:<20} {:<7} {:<7} {:<7}".format("Ref.","Disco", "Artista", "Precio", "Año","Tipo"))
            print("-" * 85)

        for disc in Discs_available:
            print("{:<7} {:<30} {:<20} {:<7.2f} {:<7} {:<7}".format(disc.Reference, disc.Name, disc.Artist, disc.Price, disc.Year, disc.Type))
        
        purchase_page = input("\n ¿Qué deseas hacer?\n\n" "1 - Comprar discos \n\n""2 - Salir de la tienda" "\n\n Indique aquí su opción: ")
        if purchase_page == "2":
            print("Muchas gracias, esperamos verle pronto")
            break
        elif purchase_page == "1":
            adding_reference()
            break
        else:
            print ("Por favor elige una opción entre 1 y 2")

def adding_reference ():
        print("\nDISCOS DISPONIBLES:")
        print("-" * 85)
        print("{:<7} {:<30} {:<20} {:<7} {:<7} {:<7}".format("Ref.","Disco", "Artista", "Precio", "Año","Tipo"))
        print("-" * 85)
        for disc in Discs_available:
            print("{:<7} {:<30} {:<20} {:<7.2f} {:<7} {:<7}".format(disc.Reference, disc.Name, disc.Artist, disc.Price, disc.Year, disc.Type))   
        print()
        reference_to_add = input ("Por favor, introduzca la referencia que quiere comprar: ")
        found_disc = False
        for disc in Discs_available:
            if disc.Reference == reference_to_add:
                found_disc = True
                Customer_trolley.append(disc)
                print(f'\n El disco "{disc.Name}" de "{disc.Artist}" se ha añadido a su carrito')
        if not found_disc:
                print(f'\n No se ha encontrado la referencial ')
        
        end_shopping()

def print_trolley ():
    print("\n CARRITO DE COMPRA:")
    for disc in Customer_trolley:
        print(f'\n "{disc.Name}" de "{disc.Artist}')
    print(f'\n Actualmente hay un total de {len(Customer_trolley)} disco/s en tu carrito')
    end_shopping()  
        
def end_shopping ():
    while True:
        continue_shopping = input ("\n ¿Qué deseas hacer?\n\n" "1 - Añadir otra referencia\n\n""2 - Ver mi carrito actual \n\n""0 - Pagar" "\n\n Indique aquí su opción: ")
        if continue_shopping  == "1":
            adding_reference()
            break
        if continue_shopping  == "2":
            print_trolley()
            break
        elif continue_shopping == "0":
            amount_to_pay()
            break
        else:
            print("Por favor, introduce una opción entre 1,2 o 0")

def amount_to_pay ():
    
    total_price = 0.0
    discount =0.0
    for disc in Customer_trolley:
        total_price += disc.Price
    for disc in Customer_trolley:
        if disc.Type in ["Black Metal","Electro"]:
            discount += disc.Price*0.3
    
    final_price = round(total_price,2) - round(discount,2)
    
    import datetime
    current_date = datetime.date.today()
    formatted_datetime = current_date.strftime("%d-%m-%Y %H:%M:%S")

    print("\nFACTURA:")
    print(f"Fecha: {formatted_datetime}")
    print("-" * 50)
    print("{:<30} {:<15} {:<10}".format("Nombre", "Artista", "Precio"))
    print("-" * 50)

    for disc in Customer_trolley:
        print("{:<30} {:<15} {:<10.2f}".format(disc.Name, disc.Artist, disc.Price))

    print("-" * 50)

    print(f"Total: ${final_price:.2f}")
    print (f'Descuento aplicado:  $ {round(discount,2)}')