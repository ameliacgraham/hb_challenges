def max_of_three(num1, num2, num3):
    """Returns the largest of three integers"""

    numbers = [num1, num2, num3]

    max_num = None

    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num

print max_of_three(12, 21, 1)