""" Selection sort algorithm implementation in Python.

The selection sort improves on the bubble sort by making only one
exchange for every pass through the list. In order to do this, a
selection sort looks for the largest value as it makes a pass and,
after completing the pass, places it in the proper location.
"""
from typing import TypeVar


T = TypeVar("T")


def selection_sort(lst: list[T]):
    """Selection sort algorithm, O(n^2)."""
    for i, item in enumerate(lst):
        min_idx = len(lst) - 1
        for j in range(i, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j

        if min_idx != i:
            lst[min_idx], lst[i] = lst[i], lst[min_idx]


def main():
    lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selection_sort(lst)
    print(lst)


if __name__ == "__main__":
    main()
