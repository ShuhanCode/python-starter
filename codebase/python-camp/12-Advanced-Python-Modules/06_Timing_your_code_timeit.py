def func_one (n):
    return [str(num) for num in range(n)]

print(func_one(10)) # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def func_two (n):
    return list(map(str, range(n)))

print(func_two(10)) # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


import time

# CURRENT TIME BEFORE

start_time = time.time()

# RUN CODE

result = func_one(1)

# CURRENT TIME AFTER RUNNING CODE

end_time = time.time()

# ELAPSED TIME

elapsed_time = end_time - start_time

print(elapsed_time) 

# CURRENT TIME BEFORE

start_time = time.time()

# RUN CODE

result = func_two(1)

# CURRENT TIME AFTER RUNNING CODE

end_time = time.time()

# ELAPSED TIME

elapsed_time = end_time - start_time

print(elapsed_time) 

import timeit

stmt = '''  
func_one(100)
'''

setup = '''
def func_one (n):
    return [str(num) for num in range(n)]
'''

result = timeit.timeit(stmt, setup, number=1000000)

print(result) 

stmt = '''  
func_two(100)
'''

setup = '''
def func_two (n):
    return list(map(str, range(n)))
'''

result = timeit.timeit(stmt, setup, number=1000000)

print(result) 


# import timeit

def func_one (n):
    return [str(num) for num in range(n)]

# Measure the execution time of func_one(100) using timeit
execution_time = timeit.timeit(lambda: func_one(100), number=1)

# Print the execution time
print(f"Execution time: {execution_time} seconds")


