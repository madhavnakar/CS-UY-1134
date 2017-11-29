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
'''
      
