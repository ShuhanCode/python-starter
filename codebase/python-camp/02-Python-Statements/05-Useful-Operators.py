mylist = [1,2,3]

for num in range(3, 10, 2):
    ...
    # print(num)
    
index_count = 0
word = 'abcde'

for _ in word:
    # print(word[index_count])
    index_count += 1
    
# enumerate() function    
    
for index, letter in enumerate(word):
    print(index, letter)    
    
# zip() function

mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c']

new_lst = zip(mylist1, mylist2)

print(new_lst)

for item in new_lst:
    print(item)
    
# in operator

print ('mykey' in {'mykey': 345})

d = {'mykey': 345}

print('mykey' in d)

print('mykey' in d.keys())

print(345 in d.values())

print(('mykey', 345) in d.items())

# min() and max() functions

mylist = [10, 20, 30, 40, 100]

print(min(mylist), max(mylist))

# random library

from random import shuffle

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

shuffle(mylist) # in place function

print(mylist)

from random import randint

print (randint(0, 100))

#   input() function

result = input('Enter a number here: ')

print(result)

print('{result} you putin type is {type}'.format(result=result, type=type(result)))