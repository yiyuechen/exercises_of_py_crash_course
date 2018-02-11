class Restaurant():
    def __init__(self, name, type):
        self.restaurant_name=name
        self.cuisine_type=type

    def describe_restaurant(self):
        print("Restaurant Name: "+self.restaurant_name)
        print("Cuisine Type: "+self.cuisine_type)

    def open_restaurant(self):
        print("We are open.")