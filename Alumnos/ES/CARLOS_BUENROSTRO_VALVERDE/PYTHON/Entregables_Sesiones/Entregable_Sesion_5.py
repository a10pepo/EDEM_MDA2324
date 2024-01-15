# Lee un archivo CSV con Pandas y realizar las siguientes operaciones
# import pandas as pd

# df = pd.read_csv("datos_coches.csv")
# 2 - Crea una clase Automóvil que disponga de los atributos necesarios y métodos para:
# class Automovil:
#     def __init__(self, marca, modelo, color):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
#         self.arrancado = False
#         self.velocidad = 0
#     def arrancar(self):
#         if self.arrancado:
#             print('El vehículo está arrancado.')
#         else:
#             print('El vehículo está apaagdo')
#     def acelerar(self, incremento):
#         if self.arrancado:
#             self.velocidad += incremento
#         else:
#             print('No se puede acelerar. Por favor arranque el vehículo.')
#     def frenar(self, reduccion):
#         if self.arrancado and self.velocidad > 0:
#             self.velocidad -= reduccion
#             print('Se está frenando el vehículo.')
#         else:
#             print('No se puede frenar. Encienda el vehículo.')
#     def parar(self):
#         if self.arrancado:
#             self.arrancado = False
#             self.velocidad = 0
#             print('El coche se encuentra detenido.')
#         else:
#             print('Reduzca velocidad. Frene y apague el coche.')

# 3- Crea clases de automóvil distintas como y que dispongan de distintos atributos, pero hereden los métodos de Automóvil a la hora de Arrancar, Acelerar, Frenar o Parar, salvo que algunos deben tener más potencia que otros:
    # Coche
    # Moto
    # Camión
            
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
        self.velocidad += incremento 
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
        self.velocidad += incremento 
        print(f"El automóvil está acelerando. Velocidad actual: {self.velocidad} km/h.")
        
coche = Coche(marca="Mercedes", modelo="E-280 CDI", color="Negro", dueño="Carlos", potencia=248)
moto = Moto(marca="Honda", modelo="SWT-400 ABS", color="Negro", dueño="Carlos", potencia=42)
camion = Camion(marca="IVECO", modelo="EuroCargo", color="Azul", dueño="Jose Luis", potencia = 320)

print("Coche")
coche.arrancar()
coche.acelerar(120)
coche.frenar(60)

print("Moto")
moto.arrancar()
moto.acelerar(110)
moto.frenar(50)

print("Camion")
camion.arrancar()
camion.acelerar(90)
camion.frenar(40)