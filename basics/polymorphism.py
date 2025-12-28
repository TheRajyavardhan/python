# class Animal:
#     def speak(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")
# a = Animal()
# d = Dog()

# a.speak()   # Animal makes a sound
# d.speak()   # Dog barks

class Vehicle:
    def move(self):
         print("Vehicle is moving")
class Car(Vehicle):
    def move(self):
        print("Car is moving")
class Bike(Vehicle):
    def move(self):
        print("Bike is moving")
class Boat(Vehicle):
    def move(self):
        print("Boat is moving")

obj = [Bike(),Car(),Boat()]

for i in obj:
    i.move()
