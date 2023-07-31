import unittest

def uni_char(s):
    """
    Unique Characters in String

    Problem
    Given a string,determine if it is compreised of all unique characters. For example, the string 'abcde' has all unique characters and should return True. The string 'aabcde' contains duplicate characters and should return false.
    """
    pass

class TestPair_sum(unittest.TestCase):

    def test_pair_sum(self, sol):
        # Test the function for various inputs
        self.assertEqual(uni_char((''), True))
        self.assertEqual(uni_char(('goo'), False))
        self.assertEqual(uni_char(('abcdefg'), True))
        print('ALL TEST CASES PASSED')

if __name__ == '__main__':
    unittest.main() 
