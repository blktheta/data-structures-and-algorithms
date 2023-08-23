""" Merge sort algorithm implementation in Python.

Merge sort is a recursive algorithm that continually splits a list in
half. If the list is empty or has one item, it is sorted by definition
(the base case). If the list has more than one item, we split the list
and recursively invoke a merge sort on both halves. Once the two halves
are sorted, the fundamental operation, called a merge, is performed.
Merging is the process of taking two smaller sorted lists and combining
them together into a single sorted new list.
"""
from typing import TypeVar


T = TypeVar("T")


def merge_sort(lst: list[T]):
    """Merge sort algorithm, O(n log n).

    Note: Python slicing is O(k)
    """
    print("Splitting", lst)
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0
        while (i < len(left_half)) and (j < len(right_half)):
            # stable algorithm maintains order of duplicated items
            if left_half[i] <= right_half[j]:
                lst[k] = left_half[i]
                i = i + 1
            else:
                lst[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            lst[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            lst[k] = right_half[j]
            j = j + 1
            k = k + 1
    print("Merging", lst)


def main():
    lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    merge_sort(lst)
    print(lst)


if __name__ == "__main__":
    main()
