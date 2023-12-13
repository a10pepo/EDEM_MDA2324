# EJERCICIOS SESION 5

# Ejercicio 5.1

import pandas as pd

df = pd.read_csv('datos.csv')


# Ejercicio 5.2

class Automovil:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0
        self.en_movimiento = False

    def arrancar(self):
        if not self.en_movimiento:
            self.en_movimiento = True

    def acelerar(self, incremento):
        if self.en_movimiento:
            self.velocidad += incremento

    def frenar(self, decremento):
        if self.en_movimiento and self.velocidad >= decremento:
            self.velocidad -= decremento
        elif self.en_movimiento and self.velocidad < decremento:
            self.velocidad = 0

    def parar(self):
        if self.en_movimiento:
            self.velocidad = 0
            self.en_movimiento = False


# Ejercicio 5.3

class Coche(Automovil):
    def __init__(self, marca, modelo, color, potencia):
        super().__init__(marca, modelo, color)
        self.potencia = potencia

    def acelerar(self, incremento):
        if self.en_movimiento:
            self.velocidad += incremento * self.potencia


class Moto(Automovil):
    def __init__(self, marca, modelo, color, cilindrada):
        super().__init__(marca, modelo, color)
        self.cilindrada = cilindrada

    def acelerar(self, incremento):
        if self.en_movimiento:
            self.velocidad += incremento * (self.cilindrada / 100)


class Camion(Automovil):
    def __init__(self, marca, modelo, color, capacidad_carga):
        super().__init__(marca, modelo, color)
        self.capacidad_carga = capacidad_carga

    def frenar(self, decremento):
        if self.en_movimiento and self.velocidad >= decremento / 2:
            self.velocidad -= decremento / 2
        elif self.en_movimiento and self.velocidad < decremento / 2:
            self.velocidad = 0