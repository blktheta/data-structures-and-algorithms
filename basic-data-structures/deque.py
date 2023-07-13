from typing import TypeVar


T = TypeVar("T")


class Deque:
    """Deque implementation as a list."""

    def __init__(self):
        """Create new deque."""
        self.items: list[T] = []

    def is_empty(self) -> bool:
        """Check if the deque is empty."""
        return self.items == []

    def add_front(self, item: T):
        """Add an item to the front of the deque."""
        self.items.append(item)

    def add_rear(self, item: T):
        """Add an item to the rear of the deque."""
        self.items.insert(0, item)

    def remove_front(self) -> T:
        """Remove an item from the front of the deque."""
        return self.items.pop()

    def remove_rear(self) -> T:
        """Remove an item from the rear of the deque."""
        return self.items.pop(0)

    def size(self) -> int:
        """Get the number of items in the deque."""
        return len(self.items)
