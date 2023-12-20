'''Ejercicio 2
Crea una clase Automóvil que disponga de los atributos necesarios y métodos para:
Arrancar
Acelerar
Frenar
Parar
Ejercicio 3
Crea clases de automóvil distintas como y que dispongan de distintos atributos, pero hereden los métodos de Automóvil a la hora de Arrancar, Acelerar, Frenar o Parar, salvo que algunos deben tener más potencia que otros:
Coche
Moto
Camión'''

class Automovil:

    marca:str
    modelo:str
    color:str
    matricula:str    
    id_seguro:str
    titular:str
    velocidad:float = 0
    ruedas:int

    def __init__(self, marca,modelo,color,matricula,id_seguro,titular,velocidad,ruedas,):
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.matricula=matricula
        self.id_seguro=id_seguro
        self.titular=titular
        self.velocidad=velocidad
        self.ruedas = ruedas

    
    def arrancar(self):
      self.velocidad = 10
      print('El coche ha arrancado')
      
    def frenar(self):
      self.velocidad-=5
      print(f'El coche ha frenado. Su velocidad ahora es {self.velocidad}km/h')
    
    def acelerar(self):
      self.velocidad +=5
      print(f'El coche ha acelerado. Su velocidad ahora es {self.velocidad}km/h')

    def parar(self):
      self.velocidad = 0
      print(f'El coche ha parado. Su velocidad ahora es {self.velocidad}km/h')

vehiculo=Automovil(marca="Wolkswaguen",modelo="California",color="Azul",matricula=1234,id_seguro=11,titular="Josan",velocidad=0,ruedas=4)
print(vehiculo)
vehiculo.acelerar()
vehiculo.acelerar()
vehiculo.acelerar()
print(vehiculo)
vehiculo.frenar()
print(vehiculo)
vehiculo.frenar()
print(vehiculo)
vehiculo.parar()
print(vehiculo)
