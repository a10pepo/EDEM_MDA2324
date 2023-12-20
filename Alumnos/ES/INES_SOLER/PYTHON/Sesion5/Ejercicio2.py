'''
Crea una clase Automóvil que disponga de los atributos necesarios y métodos para:
- Arrancar
- Acelerar
- Frenar
- Parar
'''

class Coche():
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
      print('El coche ha arrancado')

    def acelerar(self, presion: float):
      self.velocidad += (presion + 10)
      print(f'El coche ha acelerado. Su velocidad ahora es {self.velocidad}km/h')

      
    def frenar(self, presion: float):
      self.velocidad -= (presion - 10)
      print(f'El coche ha frenado. Su velocidad ahora es {self.velocidad}km/h')
    
    def parar(self):
      self.velocidad = 0
      print(f'El coche se ha detenido. Su velocidad ahora es {self.velocidad}km/h')
    
 

coche_1: Coche = Coche("Audi", "A3", "Blanco", "7947M")
coche_1.arrancar()
coche_1.acelerar(2)
coche_1.frenar(12)
coche_1.parar()