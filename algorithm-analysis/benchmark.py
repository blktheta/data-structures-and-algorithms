import time


def sum_of_n_1(n: int) -> tuple:
    """
    Compute the sum of the first n integers.
    """
    start = time.time()
    the_sum = 0
    for i in range(1, n + 1):
        the_sum = the_sum + i

    end = time.time()
    return the_sum, end - start


def sum_of_n_2(n: int) -> tuple:
    """
    Compute the sum of the first n integers.

    This function however takes advantage of a closed equation to compute
    the sum of the first n integers without iterating.
    """
    start = time.time()
    the_sum = (n * (n + 1)) / 2

    end = time.time()
    return the_sum, end - start


def main():
    for i in range(5):
        print("Sum is %d required %10.7f seconds" % sum_of_n_1(100000))

    for i in range(5):
        print("Sum is %d required %10.7f seconds" % sum_of_n_2(100000))

    """
    The benchmark reveal that the iterative solution seem to be doing
    much more work since some program steps are being repeated.

    Also, the time required for the iterative solution seems to increase
    as we increase the value of n.
    """


if __name__ == "__main__":
    main()
