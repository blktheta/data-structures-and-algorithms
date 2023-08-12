"""
Queue implementation in Python, the queue assumes that the rear is at
position 0 in the list. This allows for the insert function to lists to
ass new elements to the rear of the queue. The pop operation can be
used to remove the front element(the last element on the list).
"""
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
        """Add an item to the queue, O(n)."""
        self.items.insert(0, item)

    def dequeue(self) -> T:
        """Remove an item from the queue, O(1)."""
        return self.items.pop()

    def size(self) -> int:
        """Get the number of items in the queue."""
        return len(self.items)
