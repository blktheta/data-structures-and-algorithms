from typing import TypeVar


T = TypeVar("T")


class Queue:
    """Queue implementation as a list."""

    def __init__(self):
        """Create new quque."""
        self.items: list[T] = []

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return self.items == []

    def enqueue(self, item: T):
        """Add an item to the queue."""
        self.items.insert(0, item)

    def dequeue(self) -> T:
        """Remove an item from the queue."""
        return self.items.pop()

    def size(self) -> int:
        """Get the number of items in the queue."""
        return len(self.items)
