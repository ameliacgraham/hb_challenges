def print_digits(num):
    """Given int, print digits in reverse order, starting with the ones place."""
    while num:
        print num % 10,
        num = num / 10

print_digits(462)
