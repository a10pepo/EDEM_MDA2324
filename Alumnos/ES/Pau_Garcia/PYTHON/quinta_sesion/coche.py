from motor import Automovil
import time

class Coche(Automovil):
    potencia:int
    peso:int

    def __init__(self):
        super(Automovil, self).__init__()
        self.potencia = 2
        self.peso = 1000
        self.velocidad = 0

    def drive(self):
        self.arrancar()
        while (self.velocidad < 260):
            self.acelerar()
            time.sleep(1)
        print(f'La moto está en velocidad de crucero. {self.velocidad}km/h.')
    
    def stop(self):
        while (self.velocidad>20):
            self.frenar()
            time.sleep(1)
        self.parar()

class Moto(Automovil):
    potencia:int
    peso: int

    def __init__(self):
        super(Automovil, self).__init__()
        self.potencia = 2
        self.peso = 300
        self.velocidad = 0

    def drive(self):
        self.arrancar()
        while (self.velocidad < 150):
            self.acelerar()
            time.sleep(1)
        print(f'La moto está en velocidad de crucero. {self.velocidad}km/h.')
    
    def stop(self):
        while (self.velocidad>20):
            self.frenar()
            time.sleep(1)
        self.parar()

class Camion(Automovil):
    potencia:int
    peso:int
    def __init__(self):
        super(Automovil, self).__init__()
        self.potencia = 6
        self.peso = 4000
        self.velocidad = 0

    def drive(self):
        self.arrancar()
        while (self.velocidad < 60):
            self.acelerar()
            time.sleep(1)
        print(f'El camión está en velocidad de crucero. {self.velocidad}km/h.')
    
    def stop(self):
        while (self.velocidad>20):
            self.frenar()
            time.sleep(1)
        self.parar()

volvo = Camion()
volvo.drive()
volvo.stop()

honda = Moto()
honda.drive()
honda.stop()

bmw = Coche()
bmw.drive()
bmw.stop()
    
