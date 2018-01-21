import unittest
from datetime import date

from calculator import is_payday_leap_year

class CalculatorTestCase(unittest.TestCase):

    def test_thursday_2018_is_false(self):
        payday = date(2018, 1, 11)
        self.assertFalse(is_payday_leap_year(2018, payday))

    def test_thursday_2037_is_true(self):
        payday = date(2018, 1, 11)
        self.assertTrue(is_payday_leap_year(2037, payday))

    def test_thursday_2037_alternate_week_is_false(self):
        payday = date(2018, 1, 4)
        self.assertFalse(is_payday_leap_year(2037, payday))

    def test_friday_2038_is_true(self):
        payday = date(2018, 1, 12)
        self.assertTrue(is_payday_leap_year(2038, payday))

    def test_thursday_2015_weekly_is_true(self):
        payday = date(2018, 1, 11)
        self.assertTrue(is_payday_leap_year(2015, payday, 'weekly'))

    def test_unique_weekly_year(self):
        payday = date(2018, 1, 11)
        # 2020 is not a payday leap year for the biweekly frequency.
        self.assertTrue(is_payday_leap_year(2020, payday, 'weekly'))

    def test_invalid_year_raises_TypeError(self):
        payday = (2017, 10, 19)
        self.assertRaises(TypeError, is_payday_leap_year, 'not_an_int', payday)

    def test_invalid_payday_raises_TypeError(self):
        self.assertRaises(TypeError, is_payday_leap_year, 2018, 'not_a_date')

    def test_invalid_frequency_defaults_to_14(self):
        payday = date(2018, 1, 11)
        # Should default to biweekly - 2015 will be valid.
        self.assertTrue(is_payday_leap_year(2015, payday, 'not_valid'))
        # Would be True for weekly - checking this doesn't happen.
        self.assertFalse(is_payday_leap_year(2020, payday, 'not_valid'))

if __name__ == '__main__':
    unittest.main(verbosity=2)
