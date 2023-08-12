"""
Method: Deque
Example: Palindrome Checker

Algorithm that read a string of characters and check whether
it is a palindrome or not.

A palindrome is a string that reads the same forwad and backward,
for example; radar, toot, and madam.
"""
from deque import Deque


def palindrom_checker(string: str) -> bool:
    """Check wether the string is a palindrome."""
    char_deque = Deque()

    for c in string:
        char_deque.add_rear(c)

    while char_deque.size() > 1:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last:
            return False
    return True


def main():
    print(palindrom_checker("lsdkjfskf"))
    print(palindrom_checker("radar"))


if __name__ == "__main__":
    main()
