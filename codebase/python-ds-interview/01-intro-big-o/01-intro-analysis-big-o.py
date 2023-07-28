import timeit

# First function (Note the use of range since this is in Python 3)
def sum1(n):
    '''
    Take an input of n and return the sum of the numbers from 0 to n
    '''
    final_sum = 0
    for x in range(n+1): 
        final_sum += x
    
    return final_sum

print(sum1(10))

timer1 = timeit.Timer('sum1(10)', globals=globals())

time_taken1 = timer1.timeit(number=1000)

print(f"Time taken by sum1: {time_taken1:.6f} seconds")

def sum2(n):
    """
    Take an input of n and return the sum of the numbers from 0 to n
    """
    return (n*(n+1))/2

print(sum2(10))

timer2 = timeit.Timer('sum2(10)', globals=globals())

time_taken2 = timer2.timeit(number=1000)

print(f"Time taken by sum2: {time_taken2:.6f} seconds")
