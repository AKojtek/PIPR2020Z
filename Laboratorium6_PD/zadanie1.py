"""
Program finds the largest subarray using Kadane algorithm
"""


def find_largest_subarray(my_list):
    if not my_list:
        raise ValueError("Array cannot be empty")
    for x in my_list:
        int(x)
    max_local = max_total = my_list[0]
    for x in my_list[1:]:
        max_local = max(x, max_local + x)
        max_total = max(max_total, max_local)
    return max_total