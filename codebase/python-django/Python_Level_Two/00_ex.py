# s = "Global Variable"

# def func ():
#     mylocal = 10
#     print(locals())
#     print(globals()['s'])

# func()
# print(s)

# def hello(name='Jose'):
#     return 'Hello '+name

# print(hello())

# mynewgreet = hello

# print(mynewgreet())

# def hello(name='Jose'):
#     print('The hello() function has been executed')
#     def greet():
#         return '\t This is inside the greet() function'
#     def welcome():
#         return "\t This is inside the welcome() function"    
     
#     if name == 'Jose':
#         return greet    
#     else:
#         return welcome
    
# x = hello()

# x()

# print(x())


def hello():
    return 'Hi Jose!'

def other (func):
    print('HELLO')
    print(func)

other(hello)