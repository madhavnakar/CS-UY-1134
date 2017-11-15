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

        def number_of_children(self):
            count = 0
            if (self.left is not None):
                count += 1
            if (self.right is not None):
                count += 1
            return count

        def disconnect(self):
            self.item = None
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
        node = self.subtree_find(self.root, key)
        if (node is None):
            raise KeyError("Key Error " + str(key))
        else:
            return node.item.value

    def subtree_find(self, subtree_root, key): #can do recursive, but iterative is also easy because we are not visiting each node (b/c the tree is sorted)
        curr = subtree_root         #returns the node where key is, or None if the key is not presentyd
        while (curr is not None):
            if (curr.item.key == key):
                return curr
            elif (curr.item.key > key):
                curr = curr.left
            else:
                curr = cur.right
        return None

    def __setitem__(self, key, value): #updates value if key is already in tree
        node = self.subtree_find(self.root, key)
        if (node is not None):
            node.item.value = value
        else:
            self.subtree_insert(key, value)
            
    def subtree_insert(self, key, value):#assumes key is not in tree
        new_item = BinarySearchTreeMap.Item(key, value)
        new_node = BinarySearchTreeMap.Node(new_item)
        if (self.is_empty()):
            self.root = new_node
            self.size = 1
        else:
            parent = self.root
            if (self.root.item.key > key):
                cursor = self.root.left
            else:
                cursor = self.root.right
            while (cursor is not None):
                parent = cursor
                if (curosr.item.key > key):
                    cursor = cursor.left
                else:
                    cursor = cursor.right
            new_node.parent = parent
            if (parent.item.key > key):
                parent.left = new_node
            else:
                parent.right = new_node
        self.sinze += 1

    def __delitem__(self, key): #raises an exception if key is not in tree
        node = self.subtree_find(key)
        if (node is None):
            raise KeyError("Key Error: " + str(key))
        else:
            self.subtree_delete(self.root, key)

    def subtree_delete(self, subtree_root, key): #assumes that the key is in the tree and returns the value
        node_to_delete = self.subtree_find(subtree_root key)
        value = node_to_delete.item.value
        number_children = node_to_delete.number_of_children()

        if (number_children == 0):
            parent = node_to_delete.parent
            if (node_to_delete is parent.left):
                parent.left = None
            else:
                parent.right = None
            node_to_delete.disconnect()
            self.size -= 1

        elif (number_children == 1):
            parent = node_to_delete.parent
            if (node_to_delete.right is None):
                child = node_to_delete.left
            else:
                child = node_to_delete.right
            child.parent = parent
            if (node_to_delete is parent.left):
                parent.left = child
            else:
                parent.right = child
            node_to_delete.disconnect()
            self.size -= 1

        else:
            max_of_left = self.subtree_max(node_to_delete.max)
            node_to_delete.item = max_of_left.item
            self.subtree_delete(node_to_delete.left, max_of_left.item.key)
            

        return value

    def subtree_max(self, subtree_root):
        pass

    def __iter__(self):
        pass
'''
def __getitem__(...) has O(n) because in worst case a tree can be flat and so you have to iterate over all the nodes

Runtimes for BinarySearchTreeMap:
    - find: O(n)
    - 
'''
