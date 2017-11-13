'''
Dynamic Arrays:
	1. The data is continuous in the memory
	2. All elements are of the same size
These two conditions allow random access
'''
import ctypes

def make_array(n):
	return (n * ctypes.py_object)()
'''
Above makes an array of size n. The size cannot change
like lists can.
'''

class MyList:
	def __init__(self):
		self.data = make_array(1)
		self.n = 0
		self.capacity = 1
	def __len__(self):
		return (self.n)
	def append(self, val):
		if (self.capacity == self.n):
			self.resize(2 * self.capacity)
		self.data[self.n] = val
		self.n += 1
	def resize(self, new_size):
		new_array = make_array(new_size)
		for i in range(self.n):
			new_array[i] = self.data[i]
		self.data = new_array
		self.capacity = new_size
	def __getitem__(self, ind):
		if (not(0 <= ind <= self.n - 1)):
			raise IndexError(str(ind) + " is an invalid index")
		return (self.data[ind]) #Indicing is supported for arrays, which the data is stored in
		
	def __setitem__(self, ind, val):
		if (not(0 <= ind <= self.n - 1)):
			raise IndexError(str(ind) + " is an invalid index")
		self.data[ind] = val
'''
Worst case of append is linear b/c we would need to resize and copy
Best case of append is Theta(1) b/c we can add elem to the end

Amortized-time: (total cost of n operations) / n
so for append amortized time would be n/n = 1

