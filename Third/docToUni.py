import unittest
import doctest
import palindrome

def load_tests(loader, tests, ignore):
	tests.addTests(doctest.DocTestSuite(palindrome))
	return tests

if __name__ == '__main__':
    unittest.main()