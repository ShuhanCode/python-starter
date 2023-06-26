a = 10

print (type(a))

a = 10.00

print (type(a))

# print(' I'm using single quotes, but this will create an error')

print(" I'm using single quotes, but this will create an error")

# String Properties
# It's important to note that strings have an important property known as immutability. This means that once a string is created, the elements within it can not be changed or replaced. For example:

s = 'Hello World'

# s[0] = 'X'

myStr = 'X' + s[1:]

print(myStr)

# split() method
# expected output: ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]

my_str = 'The quick brown fox jumps over the lazy dog.'

words = my_str.split(' ')

print(words)

words = my_str.split()

print(words)

words = my_str.split(' ', 3)

print(words)

letter = 'z'

print(letter*10)

lst = ['x', 'z']

print(lst*10)

tup = ('x', 'z')

print(tup*10)


