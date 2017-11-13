'''
Terminology of trees:
    family relations:
        child of a node
        parent of a node
        sibling of a node
    edge - line or a branch in the tree
    path in the tree - a sequence of nodes where each two subsequent nodes are connected by an edge
    length of a path - number of edges in the path
    ancestor of a node - all nodes on the path from that node to the root
    decendant of a node - all nodes on the path below that node (ie all nodes that have that node as its ancestor)
    level/height of the tree - number of edges in the longest path
    types of nodes:
        root - starting point
        leaf - node with no children
    
    kinds of trees:
        binary tree: each node has atmost 2 children 
        full (proper) tree: each node has either 2 or 0 children (not 1)
        complete binary tree: all levels are filled with as many nodes as possible
'''

class Node:
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data #we will make data required. left, right and parent are optional
        self.left = left
        if (left is not None):#we do this so the nodes on left/right are connected to the parent, which is self
            self.left.parent = self
        self.right = right
        if (right is not None):
            self.right.parent = self
        self.parent = parent
'''
creating the below binary tree with node class starting from down:

      4
   /     \ 
  2      6
 / \    /
1   3  5

height of this tree would be 2. height is length of the longest path
'''
l_ch1 = Node(1)
r_ch1 = Node(3)
l_ch2 = Node(2, l_ch1, r_ch1)
l_ch3 = Node(5)
r_ch2 = Node(6, l_ch3)
root = Node(4, l_ch2, r_ch2)

class EmptyCollection(Exception):
    pass
class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None, parent=None):
            self.data = data #we will make data required. left, right and parent are optional
            self.left = left
            if (left is not None):#we do this so the nodes on left/right are connected to the parent, which is self
                self.left.parent = self
            self.right = right
            if (right is not None):
                self.right.parent = self
            self.parent = parent
    def __init__(self, root=None):
        self.root = root
        self.size = self.count_nodes_in_subtree(self.root)
    def __len__(self):
        return (self.size)
    def is_empty(self):
        return (len(self) == 0)
    def count_nodes_in_subtree(self, subtree_root):
        if (subtree_root is None):
            return (0)
        else:
            left_count = self.count_nodes_in_subtree(subtree_root.left)
            right_count = self.count_nodes_in_subtree(subtree_root.right)
            return (left_count + right_count + 1)
    def sum_tree(self):
        return (self.sum_subtree(self.root))
    def sum_subtree(self, subtree_root):
        if (subtree_root is None):
            return (0)
        else:
            left_sum = self.sum_subtree(subtree_root.left)
            right_sum = self.sum_subtree(subtree_root.right)
            return (left_sum  + right_sum + subtree_root.data)
    def height(self):
        if (self.is_empty()):
            raise EmptyCollection("Height is not defined for an empty tree")
        return subtree_height(self.root)
    def subtree_height(self, subtree_root):#this function finds the length of longest path.
        if (subtree_root.left is None and subtree_root.right is None):#height of an empty tree is not defined. Can't return 0 b/c that is the height of 1 node
            return (0)
        elif (subtree_root.left is None):
            return 1 + self.subtree_height(subtree_root.right)
        elif(subtree_root.right is None):
            return 1 + self.subtree_height(subtree_root.left)
        else: #if both arent none
            left_height = self.subtree_height(subtree_root.left)
            right_height = self.subtree_height(subtree_root.right)
            return (1 + max(left_height, right_height))
    def preorder(self):
        yield from self.subtree_preorder(self.root)
    def subtree_preoder(self, subtree_root):
        if (subtree_root is None):
            return 
        else:
            yield subtree_root #we dont return the data so that we get more access (ie if we want to change the data)
            yield from self.subtree_preorder(subtree_root.left)  # we use 'yield from' because calling a generator from a generator doesn't work. we need to
            yield from self.subtree_preorder(subtree_root.right) # 'yield from' is the same as for i in (...):
    def inorder(self):
        yield from self.subtree_inorder(self.root)
    def subtree_inorder(self, subtree_root):
        if (subtree_root is None):
            return
        else:
            yield from self.subtree_inorder(subtree_root.left)
            yield subtree_root
            yield from self.subtree_inorder(subtree_root.right)
    def postorder (self):
        yield from self.subtree_postorder(self.root)
    def subtree_postorder(self, subtree_root):
        if (subtree_root is None):
            return
        else:
            yield from self.subtree_postorder(subtree_root.left)
            yield from self.subtree_postorder(subtree_root.right)
            yield subtree_root
    def __iter__(self): #we will make this as inorder since that is the most common
        for node in self.inorder():
            yield node.data #we will yield data instead of node
    def breadth_first(self): #add nodes, then removes it, then adds the removed node's children,... I am assuming the queue class is here (its not).
        if (self.is_empty()):
            return
        nodes_q = ArrayQueue()
        nodes_q.enqueue(self.root)
        while(nodes_q.is_empty() == False):
            curr_node = nodes_q.dequeue()
            yield curr_node
            if (curr_node.left is not None):
                nodes_q.enqueue(curr_node.left)
            if (curr_node.right is not None):
                nodes_q.enqueu(curr_node.right)

        



'''
initializing a node with the linkedbinarytree in a different file would be:
node = LinkedBinaryTree.LinkedBinaryTree.Node(1)
we have to first go into the file then into the class to access the function
'''

'''
Analyzing run times for the methods:
    - height: O(n): function visits each node a constant (once in this case) 
                    number of times therefore linear run time. Drawing the recursive tree
                    will make a tree with the same structure as the binary tree
    - sum: O(n): function visits each node and calls function on node.left and node.right on the node 
                 even if left or right is None. This is because the base case is if 
                 the node is None. So the recursion tree will have two additional calls for each leaf
                 and an additional call for each node that doesn't have two children. the function
                 calls n times plus an additional atmost 2n times. n + 2n = 3n = O(3n)
'''



'''
      5
   /     \ 
  2      3
 / \    / \ 
1   6  4   7

traversal sequences of a binary tree:
1. preorder (DLR) - 5, 2, 1, 6, 3, 4, 7
2. inorder (LDR) - 1, 2, 6, 5, 4, 3, 7
3. postorder (LRD) - 1, 6, 2, 4, 7, 3, 5
4. breadth-first - level by level, each from left to right: 5, 2, 3, 1, 6, 4, 7
'''


'''
Expression trees:
expression "(3 + 4) * 2" should be represented as the following tree:

     *
   /   \ 
  +     2
 / \      
3   4  

below is code for above tree
'''
l_ch1 = Node(3)
r_ch1 = Node(4)
l_ch2 = Node('+', l_ch1, r_ch1)
r_ch2 = Node(2)
root = Node('*', l_ch2, r_ch2)
tree = LinkedBinaryTree(root)
#evaluating expression trees
def eval_exp_tree(tree):
    return eval_exp_subtree(tree.root)
def eval_exp_subtree(subtree_root):
    if (subtree_root.left is None and subtree_root.right is None):
        return subtree_root.data
    else:
        left_arg = eval_exp_subtree(subtree_root.left)
        right_arg = eval_exp_subtree(subtree_root.right)
        op = subtree_root.data
        if (op == '+'):
            return left_arg + right_arg
        elif (op == '-'):
            return left_arg - right_arg
        elif (op == '*'):
            return left_arg * right_arg
        elif (op == '/'):
            return left_arg / right_arg
        else:
            raise Exception("Unsupported operation: " + str(op))
