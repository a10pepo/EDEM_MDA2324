class Automovil:
    velocidad:int

    def __init__(self):
        self.velocidad = 0

    def arrancar(self):
        if (self.velocidad > 0):
            print(f'El vehículo ya está en marcha... {self.velocidad}km/h')
        else:
            self.velocidad += 20
            print(f'El vehículo está en marcha... {self.velocidad}km/h')
    
    def frenar(self):
        if (self.velocidad == 0):
            print(f'El vehículo está parado ya. {self.velocidad}km/h')
        else:
            if (self.velocidad < 21):
                self.velocidad = 0
                print('El vehículo está parado.')
            elif (self.velocidad >= 21):
                self.velocidad -= 20
                print(f'Bajando de marcha... {self.velocidad}km/h')
            
    def parar(self):
        if (self.velocidad == 0):
            print(f'El vehículo está parado ya. {self.velocidad}km/h')
        else:
            print('Parando el vehículo... \nEl vehículo está parado.')
        self.velocidad = 0
        
    def acelerar(self):
        self.velocidad += 20
        print(f'Subiendo de marcha... {self.velocidad}km/h')
