# 47. Dynamic Array

<details>
  <summary> Slides: Dynamic Array </summary>

<p align="center" >
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-for-Data-Structures-Algorithms-and-Interviews/images/47_Dynamic-Array.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-for-Data-Structures-Algorithms-and-Interviews/images/47_Dynamic-Array_2.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-for-Data-Structures-Algorithms-and-Interviews/images/47_Dynamic-Array_3.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-for-Data-Structures-Algorithms-and-Interviews/images/47_Dynamic-Array_4.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-for-Data-Structures-Algorithms-and-Interviews/images/47_Dynamic-Array_5.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-for-Data-Structures-Algorithms-and-Interviews/images/47_Dynamic-Array_6.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-for-Data-Structures-Algorithms-and-Interviews/images/47_Dynamic-Array_7.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-for-Data-Structures-Algorithms-and-Interviews/images/47_Dynamic-Array_8.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-for-Data-Structures-Algorithms-and-Interviews/images/47_Dynamic-Array_9.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-for-Data-Structures-Algorithms-and-Interviews/images/47_Dynamic-Array_10.png" width="90%" > 

</p> 

</details>

<details>
  <summary> Result: print or picture capture </summary>

-   `03_dynamic_array.py`

```python
import sys

# Set n
n = 10

data = []

for i in range(n):
    
    # Number of elements
    a = len(data)
    
    # Actual size in bytes  
    b = sys.getsizeof(data)
    
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    
    #   increase length by one
    data.append(n)    
```

-   run `python 03_dynamic_array.py`

```bash
Length:   0; Size in bytes:   56
Length:   1; Size in bytes:   88
Length:   2; Size in bytes:   88
Length:   3; Size in bytes:   88
Length:   4; Size in bytes:   88
Length:   5; Size in bytes:  120
Length:   6; Size in bytes:  120
Length:   7; Size in bytes:  120
Length:   8; Size in bytes:  120
Length:   9; Size in bytes:  184
```

</details>  

<details>
  <summary> Codebase: </summary>

-   [03_dynamic_array.py](../../codebase/python-ds-interview/02-array-sequences/03_dynamic_array.py)

-   [02-Array Sequences](https://github.com/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/tree/master/02-Array%20Sequences)

</details>

##  Resources for this lecture



---

[Previous](./46_Low-Level-Arrays.md) | [Next](./48_Dynamic-Array-Excercise.md)
