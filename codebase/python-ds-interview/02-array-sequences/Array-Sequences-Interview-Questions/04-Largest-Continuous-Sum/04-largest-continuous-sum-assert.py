from nose.tools import assert_equal

def pair_sum(arr,k):
    """
    Problem - Largest Continuous Sum
    
    Given an array of integers (positive and negative) find the largest continuous sum. 

    Solution

    Fill out your solution below:
    """
    pass

class LargeContTest(object):
    def test(self,sol):
        assert_equal(sol([1,2,-1,3,4,-1]),9)
        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
        assert_equal(sol([-1,1]),1)
        print('ALL TEST CASES PASSED')
        
if __name__ == '__main__':
    #Run Test
    t = LargeContTest()
    t.test(large_cont_sum)
    print("All tests passed!")
    