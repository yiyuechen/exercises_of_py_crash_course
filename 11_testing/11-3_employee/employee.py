class Employee():
    def __init__(self, first, last, annual_salary):
        self.first = first
        self.last = last
        self.annual_salary = annual_salary

    def give_raise(self, raise_size=5000):
        self.annual_salary += raise_size

# obj = Employee('jane','eyre', 10000)
# salary = obj.give_raise()
# print(salary)
