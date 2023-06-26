#  20. Print Formatting FAQs

<details>
  <summary> Section 3: Python Object and Data Structure Basics - 20. Print Formatting FAQs </summary>

**1.) I imported print from the __future__ module, now print isn't working. What happened?**

This is because once you import from the __future__ module in Python 2.7, a print statement will no longer work, and print must then use a print() function. Meaning that you must use

**print('Whatever you were going to print')**

or if you are using some formatting:

**print('This is a string with an {p}'.format(p='insert'))**

The __future__ module allows you to use Python3 functionality in a Python2 environment, but some functionality is overwritten (such as the print statement, or classic division when you import division).

Since we are using Jupyter Notebooks, once you so the import, all cells will require the use if the print() function. You will have to restart Python or start a new notebook to regain the old functionality back.

**HERE IS AN AWESOME SOURCE FOR PRINT FORMATTING:**

https://pyformat.info/

</details>


## Resources for this lecture


-   [Slides: 00-Python Object and Data Structure Basics](https://docs.google.com/presentation/d/1lMiOnSVp1dbTOOLMXJXqDyUJz5-k7n-rVPgQtMj7wcA/edit#slide=id.g2586a91ea0_0_101)

-   [Notebook: String Formatting for Printing](https://colab.research.google.com/drive/1_nnc3aTnTkPpNEWm2LWa_nyvh6OWqiAB#scrollTo=_f_sg_7KB-Nt&line=1&uniqifier=1)

---
[Previous](./19_Print-Formatting-with-Strings.md) | [Next](./21_Lists-in-Python.md)