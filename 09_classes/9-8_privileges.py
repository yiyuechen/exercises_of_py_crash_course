class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Admin ")
        for privilege in self.privileges:
            print(" " + privilege)


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


class Admin(User):
    def __init__(self, first, last, age, location):
        super().__init__(first, last, age, location)
        self.privileges = Privileges()


admin_0 = Admin("Viola", "Darcy", 20, "London")
admin_0.privileges.show_privileges()
