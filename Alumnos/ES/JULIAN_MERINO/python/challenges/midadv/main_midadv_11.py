"""
Reto 11

Una empresa quiere gestionar su cartera de clientes. Escribe un programa que guarde los clientes en un 
diccionario u objeto literal en el que disponga de:

NIF (string), nombre (string), apellidos (string), teléfono (string), email (string) y preferente (boolean)

El programa debe mostrar las siguientes opciones para que escoja el usuario:

(1) Añadir un cliente

(2) Eliminar cliente por NIF

(3) Mostrar Cliente por NIF

(4) Listar TODOS os clientes

(5) Mostrar ÚNICAMENTE los clientes preferentes

(6) Finalizar Programa
"""

from customers import Customer

#Let's define the different options of the program:
def add_cust():
    nif = input(f"Enter the customer's NIF: ")
    name = input(f"Enter the customer's name: ")
    surname = input(f"Enter the customer's surname: ")
    phone = input(f"Enter the customer's phone number: ")
    email = input(f"Enter the customer's email: ")
    preferent = eval(input(f"Enter whether the new customer is preferent (True) or not (False): "))
    new_cust = Customer(nif, name, surname, phone, email, preferent)
    print('New customer added.')
    return new_cust

def del_cust(nif: str, list):
    for i in range(len(list)):
        if customer_book[i].nif == nif:
            print(f'Customer {customer_book[i].name} {customer_book[i].surname} with NIF: {customer_book[i].nif} removed.')
            del customer_book[i]
        else:
            print(f'Customer {nif} not found.')

def search_cust(nif: str, list):
    found = False
    for i in range(len(list)):
        if customer_book[i].nif == nif:
            print(f'''
NIF: {customer_book[i].nif} 
Name: {customer_book[i].name} 
Surname: {customer_book[i].surname} 
Phone: {customer_book[i].phone}
e-mail: {customer_book[i].email}
Preferent: {customer_book[i].preferent}
            ''')
            found = True       
    if found == False:
        print("No matches found.")

def list_all(list, a: bool):
    if a:
        for i in range(len(list)):
            print(f'''
NIF: {customer_book[i].nif} 
Name: {customer_book[i].name} 
Surname: {customer_book[i].surname} 
Phone: {customer_book[i].phone}
e-mail: {customer_book[i].email}
Preferent: {customer_book[i].preferent}
                ''')
    elif not a:
        for i in range(len(list)):
            if list[i].preferent == True:
                print(f'''
NIF: {customer_book[i].nif} 
Name: {customer_book[i].name} 
Surname: {customer_book[i].surname} 
Phone: {customer_book[i].phone}
e-mail: {customer_book[i].email}
Preferent: {customer_book[i].preferent}
                ''')

customer_book = []

def customers_database(list):
    choice = str
    while choice != '6':
        print('''
          Welcome to Customers Management Program. Pick a choice:
          1. Add a customer
          2. Remove a customer
          3. Search a customer
          4. List ALL customers
          5. List Preferent customers ONLY
          6. Quit
          ''')
        choice = input('Option: ')
        if choice == '1':
            list.append(add_cust())
        elif choice == '2':
            nif = input("Enter the customer's NIF: ")
            del_cust(nif, list)
        elif choice == '3':
            nif = input("Enter the customer's NIF: ")
            search_cust(nif, list)
        elif choice == '4':
            list_all(list, a = True)
        elif choice == '5':
            list_all(list, a = False)
        elif choice == '6':
            print('Goodbye.')
            break
    return list

customers_database(customer_book)
