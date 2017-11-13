def is_prime(n):
	if (n % 2 == 0):
		return False
	for curr in range(1, int(n**(1/2)) + 1, 2):
		if (n % curr == 0):
			return False
	return True
'''
my versio of prime checker
'''

def algo1(n):
	count_divs = 0
	for curr in range(1, num + 1):
		if (n%curr == 0):
 			count_divs += 1
	if(count_divs == 2):
		return True
	else
		return False

def algo2(n):
	count_divs = 0
	for curr in range(1, num/2 + 1):
		if (n%curr == 0):
 			count_divs += 1
	if(count_divs == 1):
		return True
	else
		return False

def algo3(n):
	count_divs = 0
	for curr in range(1, sqrt(num) + 1):
		if (n%curr == 0):
 			count_divs += 1
	if(count_divs == 1):
		return True
	else
		return False


'''
Runtime criteria: We compare the number of primitive operations
executed by a process as a function of the input size: "n."

Algorithms for prime checking

Algo 1: Go from 1 to num: counting the number of primitive operations
will be 1 + 2 + 1 + 5n + 2 = 5n + 6

Algo 2: Go from 1 to num/2: 1 + 3 + 1 + 5(n/2) + 2 = (5/2)n + 7

Algo 3: Go from 1 to sqrt(num): 1 + 3 + 1 + 5(sqrt(n)) + 2 = 5*sqrt(n) + 7

Algo 1 and 2: are both O(n) = n
Algo 3 is O(n) = sqrt(n)

No technology can compensate the gap between different classes of O(n).
In other words, running a logarithmic algo on the slowest computer will
beat a linear algo on the fastest computer.
'''





'''
Big O:
Let f(n) and g(n) be two func that map pos ints to pos real nums. We say
f(n) = O(g(n)) if there exit pos real constant "c" and a positive int 
constant "n_0" such that f(n) <= c*g(n) for all n >= n_0.

- O is used to express <=
- When we say that f = O(g) we mean that g is an upperbound of f

Big Omega:
- Used to express >= 

Theta:
- Expressed equivalency 

'''

'''
Ex: O or Omega
3n^2 + 5n + 7 = O(5n^3 + 3sqrt(n)) b/c ... <= ...
3sqrt(n) + 5 = Omega(120log(n) + 70) b/c ... >= ...
'''




'''
Analyzing runtime of functions:

def print_square(n):
	for i in range(1, n + 1):  - runs n times
		line = '*'*n              - n operations
		print(line)               - n operations
T(n) = n*(2n) = 2n^2
Theta(n) = n^2


def print_triangle(n):
	for i in range(1, n + 1):  - runs n times
		line = '*' * i            - i operations
		print(line)               - i operations
i goes from 1, 2, ... n. The sum of this is T(n) = n(n + 1) / 2 
Theta(n) = n^2


def	prefix_average1(lst):
	n = len(lst)                  - n operations
	res_lst = [0] * n             - n operations
	for i in range(n):         - runs n times
		curr_avg = sum(lst[0: i + 1])/ i + 1      - 2i operations (slicing and summing)
		res_lst[i] = curr_avg                     - 1 operation
	return res_lst
Theta(n) = n^2
	|
	|
	|Better implementation of the above program
	|
	v 
def prefix_average2(lst):_
	n = len(lst)          |
	res_lst = [0] * n     | Linear time (n)
	curr_sum = 0         _| 
	for i in range(n):
		curr_sum += lst[i]             |
		curr_avg = curr_sum/(i + 1)    | Linear time (n)
		res_lst[i] = curr_avg          |
	return res_lst
T(n) = n

'''






'''






