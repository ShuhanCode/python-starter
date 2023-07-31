# 55. Find the Missing Element - Interview Problem

<details>
  <summary> <h2> Interview Problems: </h2> </summary>

## Find the Missing Element

### Problem

Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array. 

Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

Input:
    
    finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

Output:

    5 is the missing number

## Solution

Fill out your solution below:

```python
ddef finder(arr1,arr2):    
    pass
```

## Test Your Solution

Run the cell below to test your solution

```python
from nose.tools import assert_equal

class TestFinder(object):
    
    def test(self,sol):
        assert_equal(sol([5,5,7,7],[5,7,7]),5)
        assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
        assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        print('ALL TEST CASES PASSED')

# Run test
t = TestFinder()
t.test(finder)
```

</details>



##  Resources for this lecture



---

[Previous](./54_Array-Pair-Sum-Interview-Problem-SOLUTION.md) | [Next](./56_Find-the-Missing-Element-Interview-Problem-SOLUTION.md)