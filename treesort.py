
from bst import BinarySearchTree
from typing import List

def treesort(array: List[int]) -> List[int]:
    """ Simple Tree Sort implementation.
        1. Adds all elements of the array to the tree.
        2. Traverses the tree in-order.
    """
    ## in each tree sort we need a new tree or we cannot add anyhting
    tree = BinarySearchTree()

    for v in array: ##insert al elements from tree as needed, this insertion also handles the operations of BST
        tree[v] = v # <v,v> key value pairs, this magic method adds all elements to true
    #once done, elements are yet to be sorted, by are in a binary search tree
    new_array = []

    def sorted_append(v):
        new_array.append(v)
    
    tree.inorder(sorted_append)

    return new_array

if __name__ == '__main__':
    array = [int(v) for v in input('Enter sequence: ').strip().split()]
    print(' '.join([str(v) for v in treesort(array)]))

    # remember that duplicate elements are not allowed by our BST insertion!

