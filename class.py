class vehicle:
    def printConsum(self):
        print("low")

class Car(vehicle):
    pass

class Truck(vehicle):
    def printConsum(self):
        print("high")


car = Car()
car.printConsum()

truck = Truck()
truck.printConsum()