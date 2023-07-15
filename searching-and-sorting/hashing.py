from typing import TypeVar


T = TypeVar("T")


class HashTable:
    def __init__(self):
        self.size: int = 11  # prime number for efficient collision resolution
        self.slots: list[T] = [None] * self.size
        self.data: list[T] = [None] * self.size

    def put(self, key: int, data: T):
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
        return key % size

    def hash_str(self, string: str, size: int) -> int:
        # anagrams will be given same hash
        return sum([ord(c) for c in string]) % size

    def hash_str_weighted(self, string: str, size: int) -> int:
        # remedy for anagrams
        return sum([i * ord(c) for i, c in enumerate(string)]) % size

    def rehash(self, old_hash: int, size: int) -> int:
        return (old_hash + 1) % size

    def get(self, key: int) -> T:
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
