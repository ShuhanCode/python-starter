# 40. Big O Notation

<details>
  <summary> Result: picture capture </summary>

-   `02-big-o-notion.py`

```python
import numpy as np
import matplotlib.pyplot as plt

# Import math module specifically for the log function
from math import log

# Set up runtime comparisons
n = np.linspace(1, 10, 1000)
labels = ['Constant', 'Logarithmic', 'Linear', 'Log Linear', 'Quadratic', 'Cubic', 'Exponential']
big_o = [np.ones(n.shape), np.log(n), n, n*np.log(n), n**2, n**3, 2**n]

# Plot setup
plt.figure(figsize=(12, 10))
plt.ylim(0, 50)

for i in range(len(big_o)):
    plt.plot(n, big_o[i], label=labels[i])

plt.legend(loc=0)
plt.ylabel('Relative Runtime')
plt.xlabel('n')

fig = plt.gcf()
fig.set_size_inches(12, 4)
fig.savefig('../../../imgs/py-ds/02-big-o-notion.png', dpi=300)

# Display the plot
plt.show()

```

- run `python3 02-big-o-notion.py`

<p align="center" >
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-for-Data-Structures-Algorithms-and-Interviews/images/02-big-o-notion.png" width="90%" > 

</p> 

</details>

<details>
  <summary> Codebase: </summary>

-   [02-big-o-notion.py](../../codebase/python-ds-interview/01-intro-big-o/02-big-o-notion.py)

-   [02-Big O Notation.ipynb](https://github.com/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/blob/master/01-Algorithm%20Analysis%20and%20Big%20O/02-Big%20O%20Notation.ipynb)

</details>

##  Resources for this lecture



---

[Previous](./39_Introduction-to-Algorithm-Analysis-and-Big-O.md) | [Next](./41_Big-O-Examples.md)
