import sys

# Set n
n = 10

data = []

for i in range(n):
    
    # Number of elements
    a = len(data)
    
    # Actual size in bytes  
    b = sys.getsizeof(data)
    
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    
    #   increase length by one
    data.append(n)
    
    
    