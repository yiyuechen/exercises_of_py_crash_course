""" c class for car"""


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " on it.")

    def update_odometer(self, mileage):
        if self.odometer_reading <= mileage:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back an odometer.")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


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
