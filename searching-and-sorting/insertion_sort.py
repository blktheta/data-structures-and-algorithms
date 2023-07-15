from typing import TypeVar


T = TypeVar("T")


def insertion_sort(lst: list[T]):  # O(n2)
    for i in range(1, len(lst)):
        cur_val = lst[i]
        cur_pos = i

        while (cur_pos > 0) and (lst[cur_pos - 1] > cur_val):
            lst[cur_pos] = lst[cur_pos - 1]
            cur_pos = cur_pos - 1
        lst[cur_pos] = cur_val


lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(lst)
print(lst)
