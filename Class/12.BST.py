'''
To better the runtime of the map ADT, which we previously implement as UnsortedArrayMap, we introduce BinarySearchTree

Definition:
A binary tree is a binary tree search if:
    - All keys stored in the left subtree of n are less than the key stored in n
    - All keys stored in the rught subtree of n are greater than the key stored in n
**In the context of a map we are assuming that the keys are unique because there cannot be multiple keys in the same map**
- In our implementation each node of the BST will contain the class Item
'''

class BinarySearchTree:
    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value

    class Node:
        def __init__(self, item):
            self.item = item
            self.left = None
            self.right = None
            self.parent = None

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return (self.size)

    def is_empty(self):
        return (len(self) == 0)

    def __getitem__(self, key):
        node = self.subtree_find(key)
        if (node is None):
            raise KeyError("Key Error " + str(key))
        else:
            return node.item.value

    def subtree_find(self, key): #can do recursive, but iterative is also easy because we are not visiting each node (b/c the tree is sorted)
        curr = self.root         #returns the node where key is, or None if the key is not presentyd
        while (curr is not None):
            if (curr.item.key == key):
                return curr
            elif (curr.item.key > key):
                curr = curr.left
            else:
                curr = cur.right
        return None

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def __iter__(self):
        pass
'''
def __getitem__(...) has O(n) because in worst case a tree can be flat and so you have to iterate over all the nodes
'''
