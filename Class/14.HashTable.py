'''
BucketArray:
Suppose in a class room we want to map each student with the grade he/she got.
For this purpose we introduce Bucket Array:
    - the indices of the bucketarray would be grade
    - The find, insert and delete would all be O(1)
    - However this is very impractical because if we want to store students with their
      phone numbers then it would need 10^9 places. Moreover, not all domains are integers.


Hash Tables:
Instead we introduce hash tables:
    - find: 0(1) 
    - insert: 0(1)
    - delete: 0(1)
    - 0(1) is average time, it is not worst case!!!!!
    - requires O(n) space


Let V be the set containing all possible inputs (keys). Python List will serve as the underlying data structure for hash tables.
Let H be a hash function that maps items from V to H. We need a function that maps any input to an index (0 to n-1) in the 
data list. The size of V is much greater than the hash table (ie set of all strings could be V, which would make the size of 
V infinite, while H is still 0 to n-1). 



Since V is much bigger, a few keys may be mapped to the same slot (there can be collisions in the mapping).
Collision Resolutions:
    - Chaining: we use a secondary structure in each slot to store all keys that are mapped to there
    - Open Addressing: in case of a collision we try to find an alternative slot for the key



Hash function must have:
    - Uniform Distribution Property: each randomly chosen key is equally likely to be mapped to any slot independently of the
      slots that other keys are mapped to



There is a two step process for hash functions. First the key needs to be mapped to an integer (typically 32 bit), called 
coding function, then use a compression function to make it into an integer between 0 and n-1.

Coding function approaches:
    - Integer casting: Take the lower 4 bytes of the binary representation of k, and look at these 32 bits as an integer. However,
      a lot of objects can differ in the bytes 5 and on but integer casting will treat it as the same.
    - Componant Sum: X = (Xn-1,...,X3, X2, X1, X0), then h(x) = X0 + X1 + X2 + ... + Xn-1. But the position of the components are
      not considered. Words like "stop", "spot", "tops", "pots", and "post" are all mapped to the same slot.
    - Polynomial Accumulation: X = (Xn-1,...,X3, X2, X1, X0), then h(x) = X0 + X1*z^1 + X2*z^2 +...+ Xn-1*z^(n-1), where z is a an
      arbitarary number. This accounts for all the components and their positions moreover it turns out that  if you take z = 33 
      then 50,000 words in English have at most 6 collisions. 

Python has a built in coding function called hash(). But it works on built in immutable types. To make it work in classes we need 
to overload the hash method. (Keys should be immutable). hash of an int is just the int itself.

Compression function approaches:
    - Division Method: h(x) = x mod (n). This satisfies the uniform distribution property but in the real world keys are biased then
      there will be some pattern with the remaineders. Usually we will choose prime as n to eliminate some patterns.
    - MAD (multiply, add, divide) Method: let p be a prime number p > size of possible inputs (V). Let a be a random number: 
      {1, 2,...,p-1}. Let b be a random number: {0, 1,..., p-1}. Then h(x) = [(a*x + b)mod(p)]mod(n)

Runtime for chaining:
    - Worst case: 0(n) b/c if all keys are mapped to the same slot.
    - Best case: 0(1) b/c there are no collisions
    - Expected (average case): Assuming keys are chosen randomly and the hash function satisfies the uniform distribution property,
      then 0(alpha + 1). Where alpha (load factor) is the size of the table over the number of inputs (n/N). The plus 1 is for 
      applying the hash function and accessing the right slot and the alpha is the average cost of scanning the secondary storage.
      If at all times we make sure that n <= c * N, where c is a constant, then alpha <= 1, then the average case is 0(1).
'''

# We will take the built in hash function as the coding function and MAD as the compression function

# We will use the unsortedarraymap as the secondary storage (assume that I imported it correctly). In the secondary storage the key/value
# are stored in a class called item. The seconday storage takes care of storing key/val in item, so we do not have to do that

import UnsortedArrayMap 
import random

class ChainingHashTableMap:
    def __init__(self, N=64, p=6460101079):
        self.N = N
        self.table = [None]*self.N
        self.n = 0
        self.p = p
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)

    def hash_func(self, key): #does coding and compression in one line
        return ((self.a * hash(key) + self.b) % self.p) % self.N

    def __getitem__(self, key):
        j = self.hash_func(key)
        curr_bucket = self.table[j]
        if (curr_bucket is None):
            raise KeyError("Key Error: " + str(key))
        return curr_bucket[key]

    def __setitem__(self, key, value): #unsortedarraymap takes care of search for the key and updating or adding the new key
        j = self.hash_func(key)
        if (self.table[j] is None):
            self.table[j] = UnsortedArrayMap.UnsortedArrayMap()
        old_size = len(self.table[j])
        self.table[j][key] = value
        new_size = len(self.table[j])
        if (new_size > old_size): #Checking if it was a replacement or a new addition
            self.n += 1
        if (self.n > self.N):
            self.rehash(self.N * 2)

    def __delitem__(self, key):
        j = self.hash_func(key)
        curr_bucket = self.table[j]
        if (curr_bucket is None):
            raise KeyError("Key Error: " + str(key))
        del curr_bucket[key] #this will raise an exception if key is not in curr_bucket
        self.n -= 1
        if (len(curr_bucket) == 0):
            self.table[j] = None
        if (self.n < self.N // 4):
            self.rehash(self.N // 2)


    def __len__(self):
        return self.n

    def __iter__(self):
        for curr_bucket in self.table:
            if (curr_bucket is not None):
                for key in curr_bucket:
                    yield key

    def rehash(self, new_size):
        old = []
        for key in self:
            value = self[key]
            old.append((key, value))
        self.table = [None] * new_size
        self.n = 0
        self.N = new_size
        for (key, value) in old:
            self[key] = value

'''
Open Addressing:


Collision Resolutions:
    - Linear Probing: h(x, i) = (h'(x) + i) % N   i = 0, 1, 2, 3, 4, ...
      We basically try next slot if there already is an element in the slot we were assigned to. However linear probing
      encourages clustering.
    - Quadratic probing: h(x, i) = (h'(x) + i^2) % N   i = 0, 1, 2, 3, ...
    - Double hashing: h(x, i) = (h'(x) + i*h''(x)) % N 
'''
