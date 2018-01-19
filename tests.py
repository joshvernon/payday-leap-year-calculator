import unittest
from datetime import date

from calculator import is_27_payday_year

class CalculatorTestCase(unittest.TestCase):

    def test_thursday_2018_is_false(self):
        payday = date(2018, 1, 11)
        self.assertFalse(is_27_payday_year(2018, payday))

    def test_thursday_2037_is_true(self):
        payday = date(2018, 1, 11)
        self.assertTrue(is_27_payday_year(2037, payday))

    def test_thursday_2037_alternate_week_is_false(self):
        payday = date(2018, 1, 4)
        self.assertFalse(is_27_payday_year(2037, payday))

    def test_friday_2038_is_true(self):
        payday = date(2018, 1, 12)
        self.assertTrue(is_27_payday_year(2038, payday))

    def test_invalid_year_raises_TypeError(self):
        payday = (2017, 10, 19)
        self.assertRaises(TypeError, is_27_payday_year, 'not_an_int', payday)

    def test_invalid_payday_raises_TypeError(self):
        self.assertRaises(TypeError, is_27_payday_year, 2018, 'not_a_date')

if __name__ == '__main__':
    unittest.main(verbosity=2)
