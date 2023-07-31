import unittest

def pair_sum(arr,k):
    """
    Problem - Array Pair Sum

    Given an integer array, output all the ** *unique* ** pairs that sum up to a specific value **k**.

    So the input:
        
        pair_sum([1,3,2,2],4)

    would return 2 pairs:

        (1,3)
        (2,2)

    NOTE: FOR TESTING PURPOSES CHANGE YOUR FUNCTION SO IT OUTPUTS THE NUMBER OF PAIRS
    """
    pass

class TestPair_sum(unittest.TestCase):

    def test_pair_sum(self):
        # Test the function for various inputs
        self.assertEqual(pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        self.assertEqual(pair_sum([1,2,3,1],3),1)
        self.assertEqual(pair_sum([1,3,2,2],4),2)
        print('ALL TEST CASES PASSED')

if __name__ == '__main__':
    unittest.main()    
