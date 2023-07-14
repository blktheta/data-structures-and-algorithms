def list_sum(num_list: list[int]) -> int:
    the_sum = 0
    for i in num_list:
        the_sum = the_sum + i
    return the_sum


print(list_sum([1, 3, 5, 7, 9]))

"""
Compute the sum of a list of numbers without using while or for loops
total = (1 + (3 + (5 + (7 + 9))))
total = (1 + (3 + (5 + 16)))
total = (1 + (3 + 21))
total = (1 + 24)
total = 25
"""


def list_sum_recursion(num_list: list[int]) -> int:
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum_recursion(num_list[1:])


print(list_sum_recursion([1, 3, 5, 7, 9]))

"""
The 3 Laws of Recursion

    A recursive algorithm must have a base case.

    A recursive algorithm must change its state and move toward the base case.

    A recursive algorithm must call itself recursively.
"""

"""
Extra: Convert Integer to String in Any Base
"""


def to_str(n: int) -> str:
    convert_string = "0123456789"
    if n < 10:
        return convert_string[n]
    else:
        return to_str(n // 10) + convert_string[n % 10]


print(to_str(1253))
