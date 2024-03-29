# 17. split() Method

- Javascript

```js
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

- Python

```py
# split() method
# expected output: ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]

my_str = 'The quick brown fox jumps over the lazy dog.'

words = my_str.split(' ')

print(words)

words = my_str.split()

print(words)

words = my_str.split(' ', 3)

print(words)
```
