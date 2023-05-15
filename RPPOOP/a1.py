#ASSIGNMENT 1 - DEMONSTRATION OF DIFFERENT TYPES OF INHERITANCE IN PYTHON


#----FULL CODE HERE-----

class Vehicle:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def description(self):
        print(f"This is a {self.year} {self.make} {self.model} with {self.mileage} miles on it.")
        
class Watercraft:
    def __init__(self, buoyancy, water_resistance):
        self.buoyancy = buoyancy
        self.water_resistance = water_resistance

class Car(Vehicle):
    def __init__(self, make, model, year, mileage, num_doors):
        super().__init__(make, model, year, mileage)
        self.num_doors = num_doors

    def description(self):
        super().description()
        print(f"It has {self.num_doors} doors.")
        
class Bike(Vehicle):
    def __init__(self, make, model, year, mileage, num_wheels):
        super().__init__(make, model, year, mileage)
        self.num_wheels = num_wheels

    def description(self):
        super().description()
        print(f"It has {self.num_wheels} wheels.")
        
class SportsCar(Car):
    def __init__(self, make, model, year, mileage, num_doors, top_speed):
        super().__init__(make, model, year, mileage, num_doors)
        self.top_speed = top_speed

    def description(self):
        super().description()
        print(f"It has a top speed of {self.top_speed} mph.")
        
class SportsBike(Bike):
    def __init__(self, make, model, year, mileage, num_doors, top_speed):
        super().__init__(make, model, year, mileage, num_doors)
        self.top_speed = top_speed

    def description(self):
        super().description()
        print(f"It has a top speed of {self.top_speed} mph.")
        
class AmphibiousVehicle(Vehicle, Watercraft):
    def __init__(self, make, model, year, mileage, speed, acceleration, fuel_capacity, buoyancy, water_resistance):
        Vehicle.__init__(self, make, model, year, mileage)
        Watercraft.__init__(self, buoyancy, water_resistance)
        self.speed = speed
        self.acceleration = acceleration
        self.fuel_capacity = fuel_capacity

    def navigate(self):
        print("Can also navigating on land and water...")


my_car = Car("Toyota", "Corolla", 2015, 45000, 4)
my_car.description()

print("\n")

my_sports_car = SportsCar("Lykan", "Hypersport", 2021, 1000, 2, 342)
my_sports_car.description()

print("\n")

my_bike = Bike("Honda", "CBR600RR", 2020, 1000, 2)
my_bike.description()

print("\n")

my_sports_bike = SportsBike("Ducati", "XDiavel Dark", 2023, 1250, 2, 242)
my_sports_bike.description()

print("\n")

amphibious_vehi = AmphibiousVehicle("Indian Armed Forces", "BMP-II", 2021, 10000, 100, 10, 50, 200, 100)
amphibious_vehi.description()
amphibious_vehi.navigate()