"""
BinaryHeap() creates a new empty binary heap.

insert(k) adds a new item to the heap.

get_min() returns the item with the minimum key value, leaving the item in the heap.

delete() returns the item with the minimum key value, removing the item from the heap.

is_empty() returns True if the heap is empty, False otherwise.

size() returns the number of items in the heap.

heapify(list) builds a new heap from a list of keys.
"""
from typing import TypeVar


T = TypeVar("T")


class BinaryHeap:
    def __init__(self):
        self._heap = []

    def _perc_up(self, i: int):
        while (i - 1) // 2 >= 0:
            parent_idx = (i - 1) // 2

            if self.heap[i] < self._heap[parent_idx]:
                self._heap[i], self._heap[parent_idx] = self._heap[parent_idx], self._heap[i]
            i = parent_idx

    def _perc_down(self, i: int):
        while 2 * i + 1 < len(self._heap):
            sm_child = self._get_min_child(i)
            if self._heap[i] > self._heap[sm_child]:
                self._heap[i], self._heap[sm_child] = self._heap[sm_child], self._heap[i]
            else:
                break
            i = sm_child

    def _get_min_child(self, i: int) -> int:
        if 2 * i + 2 > len(self._heap) - 1:
            return 2 * i + 1
        if self._heap[2 * i + 1] < self._heap[2 * i + 2]:
            return 2 * i + 1
        return 2 * i + 2

    def insert(self, item: T):
        self._heap.append(item)
        self._perc_up(len(self._heap) - 1)

    def delete(self):
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        result = self._heap.pop()
        self._perc_down(0)
        return result

    def heapify(self, not_a_heap: T):
        self._heap = not_a_heap[:]
        i = len(self._heap) // 2 - 1
        while i >= 0:
            self._perc_down(i)
            i = i - 1

    def is_empty(self):
        return not bool(self._heap)

    def __len__(self):
        return len(self._heap)

    def __str__(self):
        return str(self._heap)


a_heap = BinaryHeap()
a_heap.heapify([9, 5, 6, 2, 3])

while not a_heap.is_empty():
    print(a_heap.delete())
