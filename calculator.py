from datetime import date

def is_27_payday_year(year, payday):
    """Determine if a given year is a 27 payday year.

    Determine if a given year is a 27 payday year, based on the given
    payday on a biweekly pay calendar. Assumes paychecks are disbursed
    on holidays.

    Args:
        year (int): The year we're testing.
        payday (date): A payday from the biweekly pay calendar.
            Does not need to be in the same year as `year`.

    Returns:
        True if the year is a 27 payday year, False if not.
    """
    new_years_day = date(year, 1, 1)
    # Determine if new year's day is a payday.
    # If new year's day is a payday, then it's always a 27 payday year.
    if abs((payday - new_years_day).days) % 14 == 0:
        result = True
    # Handle leap years - Jan. 2 can also be a payday.
    elif (year % 4 == 0) and (abs((payday - date(year, 1, 2)).days) % 14 == 0):
        result = True
    else:
        result = False
    return result

if __name__ == '__main__':
    year = 2018
    payday = date(2018, 1, 12)
    for i in range(51):
        print("{0} is a 27 payday year: {1}".format(
            year, is_27_payday_year(year, payday)
        ))
        year += 1
