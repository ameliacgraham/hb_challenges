def max_num(num_list):
    """Returns largest integer from given list"""

    num_list.sort()
    return num_list[-1]

# def max_num(num_list):
#     """Returns largest integer from given list"""

#     max = None
#     for num in num_list:
#         if num > max:
#             max = num
#     return max

print max_num([4,5,1,6,7,3])