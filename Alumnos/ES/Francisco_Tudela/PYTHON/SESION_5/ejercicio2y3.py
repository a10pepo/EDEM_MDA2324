class Automovil:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        self.velocidad = 0

    def arrancar(self):
        if not self.encendido:
            print("El vehiculo arrancó.")
            self.encendido = True
        else:
            print("Ya está en marcha.")

    def acelerar(self, velocidad):
        if self.encendido:
            self.velocidad += velocidad
            print(f"Vamos a {self.velocidad} km/h.")
        else:
            print("Para acelerar, primero arranca el motor.")

    def frenar(self, velocidad):
        if self.encendido and self.velocidad > 0:
            self.velocidad -= velocidad
            print(f"Has frenado y vas a {self.velocidad} km/h.")
        else:
            print("No puede frenar más, el coche esta parado.")

    def parar(self, apagar_motor=False):
        if self.velocidad == 0:
            print("El automóvil está detenido.")
            if apagar_motor:
                self.encendido = False
                print("Se ha apagado el motor.")
        else:
            print("Para detener el automóvil, primero frena completamente.")

auto = Automovil("Toyota", "Camry")

auto.arrancar()
auto.acelerar(50)
auto.frenar(30)
auto.parar(apagar_motor=True)


class Coche(Automovil):
    def __init__(self, marca, modelo, caballos):
        super().__init__(marca, modelo)
        self.caballos = caballos

class Moto(Automovil):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

class Camion(Automovil):
    def __init__(self, marca, modelo, potencia, capacidad_carga):
        super().__init__(marca, modelo)
        self.potencia = potencia
        self.capacidad_carga = capacidad_carga
