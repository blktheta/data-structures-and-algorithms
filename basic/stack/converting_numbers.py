"""
Method: Stack
Example: Converting decimal numbers to binary numbers

Algorithm that that continually divides the decimal number by 2 and
keeps track of the remainder.

The first division by 2 gives information as to whether the value is
even or odd. An even value will have a remainder of 0 and will have the
digit 0 in the ones place. An odd value will have a remainder of 1 and
will have the digit 1 in the ones place

The first remainder that computed will be the last digit in
the sequence:
                                                          Pop top->btm
    233 // 2 = 116                              rem = 1     rem = 1
        116 // 2 = 58                           rem = 0     rem = 1
            58 // 29 = 29                       rem = 0     rem = 1
                29 // 2 = 14                    rem = 1     rem = 0
                    14 // 2 = 7                 rem = 0     rem = 1
                        7 // 2 = 3              rem = 1     rem = 0
                            3 // 2 = 1          rem = 1     rem = 0
                                1 // 2 = 0      rem = 1     rem = 1
                                             Push btm->top
Output: 11101001
"""
from stack import Stack


def divide_by_2(decimal_num: int) -> str:
    """Converts decimal numbers to binary numbers."""
    rem_stack = Stack()

    while decimal_num > 0:
        rem = decimal_num % 2
        rem_stack.push(rem)
        decimal_num = decimal_num // 2

    bin_string = ""
    while not rem_stack.is_empty():
        bin_string = bin_string + str(rem_stack.pop())

    return bin_string


def base_converter(decimal_num:int, base: int) -> str:
    """Modified 'divide_by_2() function.

    Converts decimal number to a sequence from any value between 1-16.

    Note that a remainder above 9 can not be used as they themselves
    represent two-digit decimal numbers. Instead we need to create a
    set of digits that can be used to represent those remainders
    beyond 9.

    The solution is to extend the digit set to include som alphabet
    characters, similarly to how hexadecimal uses the ten decimal digits
    along with the first six alphabet characters for the 16 digits.
    """
    digits ="0123456789ABCDEF"
    rem_stack = Stack()

    while decimal_num > 0:
        rem = decimal_num % base
        rem_stack.push(rem)
        decimal_num = decimal_num // base

    new_string = ""
    while not rem_stack.is_empty():
        new_string = new_string + digits[rem_stack.pop()]

    return new_string

def main():
    print(divide_by_2(233))
    print(divide_by_2(42))
    print(divide_by_2(31))
    print(base_converter(25, 2))
    print(base_converter(25, 16))


if __name__ == "__main__":
    main()
