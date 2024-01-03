#Crea una clase Automóvil que disponga de los atributos necesarios y métodos para: Arrancar, Acelerar, Frenar, Parar

class Automovil:
    
    def __init__(init, marca, modelo):
        init.marca = marca
        init.modelo = modelo
        init.velocidad = 0
        init.encendido = False
        
    def arrancar(init):
        if not init.encendido:
            init.encendido = True
            print(f'Coche arrancado')
        else:
            print(f'Ya estaba arrancado')
            print(f'La velocidad del coche es {init.velocidad} KM/H')
            
    def acelerar(init, velocidad):
        if init.encendido == True:
            init.velocidad += velocidad
            print(f'Acelerando...\n'
                    f'La velocidad del coche es {init.velocidad} KM/H')
        else:
            print('El coche está apagado')
    
    def frenar(init, velocidad):
        if init.encendido == True:
            init.velocidad -= velocidad
            print(f'Frenando...\n'
                    f'La velocidad del coche es {init.velocidad} KM/H')
        else:
            print('El coche está apagado')
    
    def parar(init):
        if init.encendido:
            init.encendido = False
            init.velocidad = 0
            print(f'Coche parado')
            print(f'La velocidad del coche es {init.velocidad} KM/H')
        else:
            print(f'Ya estaba apagado')
            
        
coche = Automovil(marca = 'Alfa Romeo', modelo= 'Giulietta')

coche.arrancar()
coche.acelerar(10)
coche.frenar(5)
coche.parar()

