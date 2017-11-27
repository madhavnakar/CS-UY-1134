'''
Suppose in a class room we want to map each student with the grade he/she got.
For this purpose we introduce Bucket Array:
    - the indices of the bucketarray would be grade
    - The find, insert and delete would all be O(1)
    - However this is very impractical because if we want to store students with their
      phone numbers then it would need 10^9 places.

Instead we introduce hash tables:
    - find: 0(1) 
    - insert: 0(1)
    - delete: 0(1)
    - 0(1) is average time, it is not worst case!!!!!
    - requires O(n) space


Let V be the set containing all the inputs. Python List will serve as the underlying data structure for hash tables.
Let H be a hash function that maps items from V 

