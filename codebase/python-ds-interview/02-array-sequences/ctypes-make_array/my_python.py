print("### 1. How to us `ctypes` in Python? ###")
print()

import ctypes

# Load the shared library
my_library = ctypes.CDLL('./my_library.so')

# Specify function return types and argument types
my_library.add.restype = ctypes.c_int
my_library.add.argtypes = [ctypes.c_int, ctypes.c_int]

my_library.multiply.restype = ctypes.c_double
my_library.multiply.argtypes = [ctypes.c_double, ctypes.c_double]

# Call the C functions from Python
result_add = my_library.add(10, 5)
result_multiply = my_library.multiply(3.14, 2.0)

print("Result of add:", result_add)  # Output: Result of add: 15
print("Result of multiply:", result_multiply)  # Output: Result of multiply: 6.28


# how to use ctypes to create a C-style array in Python

print()
print("### 2. How to use ctypes to create a C-style array in Python ###")
print()

# import ctypes

class DynamicArray(object):
    """
    DYNAMIC ARRAY CLASS (Similar to Python List)
    """
    
    # ... (Other methods and constructor as defined in the initial code) ...
    
    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()

# Creating an instance of DynamicArray
dynamic_array = DynamicArray()

# Using make_array to create a new array
new_capacity = 10
new_array = dynamic_array.make_array(new_capacity)

# The new_array is a dynamic array with a capacity of 10.
# It can store Python objects, similar to a Python list.
# However, it's not directly accessible as a Python list, and you need to work with it using ctypes or other low-level approaches.

# For example, you can store values in the new array using ctypes:
for i in range(new_capacity):
    new_array[i] = i * 2

# Accessing elements in the new array:
for i in range(new_capacity):
    print(new_array[i])

# Note: This new_array is a C-style array and not directly usable as a Python list.
# If you want a dynamic array similar to Python's list, you should use the DynamicArray class and its append method as described in the initial code.
