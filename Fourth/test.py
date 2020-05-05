import unittest

from shortString import shortString as a, error

class Tests(unittest.TestCase):

    def test_extension(self):
        self.assertEqual(a("aaabb"), "3a2b");
        self.assertNotEqual(a("dddee"), "4a2d");

    def test_error(self):
        self.assertRaises(error, a, 5)



if __name__ == '__main__':
    unittest.main()