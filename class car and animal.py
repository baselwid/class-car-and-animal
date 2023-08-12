
class Car:
    def __init__(self, make, model, year, mileage, engine_type):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.engine_type = engine_type

    def get_mileage(self):
        return self.mileage

    def set_mileage(self, new_mileage):
        while new_mileage <= self.mileage:
            print("New mileage should be greater than the current mileage.")
            new_mileage = int(input("Enter a new mileage: "))
        self.mileage = new_mileage


class Animal:
    def __init__(self, name, species, age, weight):
        self.name = name
        self.species = species
        self.age = age
        self.weight = weight

    def make_sound(self):
        if self.species == "mammal":
            print("The animal makes a different sound for mammals.")
        else:
            print("The animal makes a generic sound.")


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        while self.width <= 0 or self.height <= 0:
            print("Width and height should be greater than zero.")
            self.width = float(input("Enter the width: "))
            self.height = float(input("Enter the height: "))
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)