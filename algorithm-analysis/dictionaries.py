import timeit

import random


"""
Compare the contains (in) operator of lists and dictionaries.

The implemantation should confirm that:

    - The contains operator for lists is O(n)
    - The contains operator for dictionaries is O(1)

Big O Efficiency of Python List Operators
O(n):   copy
O(1):   get item
O(1):   set item
O(1):   delete item
O(1):   contains (in)
O(n):   iteration
"""

print(f"{'n':10s}{'list':>10s}{'dict':>10s}")

for i in range(10_000, 1_000_001, 20_000):

    t = timeit.Timer(f"random.randrange({i}) in x", "from __main__ import random, x")

    x = list(range(i))

    lst_time = t.timeit(number=1000)

    x = {j: None for j in range(i)}

    dict_time = t.timeit(number=1000)

    print(f"{i:<10,}{lst_time:>10.3f}{dict_time:>10.3f}")
