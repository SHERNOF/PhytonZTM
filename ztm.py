class Car:
    has_gasoline = True # Class object attribute
    def __init__(self, brand='Tesla', speed=1):
        if brand == 'Kawasaki':
            self.brand = brand #attributes
            self.speed = speed
    
    def accelerate(self):
        # if Car.has_gasoline:
        self.speed += 10
        print(f'{self.brand} is now going {self.speed} km/h')

my_car2 = Car('Kawasaki', 5)
my_car = Car('Tesla', 20)

my_car2.accelerate()
my_car.accelerate()




    

    