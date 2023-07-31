from nose.tools import assert_equal

def uni_char(s):
    """
    Unique Characters in String

    Problem
    Given a string,determine if it is compreised of all unique characters. For example, the string 'abcde' has all unique characters and should return True. The string 'aabcde' contains duplicate characters and should return false.
    """
    pass

class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print('ALL TEST CASES PASSED')
        
if __name__ == '__main__':
    # Run Tests
    t = TestUnique()
    t.test(uni_char)
    print("All tests passed!")
    