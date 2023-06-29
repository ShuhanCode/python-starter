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