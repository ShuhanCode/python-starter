# 39. Introduction to Algorithm Analysis and Big O

<details>
  <summary> Slides: Introduction to Algorithm Analysis and Big O </summary>

<p align="center" >
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-for-Data-Structures-Algorithms-and-Interviews/images/39_Introduction-to-Algorithm-Analysis-and-Big-O.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-for-Data-Structures-Algorithms-and-Interviews/images/39_Introduction-to-Algorithm-Analysis-and-Big-O_2.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-for-Data-Structures-Algorithms-and-Interviews/images/39_Introduction-to-Algorithm-Analysis-and-Big-O_3.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-for-Data-Structures-Algorithms-and-Interviews/images/39_Introduction-to-Algorithm-Analysis-and-Big-O_4.png" width="90%" > 

</p> 

</details>

<details>
  <summary> Result: picture capture </summary>

-   `01-intro-analysis-big-o.py`

```python
import timeit

# First function (Note the use of range since this is in Python 3)
def sum1(n):
    '''
    Take an input of n and return the sum of the numbers from 0 to n
    '''
    final_sum = 0
    for x in range(n+1): 
        final_sum += x
    
    return final_sum

print(sum1(10))

timer1 = timeit.Timer('sum1(10)', globals=globals())

time_taken1 = timer1.timeit(number=1000)

print(f"Time taken by sum1: {time_taken1:.6f} seconds")

def sum2(n):
    """
    Take an input of n and return the sum of the numbers from 0 to n
    """
    return (n*(n+1))/2

print(sum2(10))

timer2 = timeit.Timer('sum2(10)', globals=globals())

time_taken2 = timer2.timeit(number=1000)

print(f"Time taken by sum2: {time_taken2:.6f} seconds")

```

- run `python3 01-intro-analysis-big-o.py`

```bash
55
Time taken by sum1: 0.000760 seconds
55.0
Time taken by sum2: 0.000153 seconds
```

</details>

<details>
  <summary> Codebase: </summary>

-   [01-intro-analysis-big-o.py](../../codebase/python-ds-interview/01-intro-big-o/01-intro-analysis-big-o.py)

-   [01-Introduction to Algorithm Analysis and Big O .ipynb](https://github.com/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/blob/master/01-Algorithm%20Analysis%20and%20Big%20O/01-Introduction%20to%20Algorithm%20Analysis%20and%20Big%20O%20.ipynb)

</details>

##  Resources for this lecture



---

[Previous](./38_Algorithm-Analysis-and-Big-O-Section-Overview.md) | [Next](./40_Big-O-Notation.md)
