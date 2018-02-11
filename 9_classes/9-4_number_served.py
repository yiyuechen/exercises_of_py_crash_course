# Based on 9-1.py, add a variable named number_served

class Restaurant():
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant Name: " + self.restaurant_name)
        print("Cuisine Type: " + self.cuisine_type)
        print("Number Served: " + str(self.number_served))

    def open_restaurant(self):
        print("We are open.")

    def set_number_served(self, value):
        if value >= self.number_served:
            self.number_served = value
        else:
            print("Error!")

    def increment_number_served(self, value):
        if value > 0:
            self.number_served += value
        else:
            print("increment should be positive here.")


restaurant = Restaurant("Fine Rest", "A plus")
restaurant.describe_restaurant()
restaurant.open_restaurant()
# add served number
print("Adding served number: ")
restaurant.set_number_served(10)
restaurant.describe_restaurant()

print("\n")

# increment
print("Increment")
restaurant.increment_number_served(20)
restaurant.describe_restaurant()
