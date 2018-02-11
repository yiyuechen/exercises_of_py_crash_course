# based on 9-3.py, 9-5.py

class User():
    def __init__(self, first, last, age, location):
        self.first_name = first
        self.last_name = last
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print("First Name: " + self.first_name)
        print("Last Name: " + self.last_name)
        print("Age: " + str(self.age))
        print("Location: " + self.location)
        print("Login Attempts: " + str(self.login_attempts))

    def greet_user(self):
        print("Hello " + self.first_name + " " + self.last_name)

    def increment_login_attempts(self, increment_time=1):
        if increment_time == 1:
            self.login_attempts += 1
        else:
            self.login_attempts += increment_time

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first, last, age, location):
        super().__init__(first, last, age, location)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Admin ")
        for privilege in self.privileges:
            print(" " + privilege)


victor = User("Vic", "Darcy", 21, "London")
victor.describe_user()
print("----------------------------")
victor.greet_user()

print("\n4 increments\n")
victor.increment_login_attempts(3)
victor.increment_login_attempts()
victor.describe_user()

print("\nResetting login attempts...\n")

victor.reset_login_attempts()

print("Now attribute login_attempts is: " + str(victor.login_attempts))

print("\n\n")

new_admin = Admin("Jane", "Eyre", "21", "England")
new_admin.show_privileges()
