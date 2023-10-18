#REQUERIMENTS:
from R11_preparation import new_customer
from R11_preparation import show_all_customers
from R11_preparation import delete_customer_NIF
from R11_preparation import show_customer_NIF
from R11_preparation import show_customer_VIP
from R11_preparation import Customer_list
from R11_preparation import VIP_Customer_list

#CÓDIGO MOSTRAR OPCIONES EN TEMRINAL
while True:
  opcion_cliente=input("\n ¿Qué deseas hacer?""\n\n" "1 - Añadir un cliente""\n\n""2 - Eliminar cliente por NIF""\n\n" "3 - Mostrar Cliente por NIF""\n\n" "4 - Listar TODOS os clientes""\n\n" "5 - Mostrar ÚNICAMENTE los clientes preferentes""\n\n" "6 - Finalizar programa""\n\n" "Escribe aquí tu opción :")
  if opcion_cliente == "6":
      print("\n\n" "Muchas gracias, esperamos verle pronto :-)\n")
      break
  elif opcion_cliente == "1":
      new_customer()
  elif opcion_cliente == "2":
      delete_customer_NIF()
  elif opcion_cliente == "3":
      show_customer_NIF()
  elif opcion_cliente == "4":
      show_all_customers()
  elif opcion_cliente == "5":
      show_customer_VIP()