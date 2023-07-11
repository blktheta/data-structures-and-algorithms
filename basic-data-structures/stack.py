from typing import TypeVar


T = TypeVar("T")


class Stack:
    """Stack implementation as a list."""

    def __init__(self):
        """Create new stack."""
        self.items: list[T] = []

    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return self.items == []

    def push(self, item: T):
        """Add an item to the stack."""
        self.items.append(item)

    def pop(self) -> T:
        """Remove an item from the stack."""
        return self.items.pop()

    def peek(self) -> T:
        """Get the value of the top item in the stack."""
        return self.items[-1]

    def size(self) -> int:
        """Get the number of items in the stack."""
        return len(self.items)
