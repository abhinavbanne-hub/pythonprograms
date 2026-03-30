# Base class
class Vehicle:
    def move(self):
        print("Vehicle is moving")


# Subclass 1
class Car(Vehicle):
    def move(self):
        print("Driving on the road")


# Subclass 2
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the road")


# Demonstrating polymorphism
vehicles = [Car(), Bicycle()]

for v in vehicles:
    v.move()   # Same method call, different behavior
