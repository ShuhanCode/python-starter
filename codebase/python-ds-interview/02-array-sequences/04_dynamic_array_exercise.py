class M(object):
    
    def public(self):
        print('Use Tab to see me!')
        
    def _private(self):
        print("You won't be able to Tab to see me!")
        
m = M()

m.public()        

m._private()

import ctypes

class DynamicArray(object):
    """
    DYNAMIC ARRAY CLASS (Similar to Python List)
    """
    
    def __init__(self):
        self.n = 0 
        self.capacity = 1
        self.A = self.make_array(self.capacity)
        
    def __len__(self):
        return self.n
    
    def __getitem__(self, k):
        
        if not 0 <= k < self.n:
            return IndexError('k is out of bounds!')
        
        return self.A[k]
    
    def append(self, ele):
        
        if self.n == self.capacity:
            self._resize(2*self.capacity +1) # Double the capacity - Amortized Analysis
            
        self.A[self.n] = ele
        self.n += 1
        
    def _resize(self, new_cap):
        
        B = self.make_array(new_cap)
        
        for k in range (self.n):
            B[k] = self.A[k]
            
        self.A = B
        self.capacity = new_cap
        
        
    def make_array(self, new_cap):
        
        return (new_cap * ctypes.py_object)()
    
    
arr = DynamicArray()

arr.append(1)
print(len(arr))
print(f"capacity 1: {arr.capacity}")

arr.append(2)
print(len(arr))
print(arr[0])
print(arr[1])
print(f"capacity 2: {arr.capacity}")

arr.append(3)
print(f"Length: {len(arr)}")
print(arr[0])
print(arr[1])
print(f"capacity 3: {arr.capacity}")

print()
print("### How to use `sys.getsizeof()` to get an estimate of the memory usage of the `DynamicArray`? ###")
print()

import sys

# Assuming the DynamicArray class is defined as before
dynamic_array = DynamicArray()

# Append some elements to the array
for i in range(100):
    dynamic_array.append(i)

# Get the size of the DynamicArray object in bytes
size_of_dynamic_array = sys.getsizeof(dynamic_array)
print("Size of DynamicArray:", size_of_dynamic_array, "bytes")

print()
print ("### How to use `tracemalloc` to get an estimate of the memory usage of the `DynamicArray`? ###")
print()

import tracemalloc

# Assuming the DynamicArray class is defined as before
dynamic_array = DynamicArray()

# Enable tracing
tracemalloc.start()

# Append some elements to the array
for i in range(100):
    dynamic_array.append(i)

# Measure memory usage after appending elements
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")

for stat in top_stats[:10]:
    print(stat)

# Disable tracing
tracemalloc.stop()

