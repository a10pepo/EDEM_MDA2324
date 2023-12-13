#Session 5 exercise 3 - EDEM MDA ES Julián Merino Pérez
#Using Vehicle class, create Car, Motorbike and Truck classes with additional attributes and inheriting the same methods:
from vehicles import Vehicle

class Car(Vehicle):
    mov_roof: bool
    engine_class: str

    def __init__(self, type, brand, model, colour, registration, insurance_no, vin, owner, speed, bhp, mov_roof, engine_class):
        super(Car, self).__init__(type, brand, model, colour, registration, insurance_no, vin, owner, speed, bhp)
        self.mov_roof = mov_roof
        self.engine_class = engine_class

    def roof_switch(self):
        if self.mov_roof == False:
            print('This {self.type} has no practicable roof.')
        if self.mov_roof == True and self.speed > 10:
            print(f'Speed ({self.speed} km/h) above the safety limit, the roof cannot be engaged. Reduce speed.')
        else:
            print('Roof moving...')

class Moto(Vehicle):
    autoclutch: bool

    def __init__(self, type, brand, model, colour, registration, insurance_no, vin, owner, speed, bhp, autoclutch):
        super(Moto, self).__init__(type, brand, model, colour, registration, insurance_no, vin, owner, speed, bhp)
        self.autoclutch = autoclutch

    def clutch_switch(self):
        if self.autoclutch == False:
            print('Only manual clutch available.')
        else:
            print('Clutch switched to manual/auto.')

class Truck(Vehicle):
    cargo: bool

    def __init__(self, type, brand, model, colour, registration, insurance_no, vin, owner, speed, bhp, cargo):
        super(Truck, self).__init__(type, brand, model, colour, registration, insurance_no, vin, owner, speed, bhp)
        self.cargo = cargo

    def cargo_switch(self):
        if self.cargo == False:
            print('Cargo attached.')
            self.cargo = True
        else:
            print('Cargo detached.')
            self.cargo = False

car: Vehicle = Car('car', 'BMW', 'i8', 'Blue', '4698STH', '0479635', '964789VGHT8', 'Jules Merino', 0.0, 500, True, 'C-class')
car.start_engine()
car.accelerate(35)
car.roof_switch()
car.brake(30)
car.roof_switch()
car.stop_engine()
print(car)

moto: Vehicle = Moto('motorbike', 'Ducati', 'Superfiore', 'Red', '846IJO', '469741', '84584MTB', 'María Casablancas', 0.0, 200, True)
moto.start_engine()
moto.accelerate(95)
moto.clutch_switch()
moto.brake(30)
moto.stop_engine()
print(moto)

truck: Vehicle = Truck('truck', 'Iveco', 'MAD9000', 'White', '4040MAR', '909574', 'ARM74698V', 'Mike Biza', 0.0, 2500, False)
truck.start_engine()
truck.accelerate(73)
truck.cargo_switch()
truck.brake(21)
truck.stop_engine()
truck.cargo_switch()
print(truck)