""" Binary Search Tree ADT.
    Defines a Binary Search Tree with linked nodes.
    Each node contains a key and item as well as references to the children.
"""

from __future__ import annotations

__author__ = 'Brendon Taylor, modified by Alexey Ignatiev, further modified by Jackson Goerner'
__docformat__ = 'reStructuredText'

from typing import TypeVar, Generic, List
from node import TreeNode
import sys

from referential_array import ArrayR

# generic types
K = TypeVar('K')
I = TypeVar('I')
T = TypeVar('T')


class BinarySearchTree(Generic[K, I]):
    """ Basic binary search tree. """

    def __init__(self) -> None:
        """
            Initialises an empty Binary Search Tree
            :complexity: O(1)
        """

        self.root = None
        self.length = 0

    def is_empty(self) -> bool:
        """
            Checks to see if the bst is empty
            :complexity: O(1)
        """
        return self.root is None

    def __len__(self) -> int:
        """ Returns the number of nodes in the tree. """

        return self.length

    def __contains__(self, key: K) -> bool:
        """
            Checks to see if the key is in the BST
            :complexity: see __getitem__(self, key: K) -> (K, I)
        """
        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True

    def __getitem__(self, key: K) -> I:
        """
            Attempts to get an item in the tree, it uses the Key to attempt to find it
            :complexity best: O(CompK) finds the item in the root of the tree
            :complexity worst: O(CompK * D) item is not found, where D is the depth of the tree
            CompK is the complexity of comparing the keys
        """
        return self.get_tree_node_by_key(key).item

    def get_tree_node_by_key(self, key: K) -> TreeNode:
        return self.get_tree_node_by_key_aux(self.root, key)

    def get_tree_node_by_key_aux(self, current: TreeNode, key: K) -> TreeNode:
        if current is None:
            raise KeyError('Key not found: {0}'.format(key))
        elif key == current.key:
            return current
        elif key < current.key:
            return self.get_tree_node_by_key_aux(current.left, key)
        else:  # key > current.key
            return self.get_tree_node_by_key_aux(current.right, key)

    def __setitem__(self, key: K, item: I) -> None:

        self.root = self.insert_aux(self.root, key, item)

    def insert_aux(self, current: TreeNode, key: K, item: I) -> TreeNode:
        """
            Attempts to insert an item into the tree, it uses the Key to insert it
            :complexity best: O(CompK) inserts the item at the root.
            :complexity worst: O(CompK * D) inserting at the bottom of the tree
            where D is the depth of the tree
            CompK is the complexity of comparing the keys
        """

        if current is None:  # base case: at the leaf
            current = TreeNode(key, item=item)
            self.length += 1

        elif key < current.key:
            # print("GOING LEFT")
            current.subtree_size += 1
            current.left = self.insert_aux(current.left, key, item)

        elif key > current.key:
            # print("GOING RIGHT")
            current.subtree_size += 1
            current.right = self.insert_aux(current.right, key, item)
            # current.subtree_size + 1
        else:  # key == current.key
            raise ValueError('Inserting duplicate item')
        # print("I AM {} WITH SIZE {}".format(current, current.subtree_size))
        return current

    def __delitem__(self, key: K) -> None:
        self.root = self.delete_aux(self.root, key)

    def delete_aux(self, current: TreeNode, key: K) -> TreeNode:
        """
            Attempts to delete an item from the tree, it uses the Key to
            determine the node to delete.
        """
        current.subtree_size -= 1
        if current is None:  # key not found
            raise ValueError('Deleting non-existent item')
        elif key < current.key:
            current.left  = self.delete_aux(current.left, key)
        elif key > current.key:
            current.right = self.delete_aux(current.right, key)
        else:  # we found our key => do actual deletion
            if self.is_leaf(current):
                self.length -= 1
                return None
            elif current.left is None:
                self.length -= 1
                return current.right
            elif current.right is None:
                self.length -= 1
                return current.left

            # general case => find a successor
            succ = self.get_successor(current)
            current.key  = succ.key
            current.item = succ.item
            current.right = self.delete_aux(current.right, succ.key)

        return current

    def get_successor(self, current: TreeNode) -> TreeNode:
        """
            Get successor of the current node.
            It should be a child node having the smallest key among all the
            larger keys.
        """
        return self.get_successor_aux(current)

    def get_successor_aux(self, current: TreeNode):
        if current.right is None:
            return None
        return self.get_minimal_aux(current.right)

    def get_minimal(self, current: TreeNode) -> TreeNode:
        """
            Get a node having the smallest key in the current sub-tree.
        """
        return self.get_minimal_aux(current)

    def get_minimal_aux(self, current: TreeNode):
        if current.left is None:
            return current
        return self.get_minimal_aux(current.left)
    def is_leaf(self, current: TreeNode) -> bool:
        """ Simple check whether or not the node is a leaf. """

        return current.left is None and current.right is None

    def draw(self, to=sys.stdout):
        """ Draw the tree in the terminal. """

        # get the nodes of the graph to draw recursively
        self.draw_aux(self.root, prefix='', final='', to=to)

    def draw_aux(self, current: TreeNode, prefix='', final='', to=sys.stdout) -> K:
        """ Draw a node and then its children. """

        if current is not None:
            real_prefix = prefix[:-2] + final
            print('{0}{1}'.format(real_prefix, str(current.key)), file=to)

            if current.left or current.right:
                self.draw_aux(current.left,  prefix=prefix + '\u2551 ', final='\u255f\u2500', to=to)
                self.draw_aux(current.right, prefix=prefix + '  ', final='\u2559\u2500', to=to)
        else:
            real_prefix = prefix[:-2] + final
            print('{0}'.format(real_prefix), file=to)


    # def inorder_traversal(self, node) -> list:
    #     my_list = []
    #     node = self.root
    #     self.inorder_traversal_aux(node, my_list)
    #     return my_list
    #
    # def inorder_traversal_aux(self, current: TreeNode, cur_list: list[TreeNode[K, I]]):
    #     if current is None:
    #         return
    #     self.inorder_traversal_aux(current.left, cur_list)
    #     cur_list.append(current.item)
    #     self.inorder_traversal_aux(current.right, cur_list)

    # def treesort(array: List[int]) -> List[int]:
    #     """ Simple Tree Sort implementation.
    #         1. Adds all elements of the array to the tree.
    #         2. Traverses the tree in-order.
    #     """
    #     ## in each tree sort we need a new tree or we cannot add anyhting
    #     tree = BinarySearchTree()
    #
    #     for v in array:  ##insert al elements from tree as needed, this insertion also handles the operations of BST
    #         tree[v] = v  # <v,v> key value pairs, this magic method adds all elements to true
    #     # once done, elements are yet to be sorted, by are in a binary search tree
    #     new_array = []
    #
    #     def sorted_append(v):
    #         new_array.append(v)
    #
    #     tree.inorder(sorted_append)
    #
    #     return new_array
    def kth_smallest(self, k: int, current: TreeNode) -> TreeNode:
        """
        Finds the kth smallest value by key in the subtree rooted at current.
        """
        if k == 1:
            return current
        if current.left is not None and current.left.subtree_size < k:


        stack = ArrayR(k)
        print(current.left)
        for i in range(k):
            if current.left is not None:
                temp_min = self.get_minimal(current)
                # self.__delitem__(temp_min.key)
                current.
                getter = self.__getitem__(temp_min.key)
                print("MY GETTER {}".format(getter))
            else:
                temp_min = self.get_successor(current)
                self.__delitem__(temp_min.key)
            stack[i] = temp_min.key, temp_min.item
            print(temp_min)
            print(current)
            print(self.get_minimal(current))
            print("   ")
        print(len(stack))
        for term in reversed(stack):
            print(term)
            # print(i)
            # print(i[0])
            # print(stack[i])
            self.__setitem__(term[0], term[1])

        print("  ")
        print(self.get_minimal(self.root))
        print(current)
        print(" TESTING INPUTS ")
        print(current.left)
        return temp_min



        # print(stack.__len__())
        # print(len(stack))
        # print(current)
        # for i in range(current.subtree_size):
        #     if current.left is not None:
        #         minimal = self.get_minimal(current)
        #         print(minimal)
        #         stack[i] = minimal.key, minimal.item
        #         print("CHECKING MY STACK CONTENT {}".format(stack[i]))
        #         # del minimal.key
        #         self.__delitem__(stack[i][0])
        #         print("MY NEW STACK[i] {} AND VALUE {}".format(stack[i][0],stack[i][1]))
        #         print(len(stack))
        #         # print("FIRST IF")
        #         print("WHICH I I AM IN {} ".format(i))
        #         break
        #     if current.right is not None:
        #         print("WHICH I I AM IN {} ".format(i))
        #         # print("2nd if")
        #         stack[i] = self.get_successor(current)
        #         # self.__delitem__(stack[i].key)
        #         break
        #     if self.is_leaf(current):
        #         print("WHICH I I AM IN {} ".format(i))
        #         break
        # for i in range(len(stack)):
        #     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        #     print(stack[i])
        # item_to_return = stack[k]
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print(item_to_return)
        # print(len(stack))
        # for i in range(len(stack)):
        #     print(stack[i])
        #     # print("WE {} COOL {} GUYS {}".format(stack[i]), stack[i][0], stack[i][1])
        #     # self.__setitem__(stack[i], stack[0], stack[1])
        #
        # return item_to_return







