'''Crea clases de automóvil distintas como y que dispongan de distintos atributos, pero hereden los métodos de Automóvil a la hora de Arrancar, Acelerar, Frenar o Parar, salvo que algunos deben tener más potencia que otros:
Coche
Moto
Camión'''

from Ejercicio2 import Automovil

class Coche(Automovil):
        numero_plazas: str
        

        def __init__(self, marca, modelo, color, 
                        matricula, id_seguro, titular, carburante,tipo, 
                        numero_plazas):
                super(Coche, self).__init__(marca, modelo, color, matricula,
                                            id_seguro, titular, carburante, tipo)
                self.numero_plazas = numero_plazas
                



class Moto(Automovil):
        
        cilindrada: float

        def __init__(self, marca, modelo, color, 
                        matricula, id_seguro, titular,
                     	carburante,tipo, cilindrada):
                super(Moto, self).__init__(marca, modelo, color,
                                           matricula, id_seguro, titular, carburante, tipo)
                
                self.cilindrada = cilindrada

        # Con esto sobreescribimos el método de la clase padre
        # Así se comporta diferente al resto de clases que heredan de Automóvil 
        def acelerar(self, presion: float,potencia):
                self.velocidad_actual += (presion + potencia)
                print(f'La moto ha acelerado, su velocidad ahora es de {self.velocidad_actual}. Es muy rápida!')

class Camión(Automovil):
        carga: float
        caballos: int
        
        def __init__(self, marca, modelo, color, 
                        matricula, id_seguro, titular,
                     	carburante, carga, caballos):
                super(Camión, self).__init__(marca, modelo, color,
                                           matricula, id_seguro, titular, carburante)
                self.carga = carga
                self.caballos = caballos
                

        
        

Coche_prueba: Coche = Coche("Mercedes", "CLA", "Negro", "6754IOP","5432", "Yael", "Gasolina","Coche","4")
Coche_prueba.arrancar(10)
Coche_prueba.acelerar(14,10)
Coche_prueba.frenar(21,10)
Coche_prueba.parar()
moto_ejemplo: Moto= Moto("BMW", "R1200", "Negro", "6754IOP","5432", "Yael", "Gasolina","Moto","125")
moto_ejemplo.arrancar(8)
moto_ejemplo.acelerar(12,8)
moto_ejemplo.frenar(16,8)
moto_ejemplo.parar()
