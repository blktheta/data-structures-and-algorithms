from typing import TypeVar


T = TypeVar("T")


def quick_sort(lst: list[T]):  # O(n log n) if split point are close to middle
    quick_sort_helper(lst, 0, len(lst) - 1)


def quick_sort_helper(lst: list[T], first: int, last: int):
    if first < last:
        split = partition(lst, first, last)
        quick_sort_helper(lst, first, split - 1)
        quick_sort_helper(lst, split + 1, last)


def partition(lst: list[T], first: int, last: int) -> int:
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
    return sorted([a, b, c])[1]


lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(lst)
quick_sort(lst)
print(lst)
