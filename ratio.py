from __future__ import annotations
from typing import Generic, TypeVar
from math import ceil
from bst import BinarySearchTree

T = TypeVar("T")
I = TypeVar("I")

class Percentiles(Generic[T]):

    def __init__(self) -> None:
        self.our_adt = BinarySearchTree()
    
    def add_point(self, item: T):
        self.our_adt[item] = item
    
    def remove_point(self, item: T):
        del self.our_adt[self.our_adt[item]]


    def ratio(self, x, y):
        return_list = []
        length_percent = 100/self.our_adt.length
        x_index = 1 + ceil(x/length_percent)

        y_index = self.our_adt.length - ceil(y/length_percent)


        print("~~~~~~~~~~~~~~~")
        print(self.our_adt.root)
        for i in range(x_index, y_index + 1):
            return_list.append(self.our_adt.kth_smallest(i, self.our_adt.root).key)
            print(return_list)

        return return_list



if __name__ == "__main__":
    points = list(range(50))
    import random
    random.shuffle(points)
    p = Percentiles()
    for point in points:
        p.add_point(point)

    print(p.our_adt.root, p.our_adt.root.left, p.our_adt.root.right)
    print(p.our_adt[1])
    print(p.our_adt.root)
    p.remove_point(1)
    print(p.our_adt.root)
    #print(p.our_adt[1])

    # for i in p:
    #     print(p)
    # Numbers from 8 to 16.
    # print(p.ratio(15, 66))
