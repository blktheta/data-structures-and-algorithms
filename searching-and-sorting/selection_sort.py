
from typing import TypeVar


T = TypeVar("T")


def selection_sort(lst: list[T]):  # O(n2)
    for i, item in enumerate(lst):
        min_idx = len(lst) - 1
        for j in range(i, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j

        if min_idx != i:
            lst[min_idx], lst[i] = lst[i], lst[min_idx]


lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(lst)
print(lst)
