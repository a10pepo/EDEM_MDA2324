'''
Crea una clase Automóvil que disponga de los atributos necesarios y métodos para:
Arrancar
Acelerar
Frenar
Parar
'''

class Automovil:
    marca: str
    modelo: str
    color: str
    matricula: str
    id_seguro: str
    titular: str
    velocidad_actual: float = 0
    carburante: str
    tipo: str
    
    def __init__(self, marca, modelo, color, matricula, id_seguro, titular, carburante,tipo):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.matricula = matricula
        self.id_seguro = id_seguro
        self.titular = titular
        self.carburante = carburante
        self.tipo = tipo
    
    def arrancar(self, potencia):
        self.velocidad_actual = potencia
        print(f'El {self.tipo} ha arrancado')
    
    def frenar(self, presion: float, potencia):
        self.velocidad_actual -= (presion - potencia)
        print(f'El {self.tipo} ha frenado. Su velocidad ahora es de {self.velocidad_actual}')
    
    def acelerar(self, presion: float, potencia):
        self.velocidad_actual += (presion + potencia)
        print(f'El {self.tipo} ha acelerado. Su velocidad ahora es de {self.velocidad_actual}')

    def parar(self):
      self.velocidad = 0
      print(f'El {self.tipo} ha parado')




