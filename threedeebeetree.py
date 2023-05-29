from __future__ import annotations
from typing import Generic, TypeVar, Tuple
from dataclasses import dataclass, field

I = TypeVar('I')
Point = Tuple[int, int, int]

@dataclass
class BeeNode:

    key: Point
    item: I
    subtree_size: int = 1
    oct1: BeeNode | None = None
    oct2: BeeNode | None = None
    oct3: BeeNode | None = None
    oct4: BeeNode | None = None
    oct5: BeeNode | None = None
    oct6: BeeNode | None = None
    oct7: BeeNode | None = None
    oct8: BeeNode | None = None
    def get_child_for_key(self, point: Point) -> BeeNode | None:
        raise NotImplementedError()


class ThreeDeeBeeTree(Generic[I]):
    """ 3️⃣🇩🐝🌳 tree. """

    def __init__(self) -> None:
        """
            Initialises an empty 3DBT
        """
        self.root = None
        self.length = 0

    def is_empty(self) -> bool:
        """
            Checks to see if the 3DBT is empty
        """
        return len(self) == 0

    def __len__(self) -> int:
        """ Returns the number of nodes in the tree. """

        return self.length

    def __contains__(self, key: Point) -> bool:
        """
            Checks to see if the key is in the 3DBT
        """
        try:
            self.get_tree_node_by_key(key)
            return True
        except KeyError:
            return False

    def __getitem__(self, key: Point) -> I:
        """
            Attempts to get an item in the tree, it uses the Key to attempt to find it
        """
        node = self.get_tree_node_by_key(key)
        return node.item

    def get_tree_node_by_key(self, key: Point) -> BeeNode:
        return self.get_tree_node_by_key_aux(self.root, key)

    def get_tree_node_by_key_aux(self, current: BeeNode, key: Point) -> BeeNode:
        if current is None:
            raise KeyError('Key not found: {0}'.format(key))
        elif key == current.key:
            return current
        elif current.key[0] < key[0] and current.key[1] < key[1] and current.key[2] < key[2]:
            return self.get_tree_node_by_key_aux(current.oct1, key)
        elif current.key[0] < key[0] and current.key[1] >= key[1] and current.key[2] < key[2]:
            return self.get_tree_node_by_key_aux(current.oct2, key)
        elif current.key[0] < key[0] and current.key[1] >= key[1] and current.key[2] >= key[2]:
            return self.get_tree_node_by_key_aux(current.oct3, key)
        elif current.key[0] < key[0] and current.key[1] < key[1] and current.key[2] >= key[2]:
            return self.get_tree_node_by_key_aux(current.oct4, key)
        elif current.key[0] >= key[0] and current.key[1] < key[1] and current.key[2] >= key[2]:
            return self.get_tree_node_by_key_aux(current.oct5, key)
        elif current.key[0] >= key[0] and current.key[1] < key[1] and current.key[2] < key[2]:
            return self.get_tree_node_by_key_aux(current.oct6, key)
        elif current.key[0] >= key[0] and current.key[1] >= key[1] and current.key[2] < key[2]:
            return self.get_tree_node_by_key_aux(current.oct7, key)
        elif current.key[0] >= key[0] and current.key[1] >= key[1] and current.key[2] >= key[2]:
            return self.get_tree_node_by_key_aux(current.oct8, key)


    def __setitem__(self, key: Point, item: I) -> None:
        self.root = self.insert_aux(self.root, key, item)

    def insert_aux(self, current: BeeNode, key: Point, item: I) -> BeeNode:
        """
            Attempts to insert an item into the tree, it uses the Key to insert it
        """
        if current is None:
            current = BeeNode(key, item)
            self.length += 1
        elif current.key[0] < key[0] and current.key[1] < key[1] and current.key[2] < key[2]:
            current.subtree_size += 1
            current.oct1 = self.insert_aux(current.oct1, key, item)
        elif current.key[0] < key[0] and current.key[1] >= key[1] and current.key[2] < key[2]:
            current.subtree_size += 1
            current.oct2 = self.insert_aux(current.oct2, key, item)
        elif current.key[0] < key[0] and current.key[1] >= key[1] and current.key[2] >= key[2]:
            current.subtree_size += 1
            current.oct3 = self.insert_aux(current.oct3, key, item)
        elif current.key[0] < key[0] and current.key[1] < key[1] and current.key[2] >= key[2]:
            current.subtree_size += 1
            current.oct4 = self.insert_aux(current.oct4, key, item)
        elif current.key[0] >= key[0] and current.key[1] < key[1] and current.key[2] >= key[2]:
            current.subtree_size += 1
            current.oct5 = self.insert_aux(current.oct5, key, item)
        elif current.key[0] >= key[0] and current.key[1] < key[1] and current.key[2] < key[2]:
            current.subtree_size += 1
            current.oct6 = self.insert_aux(current.oct6, key, item)
        elif current.key[0] >= key[0] and current.key[1] >= key[1] and current.key[2] < key[2]:
            current.subtree_size += 1
            current.oct7 = self.insert_aux(current.oct7, key, item)
        elif current.key[0] >= key[0] and current.key[1] >= key[1] and current.key[2] >= key[2]:
            current.subtree_size += 1
            current.oct8 = self.insert_aux(current.oct8, key, item)

        return current

    def is_leaf(self, current: BeeNode) -> bool:
        """ Simple check whether or not the node is a leaf. """
        return (
                current.oct1 is None and
                current.oct2 is None and
                current.oct3 is None and
                current.oct4 is None and
                current.oct5 is None and
                current.oct6 is None and
                current.oct7 is None and
                current.oct8 is None
        )

if __name__ == "__main__":
    tdbt = ThreeDeeBeeTree()
    tdbt[(3, 3, 3)] = "A"
    tdbt[(1, 5, 2)] = "B"
    tdbt[(4, 3, 1)] = "C"
    tdbt[(5, 4, 0)] = "D"
    print(tdbt.root.get_child_for_key((4, 3, 1)).subtree_size) # 2
