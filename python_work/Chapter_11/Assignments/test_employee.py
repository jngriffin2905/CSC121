import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    

    def setUp(self):
        
        self.jessica = Employee('jessica', 'griffin', 65000)

    def test_give_default_raise(self):
        self.jessica.give_raise()
        self.assertEqual(self.jessica.salary, 70000)

    def test_give_custom_raise(self):
        self.jessica.give_raise(10000)
        self.assertEqual(self.jessica.salary, 75000)

unittest.main()