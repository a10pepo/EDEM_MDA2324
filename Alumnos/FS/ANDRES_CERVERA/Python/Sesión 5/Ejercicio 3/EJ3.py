#Crea clases de automóvil distintas como y que dispongan de distintos atributos, pero hereden los métodos de Automóvil a la hora de Arrancar, Acelerar, Frenar o Parar, salvo que algunos deben tener más potencia que otros: coche, moto,camión.
class Automovil:
    
    def __init__(init, marca, modelo):
        init.marca = marca
        init.modelo = modelo
        init.velocidad = 0
        init.encendido = False
        
    def arrancar(init):
        if not init.encendido:
            init.encendido = True
            print(f'Vehículo arrancado')
        else:
            print(f'Ya estaba arrancado')
            print(f'La velocidad del vehículo es {init.velocidad} KM/H')
            
    def acelerar(init, velocidad):
        if init.encendido == True:
            init.velocidad += velocidad
            print(f'Acelerando...\n'
                    f'La velocidad del vehículo es {init.velocidad} KM/H')
        else:
            print('El vehículo está apagado')
    
    def frenar(init, velocidad):
        if init.encendido == True:
            init.velocidad -= velocidad
            print(f'Frenando...\n'
                    f'La velocidad del vehículo es {init.velocidad} KM/H')
        else:
            print('El vehículo está apagado')
    
    def parar(init):
        if init.encendido:
            init.encendido = False
            init.velocidad = 0
            print(f'vehículo parado')
            print(f'La velocidad del vehículo es {init.velocidad} KM/H')
        else:
            print(f'Ya estaba apagado')
            

class Moto(Automovil):
    def __init__(init, marca, modelo):
        super().__init__(marca, modelo)
        init.potencia = 1000
              
class Coche(Automovil):
    def __init__(init, marca, modelo):
        super().__init__(marca, modelo)
        init.potencia = 2000

class Camion(Automovil):
    def __init__(init, marca, modelo):
        super().__init__(marca, modelo)
        init.potencia = 4000


moto = Moto(marca = 'Yamaha', modelo= 'TRX')
moto.arrancar()
moto.acelerar(10)
moto.frenar(5)
moto.parar()

coche = Coche(marca = 'Alfa Romeo', modelo= 'Giulietta')
coche.arrancar()
coche.acelerar(10)
coche.frenar(5)
coche.parar()

camion = Camion(marca = 'IVECO', modelo= 'Yoquese')
camion.arrancar()
camion.acelerar(10)
camion.frenar(5)
camion.parar()

