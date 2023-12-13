'''Crea una clase Automóvil que disponga de los atributos necesarios y métodos para:
Arrancar
Acelerar
Frenar
Parar'''

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

mi_auto = Automovil(marca="Nissan", modelo="X-Trail", color="Gris", dueño="Gabriela")
mi_auto.arrancar()
mi_auto.acelerar(20)
mi_auto.frenar(10)
mi_auto.parar()