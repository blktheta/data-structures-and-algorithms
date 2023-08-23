""" Shell sort algorithm implementation in Python.

The Shell sort, sometimes called the diminishing increment sort,
improves on the insertion sort by breaking the original list into a
number of smaller sublists, each of which is sorted using an insertion
sort. The unique way that these sublists are chosen is the key to the
Shell sort. Instead of breaking the list into sublists of contiguous
items, the Shell sort uses an increment (i), sometimes called the gap, to
create a sublist by choosing all items that are (i) items apart.
"""
from typing import TypeVar


T = TypeVar("T")


def shell_sort(lst: list[T]):  # O(n) - O(n2)
    """Shell sort algorithm, between O(n) and O(n^2)."""
    sublist_count = len(lst) // 2
    while sublist_count > 0:
        for pos_start in range(sublist_count):
            gap_insertion_sort(lst, pos_start, sublist_count)
        print(f"After increments of size {sublist_count} the list is {lst}")
        sublist_count = sublist_count // 2


def gap_insertion_sort(lst: list[T], start: int, gap: int):
    """Sublist sorting based on incremental value."""
    for i in range(start + gap, len(lst), gap):
        cur_val = lst[i]
        cur_pos = i

        while (cur_pos >= gap) and (lst[cur_pos - gap] > cur_val):
            lst[cur_pos] = lst[cur_pos - gap]
            cur_pos = cur_pos - gap
        lst[cur_pos] = cur_val


def main():
    lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(lst)
    shell_sort(lst)
    print(lst)


if __name__ == "__main__":
    main()
