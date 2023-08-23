""" Binary search algorithm.

A binary search will start by examining the middle item. If that item
is the one it is searching for, it is done. If it is not the correct
item, it can use the ordered nature of the list to eliminate half of
the remaining items.

If the item it is searching for is greater than the middle item, it
knows that the entire first (left) half of the list as well as the
middle item can be eliminated from further consideration. The item,
if it is in the list, must be in the second (right) half.
"""
from typing import TypeVar


T = TypeVar("T")


def binary_search(lst: list[T], item: T) -> bool:
    """Binary search algorithm."""
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



def binary_search_rec(lst: list[T], item: T) -> bool:
    """Binary search algorithm using recursion.

    Note: Slicing in Python is O(k).
    In order for a binary search using recursion to be O(log n)
    the slicing needs to be constant time. This can be done by
    passing the list along with the starting and ending indices.
    """
    if len(lst) == 0:
        return False
    midpoint = len(lst) // 2
    if lst[midpoint] == item:
        return True
    elif item < lst[midpoint]:
        return binary_search_rec(lst[:midpoint], item)
    else:
        return binary_search_rec(lst[midpoint + 1:], item)


def main():
    test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search(test_list, 3))          # False
    print(binary_search(test_list, 13))         # True

    print(binary_search_rec(test_list, 3))      # False
    print(binary_search_rec(test_list, 13))     # True


if __name__ == "__main__":
    main()
