from car import Car

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        self.battery = Battery()

    def upgrade_battery(self):
        if self.battery.battery_size < 85:
            self.battery.battery_size = 85
            print("Battery upgrated.")

class Battery():
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describle_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    # How far it can run. print range
    def get_range(self):
        if self.battery_size == 75:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "The car can go " + str(range) + " miles on a full charge."
        print(message)