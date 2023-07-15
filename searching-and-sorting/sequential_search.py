from typing import TypeVar


T = TypeVar("T")


def sequential_search(lst: list[T], item: T) -> bool:
    pos = 0

    while pos < len(lst):
        if lst[pos] == item:
            return True
        pos = pos + 1
    return False


test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequential_search(test_list, 3))  # False
print(sequential_search(test_list, 13))  # True


def ordered_sequential_search(lst: list[T], item: T) -> bool:
    pos = 0

    while pos < len(lst):
        if lst[pos] == item:
            return True

        if lst[pos] > item:
            return False
        pos = pos + 1
    return False


test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(ordered_sequential_search(test_list, 3))  # False
print(ordered_sequential_search(test_list, 13))  # True
