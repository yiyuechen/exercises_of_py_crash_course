from car import Car

my_new_car = Car('audi','a4',2016)
name = my_new_car.get_descriptive_name()
print(name)

my_new_car.update_odometer(20)
my_new_car.read_odometer()
my_new_car.update_odometer(0)