"""Max Heap implemented using an array"""
from __future__ import annotations
__author__ = "Brendon Taylor, modified by Jackson Goerner"
__docformat__ = 'reStructuredText'

from typing import Generic
from referential_array import ArrayR, T


class MaxHeap(Generic[T]):
    MIN_CAPACITY = 1

    def __init__(self, max_size: int) -> None:
        self.length = 0
        self.the_array = ArrayR(max(self.MIN_CAPACITY, max_size) + 1)

    def __len__(self) -> int:
        return self.length

    def is_full(self) -> bool:
        return self.length + 1 == len(self.the_array)

    def rise(self, k: int) -> None:
        """
        Rise element at index k to its correct position
        Instead of comparing Item in while loop, we compute item_value and compare these computed values instead
        :pre: 1 <= k <= self.length
        """
        item = self.the_array[k]
        item_value = min(item.capacity, item.volume) * item.nutrient_factor

        while k > 1 and item_value > min(self.the_array[k // 2].capacity, self.the_array[k // 2].volume) * self.the_array[k // 2].nutrient_factor:
            self.the_array[k] = self.the_array[k // 2]
            k = k // 2
        self.the_array[k] = item



    def add(self, element: T) -> bool:
        """
        Swaps elements while rising
        """
        if self.is_full():
            raise IndexError

        self.length += 1
        self.the_array[self.length] = element
        self.rise(self.length)

    def largest_child(self, k: int) -> int:
        """
        Returns the index of k's child with greatest computed value.
        :pre: 1 <= k <= self.length // 2
        """
        
        if 2 * k == self.length or \
                min(self.the_array[2 * k].capacity, self.the_array[2 * k].volume) * self.the_array[2 * k].nutrient_factor > \
                min(self.the_array[2 * k + 1].capacity, self.the_array[2 * k + 1].volume) * self.the_array[2 * k + 1].nutrient_factor:
            return 2 * k
        else:
            return 2 * k + 1

    def sink(self, k: int) -> None:
        """ Make the element at index k sink to the correct position.
            Instead of using item, we use the computed values of items at that position
            :pre: 1 <= k <= self.length
            :complexity: ???
        """
        item = self.the_array[k]
        item_value = min(item.capacity, item.volume) * item.nutrient_factor

        while 2 * k <= self.length:
            max_child = self.largest_child(k)
            if min(self.the_array[max_child].capacity, self.the_array[max_child].volume) * self.the_array[max_child].nutrient_factor <= item_value:
                break
            self.the_array[k] = self.the_array[max_child]
            k = max_child

        self.the_array[k] = item
        
    def get_max(self) -> T:
        """ Remove (and return) the maximum element from the heap. """
        if self.length == 0:
            raise IndexError

        max_elt = self.the_array[1]
        self.length -= 1
        if self.length > 0:
            self.the_array[1] = self.the_array[self.length+1]
            self.sink(1)
        return max_elt

if __name__ == '__main__':
    items = [ int(x) for x in input('Enter a list of numbers: ').strip().split() ]
    heap = MaxHeap(len(items))

    for item in items:
        heap.add(item)
        
    while(len(heap) > 0):
        print(heap.get_max())
