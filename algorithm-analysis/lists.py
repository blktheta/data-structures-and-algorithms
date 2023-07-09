from timeit import Timer


def test1():
    """
    Extend the list using concatination.
    """
    lst = []
    for i in range(1000):
        lst = lst + [i]


def test2():
    """
    Extend the list using append method.
    """
    lst = []
    for i in range(1000):
        lst.append(i)


def test3():
    """
    Extend the list using list comprehension.
    """
    lst = [i for i in range(1000)]


def test4():
    """
    Extend the list using list range.
    """
    lst = list(range(1000))


x = list(range(2000000))
y = list(range(2000000))


def test5(x):
    """
    Pop from the start of the list.
    """
    pop_zero = Timer("x.pop(0)", "from __main__ import x")
    print(f"pop(0): {pop_zero.timeit(number=1000):10.5f} milliseconds")


def test6(y):
    """
    Pop from the end of the list.
    """
    pop_end = Timer("y.pop()", "from __main__ import y")
    print(f"pop(): {pop_end.timeit(number=1000):11.5f} milliseconds")


def main():
    t1 = Timer("test1()", "from __main__ import test1")
    print(f"concatenation: {t1.timeit(number=1000):15.2f} milliseconds")

    t2 = Timer("test2()", "from __main__ import test2")
    print(f"appending: {t2.timeit(number=1000):19.2f} milliseconds")

    t3 = Timer("test3()", "from __main__ import test3")
    print(f"list comprehension: {t3.timeit(number=1000):10.2f} milliseconds")

    t4 = Timer("test4()", "from __main__ import test4")
    print(f"list range: {t4.timeit(number=1000):18.2f} milliseconds")

    """
    Big O Efficiency of Python List Operators
    O(1):   index []
    O(1):   index assignment
    O(1):   index assignment
    O(1):   append
    O(1):   pop()
    O(n):   pop(i)
    O(n):   insert(i, item)
    O(n):   del operator
    O(n):   iteration
    O(n):   contains (in)
    O(k):   get slice [x:y]
    O(n):   del slice
    O(n+k): set slice
    O(n):   reverse
    O(k):   concatenate
    O(n log n):   sort
    O(nk):   multiply
    """

    test5(x)
    test6(y)


if __name__ == "__main__":
    main()
