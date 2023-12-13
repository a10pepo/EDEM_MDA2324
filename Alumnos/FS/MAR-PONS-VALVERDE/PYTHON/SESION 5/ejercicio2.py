# Crea una clase Automóvil que disponga de los atributos necesarios y métodos para:
# 1-Arrancar
# 2-Acelerar
# 3-Frenar
# 4-Parar

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

# Ejemplo de uso
mi_auto = Automovil("Toyota", "Corolla", "rojo")
mi_auto.arrancar()
mi_auto.acelerar(30)
mi_auto.frenar(15)
mi_auto.parar()
mi_auto.arrancar()
mi_auto.acelerar(40)
mi_auto.parar()


