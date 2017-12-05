'''
The Map ADT
Model: A collection that stores values mapped by keys
Operations:
    - m = Map(): creates a new collection
    - m[k] = v: (insert) adds the value v, mapped by k into m. If there 
                already exists a value that is mapped by k it would be 
                replaced with v.
    - m[k]: (find) returns the value associated with k in m (or raises
            a keyrror if nothing is mapped to it)
    - del m[k]: (delete) removes (and returns) the value that is 
                associated with k in m (or raises a KeyError)
    - len(m): returns # of enteries in m
    - iter(m): returns an iterator of the keys in m

Example behavior:

>> m = Map()
>> m['red'] = (255, 0, 0)
>> m['red']
(255, 0, 0)
>> m['green'] = (0, 255, 0)
>> m['blue'] = (0, 0, 255)
>> m['purple'] = (255, 0, 255)
>> del m['green']
(0, 255, 0)
>> m['red'] = (250, 0, 0)
>> m['red']
(250, 0, 0)


Possible Data Structures we can use for Map:

UnsortedArrayMap (using list): 
    - find is O(n)
    - insert is O(n) because we need to check it is a new entry or if we are updating
    - delete is O(n)

UnsortedLinkedListMap:
    - find is O(n)
    - insert is O(n) because we still have to see if the entry is there
    - delete is O(n) because we need to search the key to delete

SortedArrayMap (using list):
    - find is O(log(n)) because binary search
    - insert is O(n) because although we can find the val in log(n) adding will require shifting
    - delete is O(n) (same explanation as above)

SortedLinkedList:
    - find is O(n) because we do not have random access
    - insert is O(n)
    - delete is O(n)

we will use unsortedarraymap
 - the list will contain Item classes which contain the key/value as its fields
'''

class UnsortedArrayMap:
    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value

    def __init__(self):
        self.data = []

    def __setitem__(self, key, value):
        for item in self.data:     #checking if the key is already in the Map. In that case, update the value of the key
            if (item.key == key):  #the reason we can do "for item ..." is because item is a reference to the object item. item.key accesses 
                item.value = value #the key field of the actual class Item. if we however did item = None in the loop, then it wouldnt change self.data
                return
        new_item = UnsortedArrayMap.Item(key, value)
        self.data.append(new_item)
        
    def __getitem__(self, key):
        for item in self.data:
            if (item.key == key):
                return item.value
        raise KeyError("Key Error: " + str(key))

    def __delitem__(self, key):
        for ind in range(len(self.data)):
            if (self.data[ind].key == key):
                val = self.data[ind].value
                self.data.pop(ind)
                return val
        raise KeyError("Key Error: " + str(key))

    def __len__(self):
        return (len(self.data))

    def __iter__(self):
        for item in self.data:
            yield item.key
