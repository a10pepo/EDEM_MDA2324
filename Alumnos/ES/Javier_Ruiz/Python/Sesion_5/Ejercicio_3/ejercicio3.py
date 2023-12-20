from Ejercicio_2.ejercicio2 import Automovil

class Coche(Automovil):
    def __init__(self, marca, modelo, color, potencia_motor):
        super().__init__(marca, modelo, color)
        self.potencia_motor = potencia_motor

class Moto(Automovil):
    def __init__(self, marca, modelo, color, potencia_motor):
        super().__init__(marca, modelo, color)
        self.potencia_motor = potencia_motor

class Camion(Automovil):
    def __init__(self, marca, modelo, color, potencia_motor):
        super().__init__(marca, modelo, color)
        self.potencia_motor = potencia_motor


# Instancias de cada clase
coche = Coche(marca="Mercedes", modelo="Clase G", color="Negra", potencia_motor=150)
moto = Moto(marca="Suzuki", modelo="GS500", color="Azul", potencia_motor=180)
camion = Camion(marca="Volvo", modelo="Transporter", color="Amarillo", potencia_motor=100)

# Utilizar métodos heredados
coche.arrancar()
coche.acelerar(90)
coche.frenar(25)
coche.parar()

moto.arrancar()
moto.acelerar(120)
moto.frenar(25)
moto.parar()

camion.arrancar()
camion.acelerar(80)
camion.frenar(15)
camion.parar()