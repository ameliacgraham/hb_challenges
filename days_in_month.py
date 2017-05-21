def is_leap_year(year):
    """Is this year a leap year?"""

    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True

    return False


def days_in_month(date):
    """How many days are there in a month?"""

    month = int(date.split()[0])
    year = int(date.split()[1])
    leap = is_leap_year(year)
    thirty_days = {"04", "06", "09", "11"}
    thirty_one_days = {"01", "03", "05", "07", "08", "10", "12"}

    if month in thirty_days:
        return 30
    elif month in thirty_one_days:
        return 31
    elif month == 02 and leap:
        return 29
    else:
        return 28

print days_in_month("02 2016")
