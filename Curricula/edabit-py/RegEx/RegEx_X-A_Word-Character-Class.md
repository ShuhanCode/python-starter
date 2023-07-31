# RegEx X-A: Word Character Class

[RegEx X-A: Word Character Class](https://edabit.com/challenge/mtfCmMo9fL5yqB3Sy)

Write the regular expression that matches all alphabetic characters in a string. Use the character class \w in your expression.

**Example**

```python
    txt = "**^&$Regular#$%Expressions$%$$%^**"
    pattern = "yourregularexpressionhere"

    " ".join(re.findall(pattern, txt)) ➞ "Regular Expressions"
```

**Notes**

You **don't** need to write a function, just the pattern.
Do **not** remove `import re` from the code.
Find more info on RegEx and alternation in the Resources tab.
You can find all the challenges of this series in my [Basic RegEx](https://edabit.com/collection/8PEq2azWDtAZWPFe2) collection.

**Solution** 

```
import re

pattern = '\w+'
```

