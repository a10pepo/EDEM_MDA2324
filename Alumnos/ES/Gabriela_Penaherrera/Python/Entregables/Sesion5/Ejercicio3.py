'''Crea clases de automóvil distintas como y que dispongan de distintos atributos, pero 
hereden los métodos de Automóvil a la hora de Arrancar, Acelerar, Frenar o Parar, 
salvo que algunos deben tener más potencia que otros:
Coche
Moto
Camión'''

class Automovil():
    marca:str
    modelo:str
    color:str
    dueño:str
    velocidad:float = 0

    def __init__(self, marca, modelo, color, dueño, velocidad=0):
        self.marca= marca
        self.modelo= modelo
        self.color= color
        self.dueño= dueño
        self.velocidad= velocidad

    def arrancar(self):
        print("El automovil está arrancando.")

    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"El automóvil está acelerando la velocidad actual es: {self.velocidad} km/h.")

    def frenar(self, decremento):
        self.velocidad -= decremento
        print(f"El automóvil está frenando la velocidad actual es: {self.velocidad} km/h.")

    def parar(self):
        self.velocidad = 0
        print("El automóvil se ha detenido.")

class Coche(Automovil):
    def __init__(self, marca, modelo, color, dueño, potencia, velocidad=0):
        super().__init__(marca, modelo, color, dueño, velocidad)
        self.potencia = potencia

    def acelerar(self, incremento):
        self.velocidad += incremento * self.potencia
        print(f"El automóvil está acelerando. Velocidad actual: {self.velocidad} km/h.")

class Moto(Automovil):
    def __init__(self, marca, modelo, color, dueño, potencia, velocidad=0):
        super().__init__(marca, modelo, color, dueño, velocidad)
        self.potencia = potencia


class Camion(Automovil):
    def __init__(self, marca, modelo, color, dueño, potencia, velocidad=0):
        super().__init__(marca, modelo, color, dueño, velocidad)
        self.potencia = potencia
    
    def acelerar(self, incremento):
        self.velocidad += incremento * self.potencia
        print(f"El automóvil está acelerando. Velocidad actual: {self.velocidad} km/h.")
        
coche = Coche(marca="Nissan", modelo="X-Trail", color="Gris", dueño="Gabriela", potencia=3)
moto = Moto(marca="Yamaha", modelo="MT07", color="Azul", dueño="Jairo", potencia=1.5)
camion = Camion(marca="Volvo", modelo="Cargo", color="Negro", dueño="Juan", potencia = 6)

print("Coche")
coche.arrancar()
coche.acelerar(30)
coche.frenar(10)

print("Moto")
moto.arrancar()
moto.acelerar(50)
moto.frenar(15)

print("Camion")
camion.arrancar()
camion.acelerar(20)
camion.frenar(11)



