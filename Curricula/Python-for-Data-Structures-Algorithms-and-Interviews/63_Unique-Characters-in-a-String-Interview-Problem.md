# 63. Unique Characters in a String - Interview Problem

<details>
  <summary> <h2> Interview Problems: </h2> </summary>

## Unique Characters in String

### Problem
Given a string,determine if it is compreised of all unique characters. For example, the string 'abcde' has all unique characters and should return True. The string 'aabcde' contains duplicate characters and should return false.

## Solution

Fill out your solution below:

```python
def uni_char(s):
    pass
```

## Test Your Solution

Run the cell below to test your solution

```python
from nose.tools import assert_equal

class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print('ALL TEST CASES PASSED')
        
# Run Tests
t = TestUnique()
t.test(uni_char)
```

</details>



##  Resources for this lecture



---

[Previous](./62_String-Compression-Interview-Problem-SOLUTION.md) | [Next](./64_Unique-Characters-in-a-String-Interview-Problem-SOLUTION.md)