#  17. String Properties and Methods

-   [00-Python Object and Data Structure Basics](https://docs.google.com/presentation/d/1lMiOnSVp1dbTOOLMXJXqDyUJz5-k7n-rVPgQtMj7wcA/edit#slide=id.g2586a91ea0_0_101)

**Note**

-   `String.prototype.split() - javascript`
```
const str = 'The quick brown fox jumps over the lazy dog.';

const words = str.split(' ');
console.log(words);
// expected output: ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]

const chars = str.split('');
console.log(chars);
// expected output: ["T", "h", "e", " ", "q", "u", "i", "c", "k", " ", "b", "r", "o", "w", "n", " ", "f", "o", "x", " ", "j", "u", "m", "p", "s", " ", "o", "v", "e", "r", " ", "t", "h", "e", " ", "l", "a", "z", "y", " ", "d", "o", "g", "."]

const strCopy = str.split();
console.log(strCopy);
// expected output: Array ["The quick brown fox jumps over the lazy dog."]

```

-   `Python`
```
const my_str = 'The quick brown fox jumps over the lazy dog.';

const words = my_str.split();
print(words);
// expected output: ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]
```




---
[Previous](./16_Indexing-and-Slicing-with-Strings.md) | [Next](./18_Strings-FAQ.md)