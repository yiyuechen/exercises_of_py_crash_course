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
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describle_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        self.battery = Battery()
