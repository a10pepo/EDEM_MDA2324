""" El programa debe preguntar el artículo y su precio y añadirlo a una variable (diccionario u objeto
 literal), hasta que el usuario 
decida terminar ("Introducir otro elemento al carrito (Si / No)".

Una vez el usuario decida no introducir más elementos al carrito, 
debe mostrar por pantalla la lista de la compra y el coste total. """

IntroducirOtroElemento="Si"
articulos=[]
while (IntroducirOtroElemento=="Si"):

    nuevoElemento=input("Introduce el nombre del articulo ")
    precioNuevoElemento=int(input("Introduce el precio del articulo "))
    producto={nuevoElemento:precioNuevoElemento}
    articulos.append(producto)
    IntroducirOtroElemento=input("Introducir otro elemento al carrito (Si / No) ")

print(articulos)
