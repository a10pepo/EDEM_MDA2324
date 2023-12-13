#CREACIÓN DE CLASE:
class cliente:
    def __init__(self,NIF,Nombre,Apellidos,Telefono,Email,Preferente):
        self.NIF:str = NIF
        self.Nombre:str = Nombre
        self.Apellidos:str = Apellidos
        self.Telefono:str = Telefono
        self.Email:str = Email
        self.Preferente:bool = Preferente     

#CREACIÓN DE LISTAS:
Customer_list = [
    cliente("123456789c", "Juan", "Pérez", "555-123-456", "juan@example.com", True),
    cliente("987654321c", "Ana", "López", "555-789-123", "ana@example.com", False),
    cliente("555555555c", "Carlos", "García", "555-555-555", "carlos@example.com", True),]
VIP_Customer_list = []

#DEFINICIÓN DE FUNCIONES

def new_customer ():
    print("\n ALTA NUEVO CLIENTE \n")
    NIF = input ("NIF (Sin espacios): ").lower().strip()
    Nombre = input ("Nombre: ").strip()
    Apellidos = input ("Apellidos: ").strip()
    Telefono = input ("Telefono: ").strip()
    Email = input ("Email: ").strip().lower()
    Preferente = None
    while Preferente is None:
        Preferente_input:bool = input ("¿Usuario preferente? (S/N): ")
        if Preferente_input =="S":
            Preferente = True
        elif Preferente_input == "N":
            Preferente = False
        else :
            print ("Por favor, (S/N)")
    nuevo_cliente = cliente (NIF,Nombre,Apellidos,Telefono,Email,Preferente)
    Customer_list.append(nuevo_cliente)
    print("\nALTA COMPLETADA\n")


def show_all_customers ():
    if not Customer_list:
          print ("\nNO SE HAN REGISTRADO CLIENTES TODAVÍA")
    else:
            for cliente in Customer_list:
                print()
                print("NIF:", cliente.NIF)
                print("Nombre:", cliente.Nombre)
                print("Apellidos:", cliente.Apellidos)
                print("Teléfono:", cliente.Telefono)
                print("Email:", cliente.Email)
                print("Preferente:", "Sí" if cliente.Preferente else "No")


def delete_customer_NIF ():
    NIF_para_borrar = input("\n Por favor introduce el NIF para buscar y borrar registro: ").lower().strip()
    cliente_NIF = None
    for cliente in Customer_list:
        if cliente.NIF == NIF_para_borrar:
            cliente_NIF = cliente
            break
    if cliente_NIF:
        Customer_list.remove(cliente_NIF)
        print(f'\n EL CLIENTE CON NIF:{cliente_NIF.NIF} HA SIDO DADO DE BAJA')
    else:
        print(f'\n NO SE HA ENCONTRADO EL NIF')


def show_customer_NIF ():
    NIF_para_mostrar = input("\n Por favor introduce el NIF para buscar y mostrar: ").lower().strip()
    cliente_NIF = None
    for cliente in Customer_list:
        if cliente.NIF == NIF_para_mostrar:
            cliente_NIF = cliente
            break
    if cliente_NIF:
            print()
            print("NIF:", cliente.NIF)
            print("Nombre:", cliente.Nombre)
            print("Apellidos:", cliente.Apellidos)
            print("Teléfono:", cliente.Telefono)
            print("Email:", cliente.Email)
            print("Preferente:", "Sí" if cliente.Preferente else "No")
    else:
        print(f'\n NO SE HA ENCONTRADO EL NIF')


def show_customer_VIP ():
    if not Customer_list:
          print ("\nNO SE HAN REGISTRADO CLIENTES TODAVÍA")
    else:
        for cliente in Customer_list:
             if cliente.Preferente == True:
                  VIP_Customer_list.append(cliente)
        for cliente in VIP_Customer_list:
                print()
                print("NIF:", cliente.NIF)
                print("Nombre:", cliente.Nombre)
                print("Apellidos:", cliente.Apellidos)
                print("Teléfono:", cliente.Telefono)
                print("Email:", cliente.Email)
                print("Preferente:", "Sí" if cliente.Preferente else "No")