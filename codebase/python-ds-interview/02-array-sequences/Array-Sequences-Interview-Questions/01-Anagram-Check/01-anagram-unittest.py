import unittest

def anagram(s1, s2):
    """
    Problem: Anagram Check

    Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word). 

    For example:
        "public relations" is an anagram of "crap built on lies."        
        "clint eastwood" is an anagram of "old west action"
        
    **Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".**
    """
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
        self.assertEqual(anagram('aabbcc', 'aab bcc'), True)
        self.assertEqual(anagram('Hello World', 'World Hello'), True)
        self.assertEqual(anagram('Python', ' Java '), False)

if __name__ == '__main__':
    unittest.main()
