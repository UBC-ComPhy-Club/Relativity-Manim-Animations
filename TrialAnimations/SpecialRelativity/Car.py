from Vehicle import Vehicle

class Car(Vehicle):
    Vehicle = 'Car'
    Velocity = 10

    def __init__(self, colour, velocity=0):
        self.colour = colour
        self.velocity = velocity

    def drive(self):
        self.speed = 10
        self.mom = 'lmao'

    def stop(self):
        self.speed = 0

