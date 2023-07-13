from stack import Stack


def balance_checker(symbol_str: str) -> bool:
    """Check if the string contains balanced parentheses."""
    stck = Stack()
    for symbol in symbol_str:
        if symbol in "([{":
            stck.push(symbol)
        else:
            if stck.is_empty():
                return False
            else:
                if not matches(stck.pop(), symbol):
                    return False
    return stck.is_empty()


def matches(sym_left: str, sym_right: str) -> bool:
    """Assist with symbol matching the current closing symbol."""
    all_lefts = "([{"
    all_rights = ")]}"
    return all_lefts.index(sym_left) == all_rights.index(sym_right)


if __name__ == "__main__":
    print(balance_checker("((()))"))    # expected True
    print(balance_checker("((()()))"))  # expected True
    print(balance_checker("(()"))   # expected False
    print(balance_checker(")("))    # expected False
    print(balance_checker('{({([][])}())}'))    # expected True
    print(balance_checker('[{()]'))     # expected False
