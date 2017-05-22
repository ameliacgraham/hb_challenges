def find_range(nums):
    """Given list of numbers, return smallest & largest number as a tuple."""


    if len(nums) == 0:
        return (None, None)

    min = nums[0]
    max = nums[0]

    for num in nums:
        if num > max:
            max = num
        if num < min:
            min = num

    return (min, max)

print find_range([1, 2, 4, 5, 7])