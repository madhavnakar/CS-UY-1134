def my_range_list(start, stop, step):
	lst = []
	while (start < stop):
		lst.append(start)
		start += step
	return (lst)

for elem in my_range_list(3, 7, 0.5):
	print(elem, end = ' ')
print()





def f():
	x = 1
	yield x
	
	x += 1
	yield x

	x += 1
	yield x
g = f() 

'''
- g is a generator (a type of an iterator)
- therefore we can call next on g. (ie next(g) will be 1)
however, after doing next(g) three times (returns 1, 2, 3),
it will give 'stop iteration' error.
- this only happens if you set a var to f(). If you do for
example, next(f()), it will always return 1, because doing that
it makes new generators
'''






def my_range(start, stop, step):
	while (start < stop)
		yield start
		start += step
'''
- r = my_range(1, 3, 0.5). type(r) will return <class, 'generator'>.
calling next(r) will have the effect as calling next(g) previously
'''
for elem in my_range(3, 7, 0.5):
	print()
'''
- executing the above code will have an output 3, 3.5, 4,..., 6.5 
- the for loop calls next for us, we dont do it
- my_range is an iterator, not an interatorable object (eg list). For 
loop accepts both, therefore having iterator in for loop is valid. iter 
of an iterator is the same object
'''






def factors(num):
	for curr in range(1, num + 1):
		if (num % curr == 0):
			yield curr
'''
- this is called 'lazy evaluation' which means it allows to produce an
implicit sequence. 1) doesnt contain the entire sequence all at once 
inside the memory 2) not calculated up front (b/c of yield), but breaks 
the execution to steps that are triggered on demand
'''






def is_prime(num):
	count = 0
	for curr in range(1, num + 1):
		if (num % curr == 0):
			count += 1
	if (count == 2):
		return True
	return False





