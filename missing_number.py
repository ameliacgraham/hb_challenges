def missing_number_scan(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing."""

    # full = set(range(1, max_num))
    # missing = set(nums)
    # missing_num = list(full - missing)
    # return missing_num[0]

    expected = sum(range(max_num + 1))

    return expected - sum(nums)


print missing_number_scan([1, 2, 3, 4, 5, 6, 7, 9, 10], 10)



