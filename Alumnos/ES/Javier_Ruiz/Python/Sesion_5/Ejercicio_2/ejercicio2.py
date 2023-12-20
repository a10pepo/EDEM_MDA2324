class Automovil:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0
        self.en_movimiento = False

    def arrancar(self):
        if not self.en_movimiento:
            print(f"El {self.marca} {self.modelo} {self.color} está arrancando.")
            self.en_movimiento = True
        else:
            print(f"El {self.marca} {self.modelo} ya está en movimiento.")

    def acelerar(self, velocidad_aumento, potencia_motor=None):  #potencia_motor lo añado para el ejercicio3
        if self.en_movimiento:
            if potencia_motor:
                velocidad_aumento *= potencia_motor / 100
            self.velocidad += velocidad_aumento
            print(f"Acelerando. Velocidad actual: {self.velocidad} km/h.")
        else:
            print(f"No se puede acelerar, primero arranca el vehiculo.")

    def frenar(self, velocidad_disminucion):
        if self.en_movimiento:
            self.velocidad = max(0, self.velocidad - velocidad_disminucion)
            print(f"Frenando. Velocidad actual: {self.velocidad} km/h.")
        else:
            print(f"No se puede frenar, primero pon el vehiculo en marcha.")

    def parar(self):
        if self.en_movimiento:
            print(f"Deteniendo {self.marca} {self.modelo}.")
            self.velocidad = 0
            self.en_movimiento = False
        else:
            print("Aparcao")


