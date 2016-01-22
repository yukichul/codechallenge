from math import sqrt

"""
Find the nth prime number given a positive integer n.
"""

"""
Helper function: Check if an integer is a prime number.

Input: integer

Output: true - num is a prime number; 
		false - num is not a prime number.

"""
def isprime(num):
	# 2 is a prime number
    if num == 2: return True
    # If num is less than 2 or num is an even number other than 2, num is not a prime number.
    if num < 2 or num % 2 == 0: return False
    return not any(num % i == 0 for i in range(3, int(sqrt(num)) + 1, 2))


"""
Input: positive integer n

Output: the nth prime number
"""

def findprime(n):
	# invalid input
	if n <= 0 or n % 1 != 0:
		return "invalid input"

	count = 1
	candidate = 3

	if n == 1:
		return 2

	while count < n:
		if isprime(candidate):
			count += 1
		candidate += 2

	return candidate - 2


def test():
	# Given cases
	print "Expected: 5 Expected: " + str(findprime(3))
	print "Expected: 271 Expected: " + str(findprime(58))
	print "Expected: 104743 Expected: " + str(findprime(10001))

	# More cases
	print "Expected: 2 Expected: " + str(findprime(1))
	print "Expected: invalid input Expected: " + str(findprime(0))


#test()