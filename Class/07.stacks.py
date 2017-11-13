'''
Stack Abstract Data Type (ADT)
- LIFO mathematical model
Operations:
	Stack() creates an empty stack
	S.is_empty(): returns true iff S is an empty stack
	len(S): returns number of elements currently in S
	S.push(elem): adds elem to S
	S.pop(): removes the top elem from S
	S.top(): returns the top elem in S w/o removing it
'''


'''
S = Stack()
S.push(7)
S.push(5)
S.push(10)
S.pop() -- returns 10 and removes it
S.top() -- return 5
len(S) -- returns 2
S.push(2)
S.pop() -- returns 2 and removes it
'''

'''
Below exception class has to do with inheritance
'''
class EmptyCollection(Exception):
	pass
		
class ArrayStack:
	def __init__(self):
		self.data = []
	def __len__(self):
		return(len(self.data))
	def is_empty(self):
		return(len(self) == 0)
	def push(self, elem):
		self.data.append(elem)
	def pop(self):
		if (self.is_empty()):
			raise EmptyCollection("Stack is empty")
		return (self.data.pop())
	def top(self):
		if (self.is_empty()):
			raise EmptyCollection("Stack is empty")
		return (self.data[-1])

'''
to use this class in a different file, write:
'''
import ArrayStack
'''
then we have to go into the ArrayStack namespace.
So to create an instance in the new file:
'''
S = ArrayStack.ArrayStack()







'''
Pretend for below code that we are in a different file
We aren't extending the ADT, we are making a function (not
a method) to use locally
'''
import ArrayStack

#assume there are at least two elements in the stack
def second_top(stack):
	return(stack.data[-2])
'''
This works, but it is a very bad implementation,
because by accessing the data, we are breaking the abstraction 
layer. We want to separate the implementation and interface.
Doing this, we are assuming that the stack.data is implemented
the way we did it. We can reverse the implementation ie last 
elem of stack being the first in the lst. This implementation 
would make our function useless.

We want to keep a layer of abstraction because we want to give
the implementers the freedom of changing the implementation
without breaking our function
'''
'''
Better implementation. No abstraction layer is broken by 
accessing internal imlementations.
'''
def second_top(stack):
	temp = stack.pop()
	res = stack.top()
	stack.push(temp)
	return res
	


'''
Analyzing the worst case runtime of ArrayStack
'''
__init__ method (creating a stack): Theta(1)
length function: 					Theta(1)
is_empty: 							Theta(1)
push								Theta(1) amortized
pop									Theta(1) amortized b/c shinking the list
top									Theta(1)

'''
Conceptually, runtime stack behaves like our stack. When the 
last function ends, then every previous function ends. Follows the 
LIFO model.
'''


'''
Below function prints a string in reverse order using a stack.
Pretend it is done in a different file so we have to import
'''
def print_in_reverse(text):
	letter_stack = ArrayStack.ArrayStack()
	for ch in text:
		letter_stack.push(ch)
	while(letter_stack.is_empty == False):
		ch = letter_stack.pop()
		print(ch, end = '')
	print('')






'''
Infix, Postfix, Prefix notations (Polish notations)

Infix:
- 	5
-	3 + 2
- 	(5 - 3)*4
- 	5 - (3 * 4)
-	(5 + 2)*(8 - 3)/4

Postfix
- 	5
- 	3 2 +
- 	5 3 - 4 *
- 	5 3 4 * -
-	5 2 + 8 3 - * 4 /

Prefix
- 	5
- 	+ 3 2
- 	* - 5 3 4
- 	- 5 * 3 4
-	/ * + 5 2 - 8 3 4

*Prefix and postfix not reverse
**Postfix/Prefix do not need parenthesis
'''

'''
Program to evaluate postfix notations using stacks:
- While the string of postfix notation has a digit, keep pushing.
When a symbol comes, pop last two elems in stack and perform the
operation on the two elems. Then take the result ans push it back into
the stack. Keep iterating over the string.
'''
import ArrayStack #assume this function is written in a different file
def eval_postfix_exp(exp_str):
	operators = "+-*/"
	exp_lst = exp_str.split() #To split the tokens by whitespaces
	A = ArrayStack.ArrayStack()
	for token in exp_lst:
		if (token not in operators):
			S.push(int(token))
		else:
			arg2 = S.pop() #first that comes out is second number in operation
			arg1 = S.pop()
			if (token == '+'):
				res = arg1 + arg2
			elif (token  == '-'):
				res = arg1 - arg2
			elif (token == '*'):
				res = arg1 * arg2
			else:
				res = arg1 / arg2
			S.push(res)
	return (S.pop())
	
