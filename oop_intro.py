class Car:
    def __init__(self, mk, mdl, yr):
        self.make = mk
        self.model = mdl
        self.year = yr

    def move(self):
        print("The car is moving")

    def horn(self):
        print("Beep beep!")

mycar = Car("Toyota", "Corolla", 2020)
mycar.horn()

another_car = Car("Honda", "Civic", 2019)
another_car.move()

print(mycar.make, another_car.make)


