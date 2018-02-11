class User():
    def __init__(self, first, last, age, location):
        self.first_name = first
        self.last_name = last
        self.age = age
        self.location = location

    def describe_user(self):
        print("First Name: " + self.first_name)
        print("Last Name: " + self.last_name)
        print("Age: " + str(self.age))
        print("Location: " + self.location)

    def greet_user(self):
        print("Hello " + self.first_name + " " + self.last_name)


victor = User("Vic", "Darcy", 21, "London")
victor.describe_user()
print("----------------------------")
victor.greet_user()
