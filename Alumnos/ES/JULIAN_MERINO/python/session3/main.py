# Conditionals

# IF - ELIF (ELIF is optional) - ELSE (ELSE is optional)

#age = 18

#if (age < 18):
 # print("Menor de edad")

#elif (age >= 18 and age < 70):
  #print("Adulto")
#else:
  #print("Persona mayor")

# LOOPS

#shopping_list = [
  #{
    #"product": "Milk",
    #"price": 2.00,
    #"discount": 6,
    #"units": 0
  #}, 
  #{
    #"product": "Potatoes",
    #"price": 5.00,
    #"discount": 10,
    #"units": 0
  #}, 
  #{
    #"product": "Lettuce",
    #"price": 4.00,
    #"discount": 1,
    #"units": 50
  #}
#]

# FOR loop to ITERATE through the list
# and sum up the prices of each element and calculate
# the total
#print('''***************** Shopping ticket *******************''')
#print(f'{"Product":<10}| {"Price (€)":<10}| {"Units":<10}| {"Discount (€)":<10}|{"Total (€)":<10}')
#total_price = 0
#for element in shopping_list:
  #product = element["product"]
  #unit_price = element["price"]
  #units = element["units"]
  #discount = element["discount"]
  #if discount != 0:
    #element_total_price = units * unit_price * ( 1 -(discount / 100))
    #total_price += element_total_price
  #else:
    #element_total_price = units * unit_price
  #print(f'{product:<15}{unit_price:<12}{units:<10}{element_total_price * (discount / 100):<10}{element_total_price:.2f}')

#print(f'______________________________________________________\nTotal: {total_price:.2f}')


# ==============WHILE LOOPS============
opcion_escogida = ' '
shopping_list = []
while(opcion_escogida != 'X'):
  opcion_escogida = input('''
  Hello, choose one of the following options:
  1. Enter item
  2. Print ticket
  X. Quit program
  ''')
  
  new_product = {}
  if (opcion_escogida != 'X' and
      opcion_escogida != 'x' and
      opcion_escogida != '1' and
      opcion_escogida != '2'
     ):
    print('Wrong option. Retry')
  elif opcion_escogida == 'X' or opcion_escogida == 'x':
    print('Exited')
    break
  else:
    if int(opcion_escogida) == 1:
      new_product["product_name"] = input("Enter the product's name: ")
      #print(new_product)
      new_product["price"] = float(input("Enter the product's price: "))
      #print(new_product)
      new_product["units"] = int(input("Enter how many units: "))
      #print(new_product)
      disc_loop = True
      while disc_loop == True:
        discounted = input("Is it discounted (y/n)? ")
        if discounted == 'y' or discounted == 'Y':
          new_product["discount"] = float(input("Enter the discount (%): "))
          shopping_list.append(new_product)
          #print(shopping_list)
          disc_loop = False
        elif discounted == 'n' or discounted == 'N':
          new_product["discount"] = 0.0
          shopping_list.append(new_product)
          #print(shopping_list)
          disc_loop = False
        else:
          print("Wrong option. Retry")
    elif int(opcion_escogida) == 2:
      #print(shopping_list)
      print('''***************** Shopping ticket *******************''')
      print(f'{"Product":<10}| {"Price (€)":<10}| {"Units":<10}| {"Discount (€)":<15}| {"Total (€)":<10}')
      total_price = 0
      for element in shopping_list:
        product = element["product_name"]
        unit_price = element["price"]
        units = element["units"]
        discount = element["discount"]
        if discount != 0:
          element_total_price = units * unit_price * ( 1 -(discount / 100))
          total_price += element_total_price
        else:
          element_total_price = units * unit_price
          total_price += element_total_price
        print(f'{product:<15}{unit_price:<12}{units:<15}{round(units * unit_price * (discount / 100), 2):<12}{round(element_total_price, 3):<10}')
      print(f'______________________________________________________\nTotal: {total_price:.2f}') 
