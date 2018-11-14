import unittest
from datetime import date

from calculator import is_payday_leap_year, get_payday_leap_years


class IsPaydayLeapYearTestCase(unittest.TestCase):
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


class GetPaydayLeapYearsTestCase(unittest.TestCase):
    def test_7_26_2018_returns_correct_years(self):
        payday = date(2018, 7, 26)
        expected = [2026, 2037, 2048, 2060, 2071]
        results = get_payday_leap_years(payday)
        self.assertEqual(results, expected)
    
    def test_7_26_2018_returns_correct_years_weekly_frequency(self):
        payday = date(2018, 7, 26)
        expected = [2020, 2026, 2032, 2037, 2043]
        results = get_payday_leap_years(payday, frequency='weekly')
        self.assertEqual(results, expected)

    def test_non_default_count(self):
        payday = date(2018, 7, 26)
        results = get_payday_leap_years(payday, count=10)
        self.assertEqual(len(results), 10)

    def test_zero_count_returns_empty_result_set(self):
        payday = date(2018, 7, 26)
        results = get_payday_leap_years(payday, count=0)
        self.assertEqual(len(results), 0)

    def test_non_default_starting_year(self):
        payday = date(2018, 7, 26)
        results = get_payday_leap_years(payday, starting_year=2000)
        self.assertIn(2004, results)

if __name__ == '__main__':
    unittest.main(verbosity=2)
