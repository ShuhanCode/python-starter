def say_hello(name='NAME'):
    """
    DOCSTRING: Information about the function
    input:  name    
    output: Hello name
    """
    print(f"Hello {name}")
    
# help(say_hello)    

say_hello()
say_hello('Jose')

def sum_numbers(num1, num2):
    return num1 + num2

result = sum_numbers(10, 20)

print(result)

# num1 = 10
# num2 = input('Please provide a number: ')

# num2 = int(num2) # type casting

# result = sum_numbers(num1, num2)

# print(result)

# Interactions between functions

from random import shuffle

example = [1, 2, 3, 4, 5, 6, 7]

# shuffle(example) # in place function

# print(example)

def shuffle_list(mylist):
    shuffle(mylist) # in place function
    return mylist

# result = shuffle_list(example)

# print(result)

# mylist = [' ', 'O', ' ']

# print(shuffle_list(mylist))

def player_guess():
    guess = ''

    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0, 1, or 2: ")
        
    return int(guess)

# player_guess()

def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("Correct!")
    else:
        print("Wrong guess!")
        print(mylist)
        
# Initial list
mylist = [' ', 'O', ' ']

# Shuffle list
mixedup_list = shuffle_list(mylist)

# User guess
# guess = player_guess()

# Check guess

# check_guess(mixedup_list, guess)

# *args and **kwargs in Python

def myfunc (*args):
    return args

print(myfunc(10, 20, 30, 40, 50))

print(*(10, 20, 30, 40, 50))

print(*[10, 20, 30, 40, 50])

print(*{10, 20, 30, 40, 50})

print(*{'key1': 'value1', 'key2': 'value2'})

print(*{'key1': 'value1', 'key2': 'value2'}.keys())

print(*{'key1': 'value1', 'key2': 'value2'}.values())

print(*{'key1': 'value1', 'key2': 'value2'}.items())

myStr = 'Hello'

print(*myStr)


def my_func (**kwargs):
    return kwargs

print(my_func(key1='value1', key2='value2')) # {'key1': 'value1', 'key2': 'value2'}

# print(my_func({'key1': 'value1', 'key2': 'value2'})) # TypeError: my_func() takes 0 positional arguments but 1 was given

def myfunc(*args, **kwargs):
    print(args) # (10, 20, 30)
    print(kwargs) # {'fruit': 'orange', 'food': 'eggs', 'animal': 'dog'}
    print('I would like {} {}'.format(args[0], kwargs['food'])) # I would like 10 eggs
    
myfunc(10, 20, 30, fruit='orange', food='eggs', animal='dog')    