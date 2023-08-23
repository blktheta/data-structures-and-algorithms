""" Hashing search algorithm.

Build a data structure that can be searched in O(1) time.
This is concept is referred to as hashing.

A hash table is a collection of items which are stored in a way to
make them easy to find. Each position of the hash table hold an item
and is named by an integer value.

The mapping between an item and the slot where that item belongs in the
hash table is called hash function. The hash function will take any
item in the collection and return an integer in the range of slot names
between 0 and s - 1.
"""
from typing import TypeVar


T = TypeVar("T")


class HashTable:
    """ Data structure that store a collection of item.

        Attributes:
            size: length of the collection
            slots: placement of the item
            data: value of the item

        Functions:
            put: places an item in the collection
            get: retrieves an item from the collection
            remove: removes an item from the collection
            hash_function: basic remainder hash mapper
            hash_str: hash based on character based strings
            hash_str_weighted: char based has fix for anagrams
            rehash: recompute the remainder hash
            hash_size: returns the length of the collection

    """
    def __init__(self):
        """Create new hashtable."""
        self.size: int = 11  # prime number for efficient collision resolution
        self.slots: list[T] = [None] * self.size
        self.data: list[T] = [None] * self.size

    def put(self, key: int, data: T):
        """Computes the hash value and store the item."""
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data  # replace
            else:
                next_slot = self.rehash(hash_value, len(self.slots))

                while (
                    self.slots[next_slot] is not None
                    and self.slots[next_slot] != key
                ):
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def hash_function(self, key: int, size: int) -> int:
        """Divides the item and return its remainder as hash value."""
        return key % size

    def hash_str(self, string: str, size: int) -> int:
        """Returns the remainder for character based hash."""
        # anagrams will be given same hash
        return sum([ord(c) for c in string]) % size

    def hash_str_weighted(self, string: str, size: int) -> int:
        """Remedy for hash function that is based on character strings."""
        return sum([i * ord(c) for i, c in enumerate(string)]) % size

    def rehash(self, old_hash: int, size: int) -> int:
        """Recomputes the hash when item slot is already taken."""
        return (old_hash + 1) % size

    def get(self, key: int) -> T:
        """Retrieves the item by computing the hash."""
        start_slot = self.hash_function(key, len(self.slots))

        position = start_slot
        while self.slots[position] is not None:
            if self.slots[position] == key:
                return self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    return None

    def remove(self, key: int):
        """Removes the item by computing the hash."""
        start_slot = self.hash_function(key, len(self.slots))

        position = start_slot
        while self.slots[position] is not None:
            if self.slots[position] == key:
                self.slots[position] = None
                self.data[position] = None
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    break

    def hash_size(self):
        """Return the size of the collection."""
        count = 0
        print(len(self.slots))
        for pos in range(len(self.slots)):
            if (self.slots[pos] is not None) and (self.data[pos] is not None):
                count = count + 1
        return count

    def __getitem__(self, key: int) -> T:
        return self.get(key)

    def __setitem__(self, key: int, data: T):
        self.put(key, data)

    def __delitem__(self, key: int) -> T:
        self.remove(key)

    def __contains__(self, key: int) -> bool:
        return key in self.slots


def main():
    # setup
    h = HashTable()
    h[54] = "cat"
    h[26] = "dog"
    h[93] = "lion"
    h[17] = "tiger"
    h[77] = "bird"
    h[31] = "cow"
    h[44] = "goat"
    h[55] = "pig"
    h[20] = "chicken"
    print(h.slots)
    print(h.data)

    # modify
    print(h[20])  # chicken
    print(h[17])  # tiger
    h[20] = "duck"
    print(h[20])  # duck

    print(h.data)
    print(h[99])  # None

    print(h.slots)
    print(h.data)
    del h[26]  # remove dog
    del h[99]
    print(h.slots)
    print(h.data)

    print(h.hash_size())  # 8

    print(55 in h)  # True
    print(99 in h)  # False


if __name__ == "__main__":
    main()
