# Based on 9-1.py, add a variable named number_served
# Based on 9-4_number_served.py, create an IceCream Store

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


class IceCreamStand(Restaurant):
    def __init__(self, name, type):
        super(IceCreamStand, self).__init__(name, type)
        self.flavors = ['blueberry', 'orange', 'strawberry', 'pure']

    def show_ice_creams(self):
        print("We offer the following flavors: ")
        for flavor in self.flavors:
            print("- " + flavor)


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

print("\n\n")
mclaclin_iceCream = IceCreamStand("Mclaclin's", "Top IceCreamStand")
mclaclin_iceCream.show_ice_creams()
