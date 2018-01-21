from datetime import date

def is_payday_leap_year(year, payday, frequency='biweekly'):
    """Determine if a given year is a payday leap year.

    Determine if a given year is a payday leap year, based on the
    given payday on a weekly or biweekly pay calendar (specified by
    `frequency`). Assumes paychecks are allowed to be disbursed
    on holidays.

    Args:
        year (int): The year we're testing.
        payday (date): A payday from the biweekly pay calendar.
            Does not need to be in the same year as `year`.
        frequency (str): Pay frequency. Valid values are 'weekly'
            or 'biweekly'. Default is 'biweekly'.

    Returns:
        True if the year is a 27 payday year, False if not.
    """
    new_years_day = date(year, 1, 1)
    freq_in_days = 7 if frequency == 'weekly' else 14
    # Determine if new year's day is a payday.
    # If new year's day is a payday, then it's always a 27 payday year.
    if abs((payday - new_years_day).days) % freq_in_days == 0:
        result = True
    # Handle leap years - Jan. 2 can also be a payday.
    elif (year % 4 == 0) and (abs((payday - date(year, 1, 2)).days) % freq_in_days == 0):
        result = True
    else:
        result = False
    return result
