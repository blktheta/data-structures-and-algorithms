"""
Calculate the Sum of a List of Nombers.

Calculate the sum of a list of numbers such as: [1, 3, 5, 7, 9].

Solve the problem first by using while or for loops, then after
make use of recursion:

Steps taken during recursion:
total = (1 + (3 + (5 + (7 + 9))))
total = (1 + (3 + (5 + 16)))
total = (1 + (3 + 21))
total = (1 + 24)
total = 25

The steps above can be stated in functional form as:

    list_sum(num_list) = first(num_list) + list_sum(rest(num_list))
"""
def list_sum(num_list: list[int]) -> int:
    """Compute the sum of all number in the list with a for loop

    the_sum: accumulator variable
    """
    the_sum = 0
    for i in num_list:
        the_sum = the_sum + i
    return the_sum


def list_sum_recursion(num_list: list[int]) -> int:
    """Compute the sum of all numbers in the list.

    Base case: list of length 1
    State change: call the function again with a shorter list
    """
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum_recursion(num_list[1:])


def main():
    print(list_sum([1, 3, 5, 7, 9]))
    print(list_sum_recursion([1, 3, 5, 7, 9]))


if __name__ == "__main__":
    main()
