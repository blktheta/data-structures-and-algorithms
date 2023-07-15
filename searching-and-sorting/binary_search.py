from typing import TypeVar


T = TypeVar("T")


def binary_search(lst: list[T], item: T) -> bool:
    first = 0
    last = len(lst) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if lst[midpoint] == item:
            return True
        elif item < lst[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return False


test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(test_list, 3))  # False
print(binary_search(test_list, 13))  # True


def binary_search_recursion(lst: list[T], item: T) -> bool:
    """
    Note: Slicing in Python is O(k).
    In order for a bineary search using recursion to be O(log n)
    the slicing needs to be constant time. This can be done by
    providing the list along with the starting and ending indices.
    """
    if len(lst) == 0:
        return False
    midpoint = len(lst) // 2
    if lst[midpoint] == item:
        return True
    elif item < lst[midpoint]:
        return binary_search_recursion(lst[:midpoint], item)
    else:
        return binary_search_recursion(lst[midpoint + 1:], item)


test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(test_list, 3))  # False
print(binary_search(test_list, 13))  # True
