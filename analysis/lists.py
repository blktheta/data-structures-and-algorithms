"""
Big O performance cost for Pyhton lists operations.
"""
from timeit import Timer


def list_con():
    """
    Extend the list using concatination, O(k).
    """
    lst = []
    for i in range(1000):
        lst = lst + [i]


def list_app():
    """
    Extend the list using append method, O(1).
    """
    lst = []
    for i in range(1000):
        lst.append(i)


def list_com():
    """
    Extend the list using list comprehension.

    The list comprehension doesn't need to load the append attribute of
    the list and call it as a function at each iteration.
    """
    lst = [i for i in range(1000)]


def list_rng():
    """
    Extend the list using list range.
    """
    lst = list(range(1000))


x = list(range(2000000))
y = list(range(2000000))


def main():
    """
    Big O Efficiency of Python List Operators
    O(1):       index []
    O(1):       index assignment
    O(1):       index assignment
    O(1):       append
    O(1):       pop()
    O(n):       pop(i)
    O(n):       insert(i, item)
    O(n):       del operator
    O(n):       iteration
    O(n):       contains (in)
    O(k):       get slice [x:y]
    O(n):       del slice
    O(n+k):     set slice
    O(n):       reverse
    O(k):       concatenate
    O(n log n): sort
    O(nk):      multiply
    """
    t1 = Timer("list_con()", "from __main__ import list_con")
    print(f"Concatenation: {t1.timeit(number=1000):15.2f} milliseconds")

    t2 = Timer("list_app()", "from __main__ import list_app")
    print(f"Appending: {t2.timeit(number=1000):19.2f} milliseconds")

    t3 = Timer("list_com()", "from __main__ import list_com")
    print(f"List comprehension: {t3.timeit(number=1000):10.2f} milliseconds")

    t4 = Timer("list_rng", "from __main__ import list_rng")
    print(f"List range: {t4.timeit(number=1000):18.2f} milliseconds")

    # Pop from the start of the list.
    t5 = Timer("x.pop(0)", "from __main__ import x")
    print(f"pop(0): {t5.timeit(number=1000):10.5f} milliseconds")

    # Pop from the end of the list.
    t6 = Timer("y.pop()", "from __main__ import y")
    print(f"pop(): {t6.timeit(number=1000):11.5f} milliseconds")


if __name__ == "__main__":
    main()
