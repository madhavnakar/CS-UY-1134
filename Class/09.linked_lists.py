'''
Dynamic Arrays:
	Pros:
		- Random access
		- Efficient amortize performance for adding and
		  removing from the end
	Cons:
		- Storing data continuously in the memory can be 
		  a problem for a VERY big data set
		- Insertions and deletions at interior positions
		  of an array are expensive
		- Amortized bounds may be unacceptable in real 
		  time systems
'''

class EmptyCollection(Exception):
    pass

class DoublyLinkedList:
    class Node:
        def __init__(self, data=None, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev
        def disconnect(self): #We need to remove all the references of node when we delete so that
            self.data = None  #the garbage collector can free the used memory. the garbage collector
            self.next = None  #deletes used space if there are no references to it or if the used space
            self.prev = None  #makes no references.

    def __init__(self):
        self.header = DoublyLinkedList.Node() #because the node is not global. It is in a class.
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return (self.size)

    def is_empty(self):
        return (len(self) == 0)

    def first_node(self):
        if (self.is_empty()):
            raise EmptyCollection("List is empty")
        return self.header.next

    def last_node(self):
        if (self.is_empty()):
            raise EmptyCollection("List is empty")
        return self.trailer.prev

    def add_first(self, elem):
        return self.add_after(self.header, elem)

    def add_last(self, elem):
        return self.add_after(self.trailer.prev, elem)

    def add_before(self, node, elem):
        return self.add_after(node.prev, elem)

    def add_after(self, node, elem):
        prev = node
        succ = node.next
        new_node = DoublyLinkedList.Node()
        new_node.data = elem
        new_node.prev = prev
        new_node.next = succ
        prev.next = new_node
        succ.prev = new_node
        self.size += 1
        return new_node

    def delete(self, node):
        prev = node.prev
        succ = node.next
        prev.next = succ
        succ.prev = prev
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def __iter__(self): #makes it iterable like lists are
        if (self.is_empty()): #so that iterating over empty dll doesnt give error
            return
        cursor = self.first_node()
        while (cursor is not self.trailer):
            yield cursor.data
            cursor = cursor.next

    def __str__(self):
        return '[' + '<-->'.join([str(elem) for elem in self]) + ']'
    def __repr__(self):
        return str(self)



def remove_all(lnk_lst, elem): #removes all nodes with elem as the data
    if (lnk_lst.is_empty()): #Calling first_node() on empty list will give error, but we don't 
        return               #want that because logically remove_all of empty list should keep empty list
    cursor = lnk_lst.first_node()
    while (cursor is not lnk_lst.trailer):
        if (cursor.data == elem):
            next_node_saver = cursor.next #Need to go to next node then delete to keep track of cursor
            lnk_lst.delete(cursor)
            cursor = next_node_saver
        else:
            cursor = cursor.next

#we assume that lnk_lst is not empty therefore error will be displayed when called on empty lst
def max_in_linked_list(lnk_lst):
    return max_in_sublinked_list(lnk_lst, lnk_lst.first_node()) #we do this so programmer doesn't have to put first_node() into function call
def max_in_sublinked_list(lnk_lst, sublist_head):
    if (sublist_head.next is lnk_lst.trailer):
        return sublist_head.data
    else:
        rest_max = max_in_sublinked_list(lnk_lst, sublist_head.next)
        if (rest_max > sublist_head.data):
            return rest_max
        else:
            return sublist_head.data




#There are header and tail nodes that have data set to None but have next/prev


#below code for singly linked list, not doubly linked list 
#(not important)
head = None
head = Node()
head.data = 1

head.next = Node()
head.next.data = 2

head.next.next = Node()
head.next.next.data = 3

cursor = head
while(cursor is not None):
        print(cursor.data)
        cursor = cursor.next

new_node = Node()
new_node.data = 4
new_node.next = head
head = new_node


