""" Balanced parentheses

Method: Stack

Algorithm that read a string of parentheses from left to right and
decide whether the symbols are balanced.

Balanced parentheses means that each opening symbol has a corresponding
closing symbol and the pairs of parentheses are properly nested.

Consider the following correctly balanced strings of parentheses:
    (()()()())

    (((())))

    (()((())()))

Compare those with the following, which are not balanced:

    ((((((())

    ()))

    (()()(()
"""
from stack import Stack


def balance_checker(symbol_str: str) -> bool:
    """Check if the string contains balanced parentheses."""
    s = Stack()
    for symbol in symbol_str:
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                if not matches(s.pop(), symbol):
                    return False
    return s.is_empty()


def matches(sym_left: str, sym_right: str) -> bool:
    """Assist with symbol matching the current closing symbol."""
    all_lefts = "([{"
    all_rights = ")]}"
    return all_lefts.index(sym_left) == all_rights.index(sym_right)


def main():
    print(balance_checker("((()))"))            # expected True
    print(balance_checker("((()()))"))          # expected True
    print(balance_checker("(()"))               # expected False
    print(balance_checker(")("))                # expected False
    print(balance_checker('{({([][])}())}'))    # expected True
    print(balance_checker('[{()]'))             # expected False


if __name__ == "__main__":
    main()
