def is_leap_year(year):
    """
    find the leap year
    :param year: integer
    :return: Boolean
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Calling function with hard coded year
output = is_leap_year(1900)
print(output)