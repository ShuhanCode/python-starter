# 61. String Compression - Interview Problem

<details>
  <summary> <h2> Interview Problems: </h2> </summary>

## String Compression

### Problem

Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space. 

The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.

## Solution

Fill out your solution below:

```python
def compress(s):
    pass
```

## Test Your Solution

Run the cell below to test your solution

```python
from nose.tools import assert_equal

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print('ALL TEST CASES PASSED')

# Run Tests
t = TestCompress()
t.test(compress)
```

</details>



##  Resources for this lecture



---

[Previous](./60_Sentence-Reversal-Interview-Problem-SOLUTION.md) | [Next](./62_String-Compression-Interview-Problem-SOLUTION.md)