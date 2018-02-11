from unittest import TestCase
from employee import Employee


class TestEmployee(TestCase):
    def setUp(self):
        # create a new employee object
        self.employee = Employee('Jane', 'Austin', 50000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 55000)

    def test_give_custom_raise(self):
        self.employee.give_raise(7000)
        self.assertEqual(self.employee.annual_salary, 57000)


"""If we change to the style in book"""
# import unittest
# from employee import Employee
#
#
# class TestEmployee(unittest.TestCase):
#
#     def test_give_default_raise(self):
#         self.employee = Employee('Jane', 'Austin', 50000)
#         self.employee.give_raise()
#         self.assertEqual(self.employee.annual_salary, 55000)
#
#     def test_give_custom_raise(self):
#         self.employee = Employee('Jane', 'Austin', 50000)
#         self.employee.give_raise(7000)
#         self.assertEqual(self.employee.annual_salary, 57000)
#
# if __name__ == "__main__":
#     unittest.main()
