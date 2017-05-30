from random import choice
def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive)."""

    nums = range(1,11)
    random_nums = []
    for i in range(n):
        number = choice(nums)
        random_nums.append(number)
        nums.remove(number)

    return random_nums

print lucky_numbers(10)
