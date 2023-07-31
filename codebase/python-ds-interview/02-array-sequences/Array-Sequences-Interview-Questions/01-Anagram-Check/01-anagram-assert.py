# def anagram(s1, s2):
#     """
#     Problem: Anagram Check

#     Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word). 

#     For example:
#         "public relations" is an anagram of "crap built on lies."        
#         "clint eastwood" is an anagram of "old west action"
        
#     **Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".**
#     """
#     s1 = s1.replace(' ', '').lower()
#     s2 = s2.replace(' ', '').lower()
#     return sorted(s1) == sorted(s2)


# def test_anagram():
#     # Test the function for various inputs
#     assert anagram('go go go', 'gggooo') == True
#     assert anagram('abc', 'cba') == True
#     assert anagram('hi man', 'hi     man') == True
#     assert anagram('aabbcc', 'aabbc') == False
#     assert anagram('123', '1 2') == False
#     print("ALL TEST CASES PASSED")


# if __name__ == '__main__':
#     # Run the tests
#     test_anagram()
#     print("All tests passed!")


# from nose.tools import assert_equal

# def anagram(s1, s2):
#     """
#     Problem: Anagram Check

#     Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word). 

#     For example:
#         "public relations" is an anagram of "crap built on lies."        
#         "clint eastwood" is an anagram of "old west action"
        
#     **Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".**
#     """
#     s1 = s1.replace(' ','').lower()
#     s2 = s2.replace(' ','').lower()
#     return sorted(s1) == sorted(s2)

# def test_anagram():
#     # Test the function for various inputs
#     assert_equal(anagram('go go go','gggooo'),True)
#     assert_equal(anagram('abc','cba'),True)
#     assert_equal(anagram('hi man','hi     man'),True)
#     assert_equal(anagram('aabbcc','aabbc'),False)
#     assert_equal(anagram('123','1 2'),False)
#     print("ALL TEST CASES PASSED")

# if __name__ == '__main__':
#     # Run the tests
#     test_anagram()
#     print("All tests passed!")
    
from nose.tools import assert_equal

def anagram(s1, s2):
    """
    Problem: Anagram Check

    Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word). 

    For example:
        "public relations" is an anagram of "crap built on lies."        
        "clint eastwood" is an anagram of "old west action"
        
    **Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".**
    """
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    return sorted(s1) == sorted(s2)

class AnagramTest(object):
    
    def test(self,sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print("ALL TEST CASES PASSED")

if __name__ == '__main__':
    # Run Tests
    t = AnagramTest()
    t.test(anagram)
    print("All tests passed!")