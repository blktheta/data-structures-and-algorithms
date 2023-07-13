from deque import Deque


def palindrom_checker(string: str) -> bool:
    char_deque = Deque()

    for c in string:
        char_deque.add_rear(c)

    while char_deque.size() > 1:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last:
            return False
    return True


print(palindrom_checker("lsdkjfskf"))
print(palindrom_checker("radar"))
