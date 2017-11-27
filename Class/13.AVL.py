'''
AVL Trees:
    - Height Balance Property- for every node n of T, the heights of the children of n differ by at most 1
    - Must be ordered (it is a binary search tree)
Height of AVL Trees then will be O(log(n)).

Runtimes:
    - find: O(log(n))
    - insert: O(log(n))
    - delete: O(log(n))

we will use "rotations" to balance the tree after we insert or delete

AVL Insert:
    - apply the isnert algorithm of k as if the tree is a regular Binary Search Tree. This could violate the balancing property
    - walk from the new node(with k) upwards on the insertion path.

(rest of the notes in the pdf)

Unfortunatly we will not implement AVL trees
'''

