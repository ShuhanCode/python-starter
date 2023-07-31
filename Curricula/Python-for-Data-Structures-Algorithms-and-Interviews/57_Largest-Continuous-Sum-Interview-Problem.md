# 57. Largest Continuous Sum - Interview Problem

<details>
  <summary> <h2> Interview Problems: </h2> </summary>

## Largest Continuous Sum

### Problem
Given an array of integers (positive and negative) find the largest continuous sum. 

## Solution

Fill out your solution below:

```python
def large_cont_sum(arr): 
    pass
```

## Test Your Solution

Run the cell below to test your solution

```python
from nose.tools import assert_equal

class LargeContTest(object):
    def test(self,sol):
        assert_equal(sol([1,2,-1,3,4,-1]),9)
        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
        assert_equal(sol([-1,1]),1)
        print('ALL TEST CASES PASSED')
        
#Run Test
t = LargeContTest()
t.test(large_cont_sum)
```

</details>



##  Resources for this lecture



---

[Previous](./56_Find-the-Missing-Element-Interview-Problem-SOLUTION.md) | [Next](./58_Largest-Continuous-Sum-Interview-Problem-SOLUTION.md)