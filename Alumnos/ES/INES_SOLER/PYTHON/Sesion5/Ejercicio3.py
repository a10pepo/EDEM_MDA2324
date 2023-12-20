'''
Crea clases de automóvil distintas y que dispongan de distintos atributos, 
pero hereden los métodos de Automóvil a la hora de Arrancar, Acelerar, Frenar o Parar, 
salvo que algunos deben tener más potencia que otros:
Coche
Moto
Camión
'''

class Automovil():
    marca:str
    modelo:str
    color:str
    matricula:str    
    velocidad:float = 0
    
    def __init__(self, marca, modelo, color, matricula):
      self.marca = marca
      self.modelo = modelo
      self.color = color
      self.matricula = matricula
    
    def arrancar(self):
      self.velocidad = 10
      print(f'El {self.marca} {self.modelo} ha arrancado')

    def acelerar(self, presion: float):
      self.velocidad += (presion + self.potencia)
      print(f'El {self.marca} {self.modelo} ha acelerado. Su velocidad ahora es {self.velocidad}km/h')

      
    def frenar(self, presion: float):
      self.velocidad -= (presion - self.potencia)
      print(f'El {self.marca} {self.modelo} ha frenado. Su velocidad ahora es {self.velocidad}km/h')
    
    def parar(self):
      self.velocidad = 0
      print(f'El {self.marca} {self.modelo} se ha detenido. Su velocidad ahora es {self.velocidad}km/h')


class Coche(Automovil):
  potencia = 10

class Moto(Automovil):
  potencia = 7

class Camion(Automovil):
  potencia = 15



coche_1 = Coche("Audi", "A3", "Blanco", "7947MKD")
moto_1 = Moto("Ducati", "Panigale", "Negro", "9283PEN")
camion_1 = Camion("Mercedes-Benz", "Actros", "Azul", "5821COA")

coche_1.arrancar()
coche_1.acelerar(20)
coche_1.frenar(10)
coche_1.parar()

moto_1.arrancar()
moto_1.acelerar(15)
moto_1.frenar(5)
moto_1.parar()

camion_1.arrancar()
camion_1.acelerar(30)
camion_1.frenar(15)
camion_1.parar()