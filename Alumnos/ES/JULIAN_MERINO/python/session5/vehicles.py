#Session 5 exercise 2 - EDEM MDA ES Julián Merino Pérez
#Create the class Vehicle with attributes (including brake horse power - bhp) and methods to Start, Stop, Accelerate and Brake:
class Vehicle:
    type: str
    brand: str
    model: str
    colour: str
    registration: str
    insurance_no: str
    vin: str
    owner: str
    speed: float = 0.0
    bhp: int

    def __init__(self, type, brand, model, colour, registration, insurance_no, vin, owner, speed, bhp):
        self.type = type
        self.brand = brand
        self.model = model
        self.colour = colour
        self.registration = registration
        self.insurance_no = insurance_no
        self.owner = owner
        self.vin = vin
        self.speed = speed
        self.bhp = bhp

    def accelerate(self, speed_var):
        self.speed += speed_var
        print(f'The {self.type} has accelerated, the speed is now {self.speed} km/h.')
    
    def start_engine(self):
        self.speed = 5.0
        print(f'The {self.type} has started.')
    
    def brake(self, speed_var): 
        if speed_var >= self.speed:
            self.speed = 0.0
            print(f'The {self.type} has stopped the engine.')
        else:
            self.speed -= speed_var
            print(f'The {self.type} has braked, the speed is now {self.speed} km/h.')

    def stop_engine(self):
        self.speed = 0.0
        print(f'The {self.type} has stopped the engine.')

#car: Vehicle = Vehicle('car', 'BMW', 'i8', 'Blue', '4698STH', '0479635', '964789VGHT8', 'Jules Merino', 0.0, 500)
#car.start_engine()
#car.accelerate(35)
#car.brake(40)
#car.stop_engine()
#print(car)