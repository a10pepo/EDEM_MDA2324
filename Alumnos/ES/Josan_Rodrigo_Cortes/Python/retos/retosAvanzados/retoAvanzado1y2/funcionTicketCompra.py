from tienda import listaDiscos
from funcionpedidoCompra import pedidoCompra
import datetime

def ticketCompra():

    print("TICKET DE COMPRA")
    mipedido=pedidoCompra()
    importeTotal=0
    print(f' NOMBRE\t|ARTISTA\t|AÑO\t|GENERO\t|DESCUENTO\t|PRECIO|\t|SUBTOTAL|')
    for discos in mipedido:
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
            discos["Genero"]=(0)
        #Creo los totales y subtotales:
        if descuentoDisco!=0:
          importedisco=precioDisco-(precioDisco*(descuentoDisco/100))
        else:
            importedisco=precioDisco
        

        importeTotal+=importedisco


        print(f' {nombreDisco:<5} {artistaDisco:<5} {anyoDisco:<5} {generoDisco:<5} {descuentoDisco:<5} {precioDisco:<5} {importedisco:<5}')
            
    print(f'ELTOTAL DE SU COMPRA ASCIENDE A ------------------------------{importeTotal}')
    print("Falta la fecha")
    #No me funciona esta instrucción
    # print(datetime.today().strftime("%Y-%m-%d"))

   

   