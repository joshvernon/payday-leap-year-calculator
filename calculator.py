from datetime import date

def is_payday_leap_year(year, payday, frequency='biweekly'):
    """Determine if a given year is a payday leap year.

    Determine if a given year is a payday leap year, based on the
    given payday on a weekly or biweekly pay calendar (specified by
    `frequency`). Assumes paychecks are allowed to be disbursed
    on holidays.

    Args:
        year (int): The year we're testing.
        payday (date): A payday from the specified pay calendar.
            Does not need to be in the same year as `year`.
        frequency (str): Pay frequency. Valid values are 'weekly'
            or 'biweekly'. Default is 'biweekly'.

    Returns:
        True if the year is a payday leap year, False if not.
    """
    new_years_day = date(year, 1, 1)
    jan_2 = date(year, 1, 2)
    freq_in_days = 7 if frequency == 'weekly' else 14
    # Determine if new year's day is a payday.
    # If new year's day is a payday, then it's always a 27 payday year.
    if abs((payday - new_years_day).days) % freq_in_days == 0:
        result = True
    # Handle leap years - Jan. 2 can also be a payday.
    elif (year % 4 == 0) and (abs((payday - jan_2).days) % freq_in_days == 0):
        result = True
    else:
        result = False
    return result

def get_payday_leap_years(
    payday,
    frequency='biweekly',
    count=5,
    starting_year=date.today().year
):
    """Get the next n payday leap years.

    Return a list of the next n payday leap years, where n is specified
    by `count`.

    Args:
        payday (date): A payday from the specified pay calendar.
        frequency (str): Pay frequency. Valid values are 'weekly'
            or 'biweekly'. Default is 'biweekly'.
        count (int): The number of payday leap years to return. Default is 5.
        starting_year (int): The year to start counting from.

    Returns:
        A list of ints.
    """
    results = []
    # Start counting from the current year.
    year = starting_year
    while len(results) < count:
        if is_payday_leap_year(year, payday, frequency):
            results.append(year)
        year += 1
    return results

if __name__ == '__main__':
    year = 2018
    # January 11, 2018
    payday = date(2018, 1, 11)
    for i in range(51):
        print("{0} is a payday leap year: {1}".format(
            year, is_payday_leap_year(year, payday)
        ))
        year += 1
