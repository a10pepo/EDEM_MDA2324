'''Ejercicio 3
Crea clases de automóvil distintas como y que dispongan de distintos atributos, pero hereden los métodos de Automóvil a la hora de Arrancar, Acelerar, Frenar o Parar, salvo que algunos deben tener más potencia que otros:
Coche
Moto
Camión'''

from ejercicio2 import Automovil
	
class Moto(Automovil):

    tipodemoto:str

    def __init__(self, marca, modelo, color, matricula, id_seguro, titular, velocidad, ruedas, tipodemoto):
        super().__init__(marca, modelo, color, matricula, id_seguro, titular, velocidad, ruedas)
        
        self.tipodemoto = tipodemoto

    
    def realizar_acrobacia(self):
        print(f"La moto ha realizado una acrobacia.")
			


class Camion(Automovil):

    capacidad_carga:int

    def __init__(self, marca, modelo, color, matricula, id_seguro, titular, velocidad, ruedas, capacidad_carga):
        super().__init__(marca, modelo, color, matricula, id_seguro, titular, velocidad, ruedas)
        
        self.capacidad_carga = capacidad_carga

    
    def cargar_mercancia(self):
        print(f"El camión ha cargado mercancía.")



moto1= Moto(marca="Honda", modelo="CBR", color="Rojo", matricula="ABC123", id_seguro="12345",
                    titular="Juan", velocidad=0, ruedas=2, tipodemoto="Deportiva")


print(moto1.velocidad)  
moto1.arrancar()
print(moto1.velocidad)  
moto1.realizar_acrobacia()
 

camion1=Camion(marca="Iveco",modelo="Star",color="Blanco",matricula="111111",id_seguro="222222",
               titular="Ana",velocidad=0,ruedas=8,capacidad_carga=20000)

camion1.arrancar()
print(camion1.velocidad)
camion1.cargar_mercancia()
