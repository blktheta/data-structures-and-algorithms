"""Insertion sort algorithm implementation in Python.

The insertion sort always maintains a sorted sublist in the lower
positions of the list. Each new item is then inserted back into the
previous sublist such that the sorted sublist is one item larger.
"""
from typing import TypeVar


T = TypeVar("T")


def insertion_sort(lst: list[T]):
    """Insertion sort algorithm, O(n^2)."""
    for i in range(1, len(lst)):
        cur_val = lst[i]
        cur_pos = i

        while (cur_pos > 0) and (lst[cur_pos - 1] > cur_val):
            lst[cur_pos] = lst[cur_pos - 1]
            cur_pos = cur_pos - 1
        lst[cur_pos] = cur_val


def main():
    lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertion_sort(lst)
    print(lst)


if __name__ == "__main__":
    main()
