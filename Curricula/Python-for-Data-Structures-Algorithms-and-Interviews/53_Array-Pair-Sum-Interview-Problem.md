# 53. Array Pair Sum - Interview Problem

<details>
  <summary> <h2> Interview Problems: </h2> </summary>

## Array Pair Sum

### Problem

Given an integer array, output all the ***unique*** pairs that sum up to a specific value **k**.

So the input:
    
    pair_sum([1,3,2,2],4)

would return **2** pairs:

     (1,3)
     (2,2)

**NOTE: FOR TESTING PURPOSES CHANGE YOUR FUNCTION SO IT OUTPUTS THE NUMBER OF PAIRS**

## Solution

Fill out your solution below:

```python
def pair_sum(arr,k):
    pass
```

## Test Your Solution

Run the cell below to test your solution

```python
from nose.tools import assert_equal

class TestPair(object):
    
    def test(self,sol):
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print('ALL TEST CASES PASSED')

#Run tests
t = TestPair()
t.test(pair_sum)
print("All tests passed!")
```

</details>



##  Resources for this lecture



---

[Previous](./52_Anagram-Check-Interview-Problem-SOLUTION.md) | [Next](./54_Array-Pair-Sum-Interview-Problem-SOLUTION.md)