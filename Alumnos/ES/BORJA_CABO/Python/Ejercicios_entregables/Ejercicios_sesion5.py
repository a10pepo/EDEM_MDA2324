# EJERCICIOS SESIÓN 5

# Ejercicio 1
import pandas as pd 
df = pd.read_csv('archivo.csv')

# Ejercicio 2
class automovil:    
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0
        self.encendido = False

    def arrancar(self):
        if not self.encendido:
            print('Arranacando el motor')
            self.encendido = True
        else:
            print('El motor ya está en marcha')

    def acelerar(self, acelerando):
        if self.encendido:
            self.velocidad += acelerando
            print(f'Acelerado la velocidad actual es de {self.velocidad} ')
        else:
            print('El motor no está encendido')
    def frenar(self,frenando):
        if self.encendido:
            self.velocidad -= frenando
            print(f'Frenando la velocidad actual es de {self.velocidad} ')
        elif self.velocidad <= 0:
            print('El automovil ya está detenido')
        else:
            print('El motor no está encendido') 
    def parar(self):
        if self.encendido and self.velocidad == 0:
            print('Apagando el motor')
            self.encendido = False
        elif self.encendido and self.velocidad > 0:
            print('Antes de apagar el motor deten el automovil')
        else:
            print('El motor ya está apagado')


# Ejercicio 3

class coche(automovil):
    def __init__(self, marca, modelo, color, caballos):
        super().__init__(marca, modelo, color)
        self.caballos = caballos
        
    def acelerar(self,acelerando):
        if self.encendido:
            self.velocidad += acelerando * self.caballos/100
            print(f'Acelerado la velocidad actual es de {self.velocidad} ')
        else:
            print('El motor no está encendido') 

class moto(automovil):
    def __init__(self, marca, modelo, color, cilindrada):
        super().__init__(marca, modelo, color)
        self.cilindrada = cilindrada
        
    def acelerar(self,acelerando):
        if self.encendido:
            self.velocidad += acelerando * self.cilindrada/50
            print(f'Acelerado la velocidad actual es de {self.velocidad} ')
        else:
            print('El motor no está encendido') 

class camion(automovil):
    def __init__(self, marca, modelo, color, carga):
        super().__init__(marca, modelo, color)
        self.carga = carga
        
    def acelerar(self,acelerando):
        if self.encendido:
            self.velocidad += acelerando / self.carga * 2
            print(f'Acelerado la velocidad actual es de {self.velocidad} ')
        else:
            print('El motor no está encendido') 



    
