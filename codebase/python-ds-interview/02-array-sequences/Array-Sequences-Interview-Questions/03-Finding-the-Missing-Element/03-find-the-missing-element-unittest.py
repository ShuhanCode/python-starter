import unittest

def finder(arr1,arr2):
    """
    Problem - Find the Missing Element

    Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array. 

    Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

    Input:        
        finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

    Output:
        5 is the missing number

    Solution

    Fill out your solution below:
    """
    pass

class TestFinder(object):
    
    def test(self,sol):
        # Test the function for various inputs
        self.assertEqual(pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        self.assertEqual(pair_sum([1,2,3,1],3),1)
        self.assertEqual(pair_sum([1,3,2,2],4),2)
        print('ALL TEST CASES PASSED')

if __name__ == '__main__':
    unittest.main()    


class TestFinder(object):
    
    def test(self,sol):
        assert_equal(sol([5,5,7,7],[5,7,7]),5)
        assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
        assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        print('ALL TEST CASES PASSED')