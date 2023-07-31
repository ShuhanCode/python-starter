# 59. Sentence Reversal - Interview Problem

<details>
  <summary> <h2> Interview Problems: </h2> </summary>

## Sentence Reversal

### Problem

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

```python
def rev_word(s):
    pass
```

## Test Your Solution

Run the cell below to test your solution

```python
from nose.tools import assert_equal

class ReversalTest(object):
    
    def test(self,sol):
        assert_equal(sol('    space before'),'before space')
        assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print("ALL TEST CASES PASSED")
        
# Run and test
t = ReversalTest()
t.test(rev_word)
```

</details>



##  Resources for this lecture



---

[Previous](./58_Largest-Continuous-Sum-Interview-Problem-SOLUTION.md) | [Next](./60_Sentence-Reversal-Interview-Problem-SOLUTION.md)