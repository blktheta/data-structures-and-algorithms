"""
Ordered list implementation in Python.
"""
from typing import TypeVar
from node import Node


T = TypeVar("T")


class OrderedList:
    """Ordered list implementation with Nodes."""

    def __init__(self):
        """Create new list."""
        self.head = None
        self.tail = None

    def is_empty(self) -> bool:
        """Check if the list is empty, O(1)."""
        return self.head is None

    def add(self, item: T):
        """Add an item to the list, O(n)."""
        current = self.head
        previous = None
        stop = False

        while (current is not None) and (not stop):
            if current.data > item:
                stop = True
            else:
                previous = current
                current = current.next

        temp = Node(item)
        if previous is None:
            temp.next = self.head
            self.head = temp
        else:
            temp.next = current
            previous.next = temp

            if temp.next is None:
                self.tail = temp

    def size(self) -> int:
        """Get the number of items in the list, O(n)."""
        current = self.head
        count = 0

        while current is not None:
            count = count + 1
            current = current.next
        return count

    def search(self, item: T) -> bool:
        """Search for an item in the list, O(n)."""
        current = self.head
        found = False
        stop = False

        while (current is not None) and (not found) and (not stop):
            if current.data == item:
                found = True
            else:
                if current.data > item:
                    stop = True
                else:
                    current = current.next
        return found

    def remove(self, item: T):
        """Remove an item from the list, O(n)."""
        current = self.head
        previous = None

        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next

        if current is None:
            raise ValueError(f"{item} is not in the list")
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
            if previous.next is None:
                self.tail = previous

    def index(self, item: T) -> int:
        """Retrieve the position of an item in the list, O(n)."""
        current = self.head
        pos = 0

        while current is not None:
            pos = pos + 1

            if current.data == item:
                return pos
            current = current.next
        raise ValueError(f"{item} is not in the list")

    def pop(self, pos: int = -1) -> T:
        """Remove and return an item at position from the list, 0(n)."""
        if pos == -1:
            pos = self.size()

        if (pos > self.size()) or (pos < 0):
            raise IndexError(f"{pos} does not exist")

        current = self.head
        previous = None

        for _ in range(pos - 1):
            previous = current
            current = current.next

        previous.next = current.next
        if previous.next is None:
            self.tail = previous
        return current.data


def main():
    lst = OrderedList()

    print(lst.is_empty())   # True
    lst.add(31)
    lst.add(77)
    lst.add(17)
    lst.add(93)
    lst.add(26)
    lst.add(54)

    print(lst.head.data)    # 17
    print(lst.tail.data)    # 93
    print(lst.is_empty())   # False
    print(lst.size())       # 6

    lst.remove(54)
    lst.remove(93)
    print(lst.size())       # 4
    print(lst.tail.data)    # 77
    print(lst.index(77))    # 4

    lst.pop()
    print(lst.tail.data)    # 31
    print(lst.size())       # 3

    lst.pop(2)
    print(lst.search(26))   # False


if __name__ == "__main__":
    main()
