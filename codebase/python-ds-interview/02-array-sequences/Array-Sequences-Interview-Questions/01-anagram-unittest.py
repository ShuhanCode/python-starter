import unittest

def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    return sorted(s1) == sorted(s2)

class TestAnagram(unittest.TestCase):

    def test_anagram(self):
        # Test the function for various inputs
        self.assertEqual(anagram('go go go', 'gggooo'), True)
        self.assertEqual(anagram('abc', 'cba'), True)
        self.assertEqual(anagram('hi man', 'hi     man'), True)
        self.assertEqual(anagram('aabbcc', 'aabbc'), False)
        self.assertEqual(anagram('123', '1 2'), False)

    def test_anagram_with_spaces(self):
        # Test the function with spaces
        self.assertEqual(anagram('aabbcc', 'aab bc'), True)
        self.assertEqual(anagram('Hello World', 'World Hello'), True)
        self.assertEqual(anagram('Python', ' Java '), False)

if __name__ == '__main__':
    unittest.main()
