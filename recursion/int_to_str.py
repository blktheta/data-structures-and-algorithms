"""
Convert an Integer to a String in Any Base

Suppose you hwasnt to convert an integer to a strin in any base
between binary and hexadecimal.

Example:    Convert integer 10 to its string representation in
            decimal as "10", or to its string representation in
            binary as "1010".

Suppose we have a sequence of characters corresponding to the first
10 digits, like convert_string = "0123456789". It is easy to convert
a number less than 10 to its string equivalent by looking it up in
the sequence. For example, if the number is 9, then the string is
convert_string[9] or "9".

Knowing what our base is suggests that the overall algorithm will
involve three components:

1. Reduce the original number to a series of single-digit numbers.
2. Convert the single digit-number to a string using a lookup.
3. Concatenate the single-digit strings together to form the final result.

"""
from stack import Stack

def to_str_basic(n: int) -> str:
    """Convert integer to string."""
    convert_string = "0123456789"
    if n < 10:
        return convert_string[n]
    else:
        return to_str_basic(n // 10) + convert_string[n % 10]


def to_str(n:int, base: int) -> str:
    """Convert interger to string in any base."""
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_str(n // base, base) + convert_string[n % base]


def to_str_stack(n:int, base: int) -> str:
    """Modified integer to string convertion using stack."""
    r_stack = Stack()
    convert_string = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            r_stack.push(convert_string[n])
        else:
            r_stack.push(convert_string[n % base])
        n = n // base
    res = ""
    while not r_stack.is_empty():
        res = res + str(r_stack.pop())
    return res


def main():
    print(to_str_basic(1253))
    print(to_str(1453, 16))
    print(to_str_stack(1453, 16))


if __name__ == "__main__":
    main()
