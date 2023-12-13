#Crea clases de automóvil distintas como y que dispongan de distintos atributos, pero hereden los métodos de Automóvil a la hora de Arrancar, Acelerar, Frenar o Parar, salvo que algunos deben tener más potencia que otros:
#-Coche
#-Moto
#-Camión

class Automovil:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False
        self.velocidad = 0

    def arrancar(self):
        if not self.encendido:
            self.encendido = True
            print(f"El {self.marca} {self.modelo} de color {self.color} ha sido encendido.")
        else:
            print(f"El {self.marca} {self.modelo} ya está en marcha.")

    def acelerar(self, incremento):
        if self.encendido:
            self.velocidad += incremento
            print(f"El {self.marca} {self.modelo} ha acelerado. Velocidad actual: {self.velocidad} km/h.")
        else:
            print(f"Primero debes encender el {self.marca} {self.modelo}.")

    def frenar(self, decremento):
        if self.encendido and self.velocidad > 0:
            if decremento > self.velocidad:
                self.velocidad = 0
            else:
                self.velocidad -= decremento
            print(f"El {self.marca} {self.modelo} ha frenado. Velocidad actual: {self.velocidad} km/h.")
        else:
            print(f"El {self.marca} {self.modelo} no puede frenar si está apagado o detenido.")

    def parar(self):
        if self.encendido and self.velocidad == 0:
            print(f"El {self.marca} {self.modelo} ha sido detenido.")
            self.encendido = False
        elif self.velocidad > 0:
            print(f"El {self.marca} {self.modelo} está en movimiento. Debes frenar primero.")
        else:
            print(f"El {self.marca} {self.modelo} ya está apagado.")


class Coche(Automovil):
    def __init__(self, marca, modelo, color, potencia_motor):
        super().__init__(marca, modelo, color)
        self.potencia_motor = potencia_motor


class Moto(Automovil):
    def __init__(self, marca, modelo, color, cilindrada):
        super().__init__(marca, modelo, color)
        self.cilindrada = cilindrada


class Camion(Automovil):
    def __init__(self, marca, modelo, color, capacidad_carga):
        super().__init__(marca, modelo, color)
        self.capacidad_carga = capacidad_carga

# Ejemplo de uso
mi_coche = Coche("Toyota", "Corolla", "rojo", "200 HP")
mi_moto = Moto("Honda", "CBR", "negro", "600 cc")
mi_camion = Camion("Volvo", "FH", "blanco", "5000 kg")

mi_coche.arrancar()
mi_moto.arrancar()
mi_camion.arrancar()

mi_coche.acelerar(40)
mi_moto.acelerar(30)
mi_camion.acelerar(20)

mi_coche.parar()
mi_moto.parar()
mi_camion.parar()

#super() es una función en Python que se utiliza para acceder y llamar a métodos definidos en la clase padre o clase base
# desde una subclase o clase hija. En el contexto de la herencia, super() permite invocar métodos de la clase padre desde la subclase, 
# facilitando la implementación de la herencia y el uso de los métodos y atributos de la clase base.