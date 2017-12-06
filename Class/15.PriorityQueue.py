'''
The Priority Queue ADT

Data Model: a collection of priority-value pairs, that come out in an increasing priorities order

Operations for Minimum Priority Queue:
    - p = PriorityQueue()- creates empty priority queue
    - p.insert(pri, val)- inserts an item with priority pri and value val to p
    - p.min()- returns the pair (pri, val) with the lowest priority or raises exception if queue is empty
    - p.delete_min()- removes and returns the pair (pri, val) with the lowest priority or raises exception if empty
    - len(p)
    -
Operations for Maximum Priority Queue are very similar. We will focus on the minimum.



Data Structures for Priority Queues:
    - Unsorted Linked List: (we can keep a min as a field member and insert will check whether the new entry is smaller than min and update it)
        - Min: O(1)
        - Insert: O(1)
        - Delete Min: O(n)
    - Sorted Linked List:
        - Min: O(1)
        - Insert: O(n)
        - Delete Min: O(1)
    - Balanced Search Tree: (AVL) (we can keep a min as a field member and insert will check whether the new entry is smaller than min and update it)
        - Min: O(1)
        - Insert: O(log(n))
        - Delete Min: O(log(n))

Now we have to make a choice of which data structure to use. For all min is O(1) so we have compare insert and delete_min.
A common scenario is n inserts and n deletes. Results for each structure:
    - Unsorted Linked List:
        - Insert: 1 + 1 + 1 + .. = n
        - Delete Min: n + (n-1) + (n-2) + .. + 2 + 1 ~ n^2
        - Total: O(n^2)
    - Sorted Linked List:
        - Insert: 1 + 2 + 3 + 4 + ... + n ~ n^2
        - Delete Min: 1 + 1 + ... = n
        - Total: O(n^2)
    - Balanced Search Tree:
        - Insert: log(1) + log(2) + ...+ log(n) ~ O(nlog(n))
        - Delete Min: log(n) + log(n-1) + .. ~ O(nlog(n))
        - Total: O(nlog(n))
The search tree (AVL) seems to be the best structure to use
'''
    
