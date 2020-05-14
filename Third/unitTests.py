import unittest
import palindrome as p

class TestStringMethods(unittest.TestCase):
	def test_string(self):
		self.assertTrue(p.isPalindrome("Nan"))
		self.assertFalse(p.isPalindrome("Nani"))
	def test_string_with_spaces(self):
		self.assertTrue(p.isPalindrome("Step on no pets"))
	def test_int(self):
		self.assertTrue(p.isPalindrome(3333))
		self.assertFalse(p.isPalindrome(33331))
	def test_float(self):
		self.assertTrue(p.isPalindrome(33.33))
		self.assertFalse(p.isPalindrome(133.33))



		
if __name__ == '__main__':
	unittest.main()