from tienda import listaDiscos


# 1 Función Imprimir Articulos de la tienda

def listarDiscosTienda():

    print("ESTAS SON LAS EXISTENCIAS DE NUESTRA TIENDA: ")

    print(f' NOMBRE\t|ARTISTA\t|AÑO\t|GENERO|DESCUENTO|PRECIO|')
    for discos in listaDiscos:
        #Creo las variables para acceder al valor de cada una de ellas en el bucle
        nombreDisco=discos["Nombre"]
        artistaDisco=discos["Artista"]
        anyoDisco=discos["Año"]
        precioDisco=discos["Precio"]
        generoDisco=discos["Genero"]
        descuentoDisco=discos.setdefault("Descuento",0)
        #Creo el if para darle el que corresponde a la clave Descuento
        if generoDisco=="Black Metal":
            descuentoDisco=(30)
        elif generoDisco=="Electro":
            descuentoDisco=(30)
        else:
            descuentoDisco=(0)
        print(f' {nombreDisco:<10} {artistaDisco:<10} {anyoDisco:<10} {generoDisco:<10} {descuentoDisco:<10} {precioDisco:<10}')
    print("QUE DESAR COMPRAR??????????????????????")

   