"""Sequential search algorithm implementation in Python.

The algorithm start at the first tiem in the list and moves from item
to item, it follows the underlying sequential order until it either
find what it was looking for or run out of items, which would mean the
item it was searching for was not present.
"""
from typing import TypeVar


T = TypeVar("T")


def sequential_search(lst: list[T], item: T) -> bool:
    """Sequential search algorithm."""
    pos = 0

    while pos < len(lst):
        if lst[pos] == item:
            return True
        pos = pos + 1
    return False


def ordered_sequential_search(lst: list[T], item: T) -> bool:
    """Sequential search optimization for ordered lists.

    The algorithm exits the search if it passes the position of the
    item it was searching for.
    """
    pos = 0

    while pos < len(lst):
        if lst[pos] == item:
            return True

        if lst[pos] > item:
            return False
        pos = pos + 1
    return False


def main():
    test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(sequential_search(test_list, 3))                  # False
    print(sequential_search(test_list, 13))                 # True

    test_list_ord = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(ordered_sequential_search(test_list_ord, 3))      # False
    print(ordered_sequential_search(test_list_ord, 13))     # True


if __name__ == "__main__":
    main()
