def count_down(start, end):
	if (start == end):
		print(end)
	else:
		print(end)
		count_down(start, end - 1)

def count_up_and_down(start, end):
	if (start == end):
		print(end)
	else:
		print(start)
		count_up_and_down(start + 1, end)
		print(start)
	
'''
when calling countupanddown on a smaller range it would print the numbers
of that range in an increasing order followed by decreasing order
'''






def factorial(n);
	if (n == 0):
		return (1):
	else:
		rest = factorial(n - 1)
		return (rest * n)
'''
when calling factorial on k < n, it would return k!

the recursive step calls the function n times. Each call has constant 
time operations, such as if and return. Therefore the run time is n
'''




def sum_list(lst):
	if (len(lst) == 1)
		return lst[0]
	else:
		rest = sum_list(lst[1:])
		return (lst[0] + rest)
		
'''
when calling sum_list with a list shorter than lst, it would return the sum
of all the elements in that lst

every recursion lst[1:] makes a new list. So the cost would be n + (n - 1) ... 1. 
This sums to n(n - 1)/2 which is Theta(n^2)
'''






def power(x, n):
	if (n == 1):
		return (x)
	else:
		rest = power(x, n - 1)
		return (rest * x)
'''
T(n) = O(n)
'''
def power2(x, n):
	if (n == 1):
		return (x)
	else:
		part1 = power2(x, n//2)
		part2 = power2(x, n//2)
		if (n % 2 == 0):
			return (part1 * part2)
		else:
			return (x * part1 * part2)
'''
Each call to power2 calls two recursions. The recursion diagram looks like a binary
tree with each node representing a recursion call and pointing to two other 
recursion calls. Since each recursion call costs 1 operation, we need to sum all 
of the "1" operations. The height will be log(n). So the sum will be
1 + 2 + 4 + ... + 2^log(n) which equals 1 + 2 + 4 + ... + n = 2^(log(n)+1) - 1 = 2n - 1.
So this is still O(n). 

power and power2 are still O(n)!!! 

2^0 + 2^1 + 2^2 + ... + 2^n = 2^(n + 1) - 1
'''
def power3(x, n):
	if (n == 1):
		return (x)
	else:
		part = power3(x, n//2)
		if (n % 2 == 0):
			return (part * part)
		else:
			return (x * part * part)
'''
Each recursive call makes one recursive call. n is still being divided by two 
each call. The height will still be log(n) but total cost will be O(log(n)) because the 
recursive call only makes one call.

power3 is significantly better than power and power2
O(log(n))                            O(n)      O(n)

