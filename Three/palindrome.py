import doctest
def isPalindrome(n):
	"""Return boolean whether n is a palindrome
	>>> isPalindrome("hih")
	True
	>>> isPalindrome("no")
	False
	>>> isPalindrome(33)
	True
	>>> isPalindrome(33.2)
	False
	>>> isPalindrome(33.33)
	True
	>>> isPalindrome(-1)
	False
	>>> isPalindrome("Step on no pets")
	True
	>>> isPalindrome(['h','e','l','l','o'])
	False
	"""
	try:
		n = str(n)
	except ValueError:
		raise ValueError("Input must be of basic type")
	n = n.replace(' ','')
	n = n.lower()
	#print(n)
	return n == n[::-1]

if __name__ == "__main__":
    doctest.testmod()