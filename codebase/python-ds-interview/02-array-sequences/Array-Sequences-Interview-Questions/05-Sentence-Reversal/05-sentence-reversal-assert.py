from nose.tools import assert_equal

def rev_word(s):
    """
    Problem - Sentence Reversal    

    Given a string of words, reverse all the words. For example:

    Given:        
        'This is the best'

    Return:
        'best the is This'

    As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:

        '  space here'  and 'space here      '

    both become:

        'here space'

    ## Solution

    Fill out your solution below:
    """
    pass

class ReversalTest(object):
    
    def test(self,sol):
        assert_equal(sol('    space before'),'before space')
        assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print("ALL TEST CASES PASSED")
        
if __name__ == '__main__':
    # Run and test
    t = ReversalTest()
    t.test(rev_word)
    print("All tests passed!")
    