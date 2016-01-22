"""
Sort a given list of number using merge sort algorithm.
"""


"""
Input: a list of unordered numbers.

Output: an ordered list of the input numbers.
"""
def mergesort(s):
	out = []

	# If input s only has one number, return s.
	if len(s) == 1:
		return s

	mid = len(s) / 2

	# Call mergesort on the left and right halves of s.
	left = mergesort(s[:mid])
	right = mergesort(s[mid:])

	# Merge the two lists.
	i = 0;
	j = 0;
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			out.append(left[i])
			i += 1
			
		else:
			out.append(right[j])
			j += 1
	if i == len(left):
		out = out + right[j:]
	else:
		out = out + left[i:]

	return out

def test():
	# given example
	print "Expected:[-1, 1, 5, 10, 10, 10, 12, 29, 29, 44, 63, 71]" + "\nActual:  "+ str(mergesort([1,10,5,63,29,71,10,12,44,29,10,-1]))

	# base case
	print "Expected:[0]" + "\nActual:  "+ str(mergesort([0]))

	print "Expected:[-99, -30, -2, 0, 0, 1, 2, 2, 2, 17, 34, 182]" + "\nActual:  "+ str(mergesort([-30,1,-2,0,17,2,2,2,0,34,182,-99]))



#test()