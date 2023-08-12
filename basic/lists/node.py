"""
Node implementation in Python.
"""
from typing import TypeVar


T = TypeVar("T")


class Node:
    """A node of a linked list."""

    def __init__(self, node_data: T):
        """Create new node."""
        self._data = node_data
        self._next = None

    def get_data(self) -> T:
        """Get node data."""
        return self._data

    def set_data(self, node_data: T):
        """Set node data."""
        self._data = node_data

    data = property(fget=get_data, fset=set_data, doc="The data property")

    def get_next(self) -> T:
        """Get next node."""
        return self._next

    def set_next(self, next_node: T):
        """Set next node."""
        self._next = next_node

    next = property(fget=get_next, fset=set_next, doc="The next property")

    def __str__(self):
        """String."""
        return str(self._data)
