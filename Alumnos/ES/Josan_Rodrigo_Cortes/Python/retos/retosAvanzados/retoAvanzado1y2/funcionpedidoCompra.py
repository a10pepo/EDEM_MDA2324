from tienda import listaDiscos
from funcionlistarDiscosTienda import listarDiscosTienda


def pedidoCompra():
    nuevoPedido=[]
    listarDiscosTienda()
    quiereSeguirComprando="si"
    while quiereSeguirComprando== "si":
        nombreDiscoElegido=input("Introduce el disco elegido: ")
        
        for disco in listaDiscos:
            if nombreDiscoElegido==disco["Nombre"]:
                nuevoPedido.append(disco)
                #listaDiscos.remove(disco)
        quiereSeguirComprando=input("Quiere seguir comprando (si/no): ")
    nuevoPedido.copy()    


    return nuevoPedido



