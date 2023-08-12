"""
Unordered list implementation in Python.
"""
from typing import TypeVar
from node import Node


T = TypeVar("T")


class UnorderedList:
    """Unordered list implementation with Nodes."""

    def __init__(self):
        """Create new list."""
        self.head = None
        self.tail = None

    def is_empty(self) -> bool:
        """Check if the list is empty, O(1)."""
        return self.head is None

    def add(self, item: T):
        """Add an item to the list, O(1)."""
        temp = Node(item)
        temp.next = self.head
        self.head = temp

        if self.tail is None:
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

        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

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

    def append(self, item: T):
        """Add an item to the ned of the list, O(1)."""
        temp = Node(item)
        self.tail.next = temp
        self.tail = temp

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

    def insert(self, pos: int, item: T):
        """Add an item at position in the list, O(n)."""
        if (pos > self.size()) or (pos < 0):
            raise IndexError(f"{pos} does not exist")

        current = self.head
        previous = None

        for _ in range(pos - 1):
            previous = current
            current = current.next

        temp = Node(item)
        previous.next = temp
        temp.next = current

    def pop(self, pos: int = -1) -> T:
        """Remove and return an item at position from the list, O(n)."""
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
    lst = UnorderedList()

    lst.add(31)
    lst.add(77)
    lst.add(17)
    lst.add(93)
    lst.add(26)
    lst.add(54)

    # [54, 26, 93, 17, 77, 31]

    print(lst.size())
    print(lst.search(93))
    print(lst.search(100))

    lst.add(100)
    print(lst.search(100))
    print(lst.size())

    # [100, 54, 26, 93, 17, 77, 31]

    lst.remove(54)
    print(lst.size())
    lst.remove(93)
    print(lst.size())
    lst.remove(31)
    print(lst.size())
    print(lst.search(93))

    # [100, 26, 17, 77]

    lst.append(123)
    print(lst.size())
    print(lst.search(123))

    # [100, 26, 17, 77, 123]

    print(lst.tail.data)
    lst.remove(123)
    print(lst.tail.data)

    # [100, 26, 17, 77]

    lst.add(39)
    lst.add(82)
    lst.add(11)

    # [11, 82, 39, 100, 26, 17, 77]

    print(lst.index(17))
    print(lst.size())
    lst.insert(6, 4)
    print(lst.search(4))
    print(lst.index(4))
    print(lst.index(17))

    # [11, 82, 39, 100, 26, 17, 4, 77]

    print(lst.index(39))
    print(lst.pop(3))
    print(lst.index(100))

    # [11, 82, 100, 26, 17, 4, 77]

    print(lst.head.data)
    print(lst.index(11))


if __name__ == "__main__":
    main()
