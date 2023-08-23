""" Quicksort algorithm implementation in Python.

The quicksort uses divide and conquer to gain the same advantages as
the merge sort, while not using additional storage. As a trade-off,
however, it is possible that the list may not be divided in half.
When this happens, we will see that performance is diminished.

A quicksort first selects a value, which is called the pivot value.
Although there are many different ways to choose the pivot value, we
will simply use the first item in the list. The role of the pivot
value is to assist with splitting the list. The actual position where
the pivot value belongs in the final sorted list, commonly called the
split point, will be used to divide the list for subsequent calls to
the quicksort.
"""
from typing import TypeVar


T = TypeVar("T")


def quick_sort(lst: list[T]):
    """Quicksort wrapper."""
    quick_sort_helper(lst, 0, len(lst) - 1)


def quick_sort_helper(lst: list[T], first: int, last: int):
    """Recursive call for the algorithm to be partitioned."""
    if first < last:
        split = partition(lst, first, last)
        quick_sort_helper(lst, first, split - 1)
        quick_sort_helper(lst, split + 1, last)


def partition(lst: list[T], first: int, last: int) -> int:
    """Quicksort algorithm logic, O(n log n).

    Note: efficiency stays true if the split point is close to middle.
    """
    # Help pick a better pivotal value
    pivot_val = median_of_three(lst[first], lst[(first + last) // 2], lst[last])
    left_mark = first + 1
    right_mark = last
    done = False

    while not done:
        while (left_mark <= right_mark) and (lst[left_mark] <= pivot_val):
            left_mark = left_mark + 1
        while (left_mark <= right_mark) and (lst[right_mark] >= pivot_val):
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            lst[left_mark], lst[right_mark] = lst[right_mark], lst[left_mark]
    lst[first], lst[right_mark] = lst[right_mark], lst[first]

    return right_mark


def median_of_three(a: int, b: int, c: int) -> T:
    """Technique to alleviate uneven division of the pivotal value."""
    return sorted([a, b, c])[1]


def main():
    lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(lst)
    quick_sort(lst)
    print(lst)


if __name__ == "__main__":
    main()
