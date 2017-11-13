def linear_search(lst, val):
	for i in range(len(lst)):
		if (lst[i] == val):
			return i
	return None
'''
Worst Case: n
'''

def binary_search(srt_lst, val):
	l = 0
	r = len(srt_lst) - 1
	ind = None
	found = False
	while (found and left <= right):
		mid = (l + r)//2
		if (srt_lst[mid] == val):
			found = True
			ind = mid
		elif (srt_lst[mid] > val):
			r = mid - 1
		else:
			l = mid + 1
	return ind
