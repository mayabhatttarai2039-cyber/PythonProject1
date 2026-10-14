# step 1 is the blueprnt parent class
# step 2 is the electrc branch child class
# step 3 is the gas branch child class
# step 4 is putting them together
# super(). __init__(make, model)
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.starting_speed = 0
    def display_info(self):
        print(f"Vehicle: {self.make} | {self.model} | Speed: {self.starting_speed} mph")

    def accelerate(self, amount):
        self.starting_speed += amount
        print(f"🚘 {self.model} accelerated by {amount} mph. New speed: {self.starting_speed} mph")

class ElectricVehicle(Vehicle):
    def __init__(self, make, model, battery_level= 100):
        super(). __init__(make, model)
        self.battery_level = battery_level


    def charge_battery(self):
        self.battery_level = 100
        print(f"Charging.. The {self.model}'s battery is now fully charged to 100%")


class GasVehicle(Vehicle):
    def __init__(self, make, model, fuel_level = 100):
        super(). __init__(make, model)
        self.fuel_level = fuel_level

    def refuel_tank(self):
        self.fuel_level = 100
        print(f"Refueling... The {self.model}'s gas tank is now filled to 100%")

myev = ElectricVehicle("Ford", "S class")
myev.display_info()
myev.charge_battery()
my_engine_powered_car = GasVehicle("Ford", "Z class")
my_engine_powered_car.display_info()
my_engine_powered_car.refuel_tank()
myev.accelerate(40)
my_engine_powered_car.accelerate(50)
# Key concepts to takeaway:
# Parent Blueprinting
# Inheritance Extension
# Shared Behavior