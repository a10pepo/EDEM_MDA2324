#Lee un archivo CSV con Pandas y realizar las siguientes operaciones (Pendiente de establecer)
#import pandas as pd
#df = pd.read_csv('RUTA ARCHIVO CSV')

#Crea una clase Automóvil que disponga de los atributos necesarios y métodos para:

class Automovil:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False
        self.velocidad = 0

    def arrancar(self):
        if not self.encendido:
            print("El automóvil está arrancando.")
            self.encendido = True
        else:
            print("El automóvil ya está en marcha.")

    def acelerar(self, incremento):
        if self.encendido:
            self.velocidad += incremento
            print(f"Acelerando. Velocidad actual: {self.velocidad} km/h")
        else:
            print("No puedes acelerar, el automóvil está apagado.")

    def frenar(self, decremento):
        if self.encendido and self.velocidad > 0:
            self.velocidad -= decremento
            print(f"Frenando. Velocidad actual: {self.velocidad} km/h")
        elif self.velocidad == 0:
            print("El automóvil ya está detenido.")
        else:
            print("No puedes frenar, el automóvil está apagado.")

    def parar(self):
        if self.encendido:
            print("Apagando el automóvil.")
            self.encendido = False
            self.velocidad = 0
        else:
            print("El automóvil ya está apagado.")

mi_auto = Automovil(marca="Toyota", modelo="Corolla", color="Rojo")

mi_auto.arrancar()
mi_auto.acelerar(20)
mi_auto.frenar(10)
mi_auto.parar()

#Crea clases de automóvil distintas como y que dispongan de distintos atributos, pero hereden los 
#métodos de Automóvil a la hora de Arrancar, Acelerar, Frenar o Parar, salvo que algunos deben tener más potencia que otros:

class Automovil:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False
        self.velocidad = 0

    def arrancar(self):
        if not self.encendido:
            print(f"{self.marca} {self.modelo} está arrancando.")
            self.encendido = True
        else:
            print(f"{self.marca} {self.modelo} ya está en marcha.")

    def acelerar(self, incremento):
        if self.encendido:
            self.velocidad += incremento
            print(f"Acelerando. Velocidad actual: {self.velocidad} km/h")
        else:
            print("No puedes acelerar, el automóvil está apagado.")

    def frenar(self, decremento):
        if self.encendido and self.velocidad > 0:
            self.velocidad -= decremento
            print(f"Frenando. Velocidad actual: {self.velocidad} km/h")
        elif self.velocidad == 0:
            print(f"{self.marca} {self.modelo} ya está detenido.")
        else:
            print("No puedes frenar, el automóvil está apagado.")

    def parar(self):
        if self.encendido:
            print(f"Apagando {self.marca} {self.modelo}.")
            self.encendido = False
            self.velocidad = 0
        else:
            print(f"{self.marca} {self.modelo} ya está apagado.")


class Coche(Automovil):
    def __init__(self, marca, modelo, color, numero_puertas):
        super().__init__(marca, modelo, color)
        self.numero_puertas = numero_puertas


class Moto(Automovil):
    def __init__(self, marca, modelo, color, tipo):
        super().__init__(marca, modelo, color)
        self.tipo = tipo

    def acelerar(self, incremento):
        # Aumentamos la potencia de la moto
        if self.encendido:
            self.velocidad += 2 * incremento
            print(f"Acelerando. Velocidad actual: {self.velocidad} km/h")
        else:
            print("No puedes acelerar, la moto está apagada.")


class Camion(Automovil):
    def __init__(self, marca, modelo, color, capacidad_carga):
        super().__init__(marca, modelo, color)
        self.capacidad_carga = capacidad_carga


coche = Coche(marca="Ford", modelo="Focus", color="Azul", numero_puertas=4)
moto = Moto(marca="Honda", modelo="CBR", color="Negro", tipo="Deportiva")
camion = Camion(marca="Volvo", modelo="VNL", color="Blanco", capacidad_carga=10000)

coche.arrancar()
coche.acelerar(30)
coche.frenar(10)
coche.parar()

moto.arrancar()
moto.acelerar(30)
moto.frenar(10)
moto.parar()

camion.arrancar()
camion.acelerar(20)
camion.frenar(5)
camion.parar()
