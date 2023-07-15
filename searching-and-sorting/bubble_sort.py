from typing import TypeVar


T = TypeVar("T")


def bubble_sort(lst: list[T]):  # O(n2)
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                # simultaneous assignment swap
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def bubble_sort_short(lst: list[T]):
    for i in range(len(lst) - 1, 0, -1):
        exchanges = False

        for j in range(i):
            if lst[j] > lst[j + 1]:
                exchanges = True
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            if not exchanges:
                break


lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(lst)
print(lst)

lst = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
bubble_sort_short(lst)
print(lst)
