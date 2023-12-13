#REQUERIMENTS:
from R01y02_preparation import show_discs_stock
from R01y02_preparation import Discs_available
from R01y02_preparation import Customer_trolley

#CÓDIGO MOSTRAR OPCIONES EN TEMRINAL
print ("Muchas gracias por venir a nuestra tienda ")
while True:
    main_page=input("\n ¿Qué deseas hacer?\n\n" "1 - Ver discos en stock\n\n""2 - Salir de la tienda" "\n\n Indique aquí su opción: ")
    if main_page == "2":
        print("\n\n" "Muchas gracias, esperamos verle pronto :-)\n")
        break
    elif main_page == "1":
        show_discs_stock()
        break
    else:
        print ("")
        print ("Por favor elige una opción de las mostradas")