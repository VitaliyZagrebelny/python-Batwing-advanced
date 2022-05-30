import unittest
from employee import Employee
from unittest.mock import patch


class TestEmployee(unittest.TestCase):
    def test_name(self):
        self.test_info = Employee('Vitali', 'Zahrebelnyi', 1000)

    def test_email(self):
        self.assertEqual(self.test_info.email, 'vitalii@gmail.com')

    def test_fullname(self):
        self.assertEqual(self.test_info.fullname, 'Vitali Zahrebelnyi')

    def test_apply_raise(self):
        self.test_info.apply_raise()
        self.assertEqual(self.test_info.pay, 150)

    @patch("employee.Employee.monthly_schedule")
    def test_monthly_schedule(self, mockCheck):
        self.maxDiff = None
        value = Employee("Vasya", "Pop", 456)
        mockCheck.return_value = 'Bad Response!'
        self.assertNotEqual(value.monthly_schedule(12), value.func_for_compare())
